#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build_docs.py — cắt file bài giảng Markdown thành các trang cho MkDocs.

    python tools/build_docs.py            # dựng cả 5 chương
    python tools/build_docs.py 1          # chỉ dựng chương 1

Nguồn `noi-dung/Bai-giang_Chuong-N_*.md` có cấu trúc 12 mục đồng nhất ở cả 5
chương, nên cắt được bằng cách tách theo dòng `## `. Ánh xạ:

    MỤC TIÊU CHƯƠNG + DẪN NHẬP        → chuong-N/index.md
    ## n.m. Tên mục                    → chuong-N/n-m-slug.md   (một trang mỗi mục)
    TÓM TẮT + ba DANH MỤC              → chuong-N/tom-tat.md
    CÂU HỎI ÔN TẬP                     → chuong-N/on-tap.md   (+ khối tương tác)
    BÀI TẬP CHƯƠNG                     → chuong-N/bai-tap.md  (+ lời giải)
    TÀI LIỆU THAM KHẢO                 → gộp vào tom-tat.md
    PHỤ LỤC nA (dành cho giảng viên)   → BỎ, không lên site sinh viên

Script chạy lại được nhiều lần. Nó KHÔNG đụng tới `docs/quiz/*.json` và
`loi-giai/*.md` — hai thứ đó viết tay, script chỉ đọc để chèn vào.
"""
import io
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "noi-dung")
DOCS = os.path.join(ROOT, "docs")
GIAI = os.path.join(ROOT, "loi-giai")

CHUONG = {
    1: ("Bai-giang_Chuong-1_Tong-quan-CSDL.md", "Tổng quan về cơ sở dữ liệu"),
    2: ("Bai-giang_Chuong-2_Mo-hinh-ER.md", "Mô hình thực thể – liên kết"),
    3: ("Bai-giang_Chuong-3_Mo-hinh-quan-he.md", "Mô hình dữ liệu quan hệ"),
    4: ("Bai-giang_Chuong-4_Rang-buoc-toan-ven.md", "Ràng buộc toàn vẹn"),
    5: ("Bai-giang_Chuong-5_Ly-thuyet-thiet-ke-chuan-hoa.md", "Lý thuyết thiết kế và chuẩn hóa"),
}

# Khối trích dẫn `> **Nhãn.**` đổi thành khung màu của Material.
KHUNG = [
    (r"Định nghĩa", "note", "Định nghĩa"),
    (r"Ví dụ", "example", "Ví dụ"),
    (r"Chú ý", "warning", "Chú ý"),
    (r"Ghi nhớ", "tip", "Ghi nhớ"),
]


def utf8_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def slug(s):
    """Bỏ dấu, chỉ giữ chữ thường và gạch nối — GitHub Pages phân biệt hoa thường."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("đ", "d").replace("Đ", "D")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)


def cat_sections(text):
    """Tách theo dòng `## `, trả về [(tiêu đề, nội dung), ...]."""
    parts = re.split(r"^## +(.+?) *$", text, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


def go_khung(body):
    """`> **Định nghĩa 2.1.** …` → `!!! note "Định nghĩa 2.1"` kèm thụt lề 4 dấu cách."""
    lines = body.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^> \*\*(%s)([^*]*?)\.?\*\*\s*(.*)$"
                     % "|".join(k[0] for k in KHUNG), ln)
        if not m:
            out.append(ln)
            i += 1
            continue
        nhan, so, dau = m.group(1), m.group(2).strip(), m.group(3)
        kieu = next(k[1] for k in KHUNG if k[0] == nhan)
        tieu = ("%s %s" % (nhan, so)).strip()
        block = [dau] if dau.strip() else []
        i += 1
        while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
            if lines[i].strip() == "":
                # dòng trống chỉ thuộc khối nếu ngay sau đó vẫn còn `>`
                if i + 1 < len(lines) and lines[i + 1].startswith(">"):
                    block.append("")
                    i += 1
                    continue
                break
            block.append(re.sub(r"^> ?", "", lines[i]))
            i += 1
        out.append('!!! %s "%s"' % (kieu, tieu.replace('"', "'")))
        out.append("")
        for b in block:
            out.append(("    " + b) if b.strip() else "")
        out.append("")
    return "\n".join(out)


def ha_bac(body):
    """Hạ một bậc tiêu đề: `###` → `##`, vì tiêu đề mục lớn đã thành H1 của trang."""
    return re.sub(r"^(#{3,6}) ", lambda m: "#" * (len(m.group(1)) - 1) + " ", body, flags=re.M)


def sua_anh(body):
    """Ảnh tĩnh nằm ở docs/hinh-ve/, trang nằm ở docs/chuong-N/ nên lùi một cấp."""
    return body.replace("](hinh-ve/", "](../hinh-ve/")


def don(body):
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"


def chuan(body):
    return don(sua_anh(ha_bac(go_khung(body))))


def doc_loi_giai(n):
    """`loi-giai/chuong-N.md` cắt theo `## A1` → {'A1': 'markdown lời giải'}."""
    p = os.path.join(GIAI, "chuong-%d.md" % n)
    if not os.path.exists(p):
        return {}
    txt = io.open(p, encoding="utf-8").read()
    parts = re.split(r"^## +([ABC]\d+) *$", txt, flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip()
            for i in range(1, len(parts), 2)}


def chen_loi_giai(body, giai):
    """Chèn khối gập `??? success` ngay sau mỗi bài tập."""
    if not giai:
        return body
    lines = body.split("\n")
    out, cur = [], None

    def xa():
        if cur and cur in giai:
            out.append("")
            out.append('??? success "Lời giải bài %s"' % cur)
            out.append("")
            for ln in giai[cur].split("\n"):
                out.append(("    " + ln) if ln.strip() else "")
            out.append("")

    for ln in lines:
        m = re.match(r"^\*\*Bài ([ABC]\d+)\.?\*\*", ln)
        end = re.match(r"^#{2,6} ", ln)
        if m or end:
            xa()
            cur = m.group(1) if m else None
        out.append(ln)
    xa()
    return "\n".join(out)


def go_goi_y(body):
    """`**Gợi ý trả lời một số câu**` → khối gập, sinh viên tự nghĩ trước."""
    m = re.search(r"^\*\*Gợi ý trả lời một số câu\*\*\s*$", body, flags=re.M)
    if not m:
        return body
    dau, cuoi = body[:m.start()], body[m.end():]
    khoi = ['??? note "Gợi ý trả lời một số câu — thử tự trả lời trước khi mở"', ""]
    for ln in cuoi.strip().split("\n"):
        khoi.append(("    " + ln) if ln.strip() else "")
    return dau.rstrip() + "\n\n" + "\n".join(khoi) + "\n"


def khoi_tuong_tac(n):
    """Ba khối củng cố kiến thức, dữ liệu nằm ở docs/quiz/chuong-N.json.

    `data-src` tính từ GỐC site, không phải từ trang — hoclieu.js tự ghép tiền
    tố. Lý do: MkDocs không viết lại đường dẫn trong thuộc tính data-*, mà bật
    use_directory_urls thì đường dẫn tương đối lệch một cấp."""
    src = "quiz/chuong-%d.json" % n
    return "\n".join([
        "",
        "## Trắc nghiệm tự kiểm tra",
        "",
        "Chọn phương án rồi bấm **Kiểm tra**. Mỗi câu đều có giải thích vì sao đúng",
        "và vì sao các phương án còn lại sai. Tiến độ được lưu ngay trên máy của bạn.",
        "",
        '<div class="hl-quiz" data-src="%s"></div>' % src,
        "",
        "## Thẻ lật khái niệm",
        "",
        "Nhấp vào thẻ để lật xem định nghĩa.",
        "",
        '<div class="hl-cards" data-src="%s"></div>' % src,
        "",
        "## Tự đánh giá theo mục tiêu chương",
        "",
        "Tự đối chiếu xem đã đạt từng mục tiêu của chương chưa.",
        "",
        '<div class="hl-check" data-src="%s"></div>' % src,
        "",
    ])


def trang_slide(n):
    """Liệt kê các buổi slide có sẵn của chương."""
    files = sorted(f for f in os.listdir(os.path.join(DOCS, "slide"))
                   if re.match(r"Slide_Chuong-%d_Buoi-\d+\.html$" % n, f))
    if not files:
        return None
    out = ["# Slide bài giảng — Chương %d" % n, "",
           "Bản trình chiếu tương tác: trắc nghiệm tự chấm, thẻ lật, kéo–thả.",
           "Dùng phím `→` `←` để chạy từng đoạn, `N` để xem kịch bản.", ""]
    for f in files:
        buoi = re.search(r"Buoi-(\d+)", f).group(1)
        out += ["## Buổi %s" % buoi, "",
                '[Mở toàn màn hình](../slide/%s){ .md-button .md-button--primary target=_blank }' % f,
                "",
                '<iframe src="../slide/%s" loading="lazy" class="hl-slide"></iframe>' % f,
                ""]
    return "\n".join(out)


def dung_chuong(n):
    fn, ten = CHUONG[n]
    txt = io.open(os.path.join(SRC, fn), encoding="utf-8").read()
    # bỏ ghi chú biên soạn dành cho người soạn sách
    txt = re.sub(r"^> \*\*Ghi chú biên soạn.*?$", "", txt, flags=re.M | re.S if False else re.M)
    secs = cat_sections(txt)
    out = os.path.join(DOCS, "chuong-%d" % n)
    if not os.path.exists(out):
        os.makedirs(out)

    muc_tieu = dan_nhap = tom_tat = on_tap = bai_tap = tai_lieu = ""
    danh_muc, trang_muc, nav = [], [], []

    for tieu, body in secs:
        if tieu.startswith("MỤC TIÊU"):
            muc_tieu = body
        elif tieu.startswith("DẪN NHẬP"):
            dan_nhap = body
        elif tieu.startswith("TÓM TẮT"):
            tom_tat = body
        elif tieu.startswith("CÂU HỎI ÔN TẬP"):
            on_tap = body
        elif tieu.startswith("BÀI TẬP"):
            bai_tap = body
        elif tieu.startswith("TÀI LIỆU THAM KHẢO"):
            tai_lieu = body
        elif tieu.startswith("PHỤ LỤC"):
            continue                      # dành cho giảng viên — không lên site
        elif tieu.startswith("DANH MỤC"):
            danh_muc.append((tieu, body))
        else:
            m = re.match(r"^(\d+)\.(\d+)\.\s*(.+)$", tieu)
            if m:
                trang_muc.append((m.group(1), m.group(2), m.group(3).strip(), body))

    # --- index.md ---
    idx = ["# Chương %d. %s" % (n, ten), "", "## Mục tiêu chương", "",
           chuan(muc_tieu), "", "## Dẫn nhập", "", chuan(dan_nhap), "",
           "## Các mục trong chương", ""]
    for a, b, t, _ in trang_muc:
        idx.append("- [%s.%s. %s](%s-%s-%s.md)" % (a, b, t, a, b, slug(t)))
    ghi(os.path.join(out, "index.md"), "\n".join(idx))
    nav.append(("Chương %d. %s" % (n, ten), "chuong-%d/index.md" % n))

    # --- mỗi mục lớn một trang ---
    for i, (a, b, t, body) in enumerate(trang_muc):
        name = "%s-%s-%s.md" % (a, b, slug(t))
        page = ["# %s.%s. %s" % (a, b, t), "", chuan(body), ""]
        prev_ = "index.md" if i == 0 else "%s-%s-%s.md" % (
            trang_muc[i - 1][0], trang_muc[i - 1][1], slug(trang_muc[i - 1][2]))
        next_ = "tom-tat.md" if i == len(trang_muc) - 1 else "%s-%s-%s.md" % (
            trang_muc[i + 1][0], trang_muc[i + 1][1], slug(trang_muc[i + 1][2]))
        page += ["---", "",
                 "[← Trang trước](%s) · [Trang sau →](%s)" % (prev_, next_), ""]
        ghi(os.path.join(out, name), "\n".join(page))
        nav.append(("%s.%s. %s" % (a, b, t), "chuong-%d/%s" % (n, name)))

    # --- tóm tắt + danh mục + tài liệu ---
    tt = ["# Tóm tắt Chương %d" % n, "", chuan(tom_tat), ""]
    if tai_lieu:
        tt += ["## Tài liệu tham khảo của chương", "", chuan(tai_lieu), ""]
    for tieu, body in danh_muc:
        tt += ["## %s" % tieu.title(), "", chuan(body), ""]
    ghi(os.path.join(out, "tom-tat.md"), "\n".join(tt))
    nav.append(("Tóm tắt", "chuong-%d/tom-tat.md" % n))

    # --- ôn tập + ba khối tương tác ---
    ot = ["# Ôn tập Chương %d" % n, "", "## Câu hỏi ôn tập", "",
          don(sua_anh(ha_bac(go_goi_y(go_khung(on_tap))))), khoi_tuong_tac(n)]
    ghi(os.path.join(out, "on-tap.md"), "\n".join(ot))
    nav.append(("Ôn tập và trắc nghiệm", "chuong-%d/on-tap.md" % n))

    # --- bài tập + lời giải ---
    giai = doc_loi_giai(n)
    bt = ["# Bài tập Chương %d" % n, "",
          chen_loi_giai(don(sua_anh(ha_bac(go_khung(bai_tap)))), giai), ""]
    ghi(os.path.join(out, "bai-tap.md"), "\n".join(bt))
    nav.append(("Bài tập", "chuong-%d/bai-tap.md" % n))

    # --- slide ---
    sl = trang_slide(n)
    if sl:
        ghi(os.path.join(out, "slide.md"), sl)
        nav.append(("Slide bài giảng", "chuong-%d/slide.md" % n))

    print("  Chương %d: %d mục lớn → %d trang · %d lời giải chèn vào"
          % (n, len(trang_muc), len(nav), len(giai)))
    return nav


def ghi(path, text):
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip() + "\n")


# Mục nào của đề cương thì đưa lên site cho sinh viên xem. Những mục quản lý
# đào tạo nội bộ (ma trận CLO–PLO còn bỏ trống, cách tính điểm, phiếu chấm mẫu,
# nhật ký thay đổi) không đưa lên.
DE_CUONG_LAY = [
    r"^3\. Mô tả", r"^4\. Mục tiêu", r"^5\. Chuẩn đầu ra",
    r"^7\. Đánh giá", r"^7\.1", r"^7\.2", r"^7\.3", r"^7\.4", r"^7\.5",
    r"^8\.", r"^9\.", r"^10\.", r"^11\.",
]

# Trang đề cương trên site chỉ công bố KẾT LUẬN CUỐI CÙNG. Những đoạn dưới đây
# là lập luận, giải trình thay đổi so với bản gốc, hoặc hướng dẫn dành riêng cho
# người ra đề — không đăng cho người học.
#
# Khớp theo cụm mở đầu của đoạn hoặc của khối trích dẫn. Thêm bớt ở đây khi đề
# cương đổi; script in ra danh sách đã bỏ và đã giữ để soát lại.
DE_CUONG_BO = [
    # giải trình thay đổi so với bản đề cương gốc
    "Về bộ chuẩn đầu ra",
    "Một điều chỉnh về câu chữ của CLO3",
    # lập luận vì sao có tiêu chí rubric
    "Tiêu chí 1.3 là mắt xích",
    "Tiêu chí 1.4 là chỗ duy nhất",
    "Đây là thành phần đánh giá giữa học phần và nằm đúng giữa",
    # hướng dẫn dành cho người ra đề và người chấm
    "Bắt buộc khi ra đề",
    "Khuyến nghị 2 giảng viên chấm độc lập",
    "Sơ đồ ER phát trong đề",
    "Cảnh báo về tính giá trị",
    "Ma trận đề bắt buộc",
    "Ví dụ câu đúng chuẩn cho khối",
    "CLO3 tuyên bố ở mức Nhận thức",
    "Lưu ý kỹ thuật khi nhập điểm",
    # tính toán phân bổ quỹ tự học nội bộ
    "Tỷ lệ chuẩn",
]


def _mo_dau(dong):
    """Bỏ dấu trích dẫn, emoji và đánh dấu đậm để lấy cụm mở đầu."""
    t = re.sub(r"^>\s*", "", dong)
    t = re.sub(r"[\U0001F300-\U0001FAFF☀-➿]", "", t)
    return re.sub(r"[*_`]", "", t).strip()


def bo_dien_giai(body, bo_ra, giu_lai):
    """Loại các đoạn và khối trích dẫn mang tính diễn giải khỏi trang đề cương."""
    khoi, cur, la_tq = [], [], False
    for ln in body.split("\n") + [""]:
        tq = ln.startswith(">")
        if ln.strip() == "" or tq != la_tq:
            if cur:
                khoi.append((la_tq, cur))
            cur, la_tq = [], tq
            if ln.strip() == "":
                khoi.append((None, [""]))
                continue
        cur.append(ln)
        la_tq = tq
    if cur:
        khoi.append((la_tq, cur))

    out = []
    for loai, dong in khoi:
        if loai is None:
            out += dong
            continue
        dau = _mo_dau(dong[0])
        if any(dau.startswith(p) for p in DE_CUONG_BO):
            bo_ra.append(dau[:60])
            continue
        if loai:
            giu_lai.append(dau[:60])
        out += dong
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def dung_de_cuong():
    p = os.path.join(SRC, "De-cuong_DBS201_2026.md")
    if not os.path.exists(p):
        print("  (bỏ qua đề cương: không tìm thấy file nguồn)")
        return
    txt = io.open(p, encoding="utf-8").read()
    out = ["# Đề cương học phần", "",
           "Trích các phần liên quan trực tiếp tới người học: mục tiêu, chuẩn đầu ra,",
           "cách đánh giá kèm rubric, kế hoạch giảng dạy và kế hoạch tự học.", ""]
    giu, bo_ra, giu_lai = 0, [], []
    for tieu, body in cat_sections(txt):
        lay = any(re.match(r, tieu) for r in DE_CUONG_LAY)
        if not lay:
            continue
        giu += 1
        body = bo_dien_giai(body, bo_ra, giu_lai)
        out += ["## %s" % re.sub(r"\s*\*\(.*?\)\*\s*$", "", tieu).strip(),
                "", don(ha_bac(go_khung(body))), ""]
    ghi(os.path.join(DOCS, "de-cuong.md"), "\n".join(out))
    print("  Đề cương: giữ %d mục · bỏ %d đoạn diễn giải" % (giu, len(bo_ra)))
    for t in bo_ra:
        print("      ✂ bỏ  : %s…" % t)
    for t in giu_lai:
        print("      ✓ giữ : %s…" % t)


def main():
    utf8_stdout()
    ns = [int(a) for a in sys.argv[1:] if a.isdigit()]
    if not ns:
        # Không nêu chương cụ thể thì chỉ dựng những chương ĐÃ SẴN SÀNG, tức là
        # đã có ngân hàng câu hỏi. Nhờ vậy CI không dựng ra các chương còn dở,
        # và một chương tự lên sóng đúng lúc soạn xong phần củng cố của nó.
        ns = [n for n in sorted(CHUONG)
              if os.path.exists(os.path.join(DOCS, "quiz", "chuong-%d.json" % n))]
        chua = [n for n in sorted(CHUONG) if n not in ns]
        if chua:
            print("Bỏ qua chương chưa có ngân hàng câu hỏi: %s"
                  % ", ".join(str(n) for n in chua))
    print("Dựng trang từ %s" % SRC)
    nav = {}
    for n in ns:
        nav[n] = dung_chuong(n)
    dung_de_cuong()
    # ghi gợi ý nav để dán vào mkdocs.yml
    lines = []
    for n in sorted(nav):
        lines.append("  - Chương %d:" % n)
        for ten, path in nav[n]:
            lines.append("      - %s: %s" % (ten, path))
    ghi(os.path.join(ROOT, "tools", "nav-goi-y.yml"), "\n".join(lines))
    print("\n✔ Xong. Gợi ý cây nav ghi ở tools/nav-goi-y.yml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
