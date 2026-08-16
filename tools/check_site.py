#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
check_site.py — soát ngân hàng câu hỏi và các khối tương tác trước khi xuất bản.

    python tools/check_site.py          # thoát mã 1 nếu còn lỗi

Bắt những lỗi mà `mkdocs build --strict` không thấy được, đặc biệt là lỗi hay
gặp nhất khi soạn tay: chèn hoặc xóa một phương án rồi quên sửa chỉ số `answer`.
Mắt người không bắt được lỗi này, máy bắt trong tích tắc.

Ngoài phần kỹ thuật, script còn soát cả **chất lượng sư phạm**: đủ số câu theo
kế hoạch từng chương, mỗi câu gắn đúng khối và đúng CLO mà chương ấy phục vụ
theo ma trận mục 6.1 của đề cương, và Chương 4, 5 có đủ tỷ lệ câu tình huống.

Nó cũng soát trang Đề cương: trang này chỉ được đăng **kết luận cuối cùng**,
không đăng đoạn giải trình thay đổi hay ghi chú dành cho người ra đề.
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")
QUIZ = os.path.join(DOCS, "quiz")

CLO_HOP_LE = {"CLO1", "CLO2", "CLO3"}
KHOI_HOP_LE = {"A", "B1", "B2", "V"}

# Kế hoạch bám đề cương DBS201 ban hành 2026.
#
# Ma trận đề trắc nghiệm cuối kỳ (Rubric 4): khối A 60% số câu đo CLO2, khối
# B1 15% (tình huống ràng buộc toàn vẹn — Chương 4) và B2 25% (tình huống chuẩn
# hóa — Chương 5) đo CLO3. Nghĩa là Chương 1, 2, 3 KHÔNG có câu khối B nào
# trong đề cuối kỳ; phần CLO3 của Chương 2 và 3 được đo bằng hai bài kiểm tra
# VIẾT (Rubric 2 tuần 5, Rubric 3 tuần 6) — câu luyện theo dạng đó ghi khối "V".
#
#   khoi     : các khối được phép xuất hiện trong chương
#   khoi_bat : khối bắt buộc phải có mặt, kèm tỷ lệ tối thiểu
#   clo      : các CLO chương này phục vụ, theo ma trận mục 6.1
KE_HOACH = {
    1: {"cau": 12, "the": 6, "muc_tieu": 6,
        "khoi": {"A"}, "khoi_bat": {}, "clo": {"CLO2"}},
    2: {"cau": 15, "the": 8, "muc_tieu": 9,
        "khoi": {"A", "V"}, "khoi_bat": {"V": 0.3}, "clo": {"CLO2", "CLO3"}},
    3: {"cau": 15, "the": 8, "muc_tieu": 8,
        "khoi": {"A", "V"}, "khoi_bat": {"V": 0.3}, "clo": {"CLO2", "CLO3"}},
    4: {"cau": 15, "the": 7, "muc_tieu": 8,
        "khoi": {"A", "B1"}, "khoi_bat": {"B1": 0.4}, "clo": {"CLO2", "CLO3"}},
    5: {"cau": 18, "the": 8, "muc_tieu": 10,
        "khoi": {"A", "B2"}, "khoi_bat": {"B2": 0.4}, "clo": {"CLO2", "CLO3"}},
}


def utf8_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def soat_chuong(n, path, loi, canh):
    w = "chuong-%d.json" % n
    try:
        d = json.load(io.open(path, encoding="utf-8"))
    except ValueError as e:
        loi.append("%s: không phải JSON hợp lệ — %s" % (w, e))
        return

    if d.get("chuong") != n:
        loi.append('%s: trường "chuong" là %r, phải là %d' % (w, d.get("chuong"), n))

    kh = KE_HOACH.get(n) or {}
    qs = d.get("questions") or []
    ids = set()
    dem_khoi = dict((k, 0) for k in KHOI_HOP_LE)
    clo_thay = set()

    for i, q in enumerate(qs, 1):
        v = "%s · câu %d" % (w, i)
        qid = q.get("id")
        if not qid:
            loi.append('%s: thiếu "id"' % v)
        elif qid in ids:
            loi.append("%s: id %r bị trùng" % (v, qid))
        else:
            ids.add(qid)

        opts = q.get("options") or []
        if len(opts) < 2:
            loi.append("%s: chỉ có %d phương án, cần ít nhất 2" % (v, len(opts)))
        if len(set(opts)) != len(opts):
            loi.append("%s: có hai phương án trùng nội dung" % v)

        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a < len(opts)):
            loi.append("%s: answer = %r nằm ngoài khoảng 0..%d"
                       % (v, a, max(0, len(opts) - 1)))

        if not (q.get("explain") or "").strip():
            loi.append("%s: thiếu giải thích — mọi câu đều phải nói vì sao đúng/sai" % v)
        elif len(q["explain"]) < 60:
            canh.append("%s: giải thích chỉ %d ký tự, có vẻ quá ngắn"
                        % (v, len(q["explain"])))

        if not (q.get("q") or "").strip():
            loi.append("%s: thiếu nội dung câu hỏi" % v)

        khoi = q.get("block")
        if khoi not in KHOI_HOP_LE:
            loi.append("%s: block = %r, phải là %s"
                       % (v, khoi, " / ".join(sorted(KHOI_HOP_LE))))
        else:
            dem_khoi[khoi] += 1
            if kh.get("khoi") and khoi not in kh["khoi"]:
                loi.append("%s: khối %s không thuộc chương này — đề cương xếp "
                           "Chương %d vào %s"
                           % (v, khoi, n, " / ".join(sorted(kh["khoi"]))))

        clo = q.get("clo")
        if clo not in CLO_HOP_LE:
            loi.append("%s: clo = %r, đề cương chỉ có CLO1, CLO2, CLO3" % (v, clo))
        else:
            clo_thay.add(clo)
            if kh.get("clo") and clo not in kh["clo"]:
                loi.append("%s: %s không thuộc chương này — ma trận mục 6.1 xếp "
                           "Chương %d vào %s"
                           % (v, clo, n, " / ".join(sorted(kh["clo"]))))

    if kh:
        if len(qs) != kh["cau"]:
            canh.append("%s: có %d câu, kế hoạch là %d" % (w, len(qs), kh["cau"]))
        if len(d.get("cards") or []) != kh["the"]:
            canh.append("%s: có %d thẻ lật, kế hoạch là %d"
                        % (w, len(d.get("cards") or []), kh["the"]))
        if len(d.get("selfcheck") or []) != kh["muc_tieu"]:
            canh.append("%s: bảng tự đánh giá có %d dòng, chương có %d mục tiêu"
                        % (w, len(d.get("selfcheck") or []), kh["muc_tieu"]))

    # phủ chuẩn đầu ra: mọi CLO mà chương này phục vụ đều phải có câu đo
    for c in sorted(kh.get("clo") or ()):
        if c not in clo_thay:
            loi.append("%s: chương phục vụ %s nhưng không có câu nào đo %s"
                       % (w, c, c))

    # tỷ lệ khối bắt buộc — Chương 4 và 5 phải có đủ câu tình huống, vì đó là
    # phần duy nhất đo CLO3 của hai chương ấy trong đề cuối kỳ
    for k, nguong in (kh.get("khoi_bat") or {}).items():
        if not qs:
            continue
        tl = dem_khoi[k] / len(qs)
        if tl < nguong:
            canh.append("%s: khối %s chỉ chiếm %.0f%% (%d/%d), nên từ %.0f%% trở lên"
                        % (w, k, tl * 100, dem_khoi[k], len(qs), nguong * 100))

    for j, c in enumerate(d.get("cards") or [], 1):
        if not (c.get("front") or "").strip() or not (c.get("back") or "").strip():
            loi.append("%s · thẻ %d: thiếu mặt trước hoặc mặt sau" % (w, j))

    for j, s in enumerate(d.get("selfcheck") or [], 1):
        if not (s.get("text") or "").strip():
            loi.append("%s · tự đánh giá dòng %d: thiếu nội dung" % (w, j))
        if s.get("clo") and s["clo"] not in CLO_HOP_LE:
            loi.append("%s · tự đánh giá dòng %d: clo = %r không hợp lệ"
                       % (w, j, s["clo"]))

    ta = " · ".join("%s %d" % (k, dem_khoi[k])
                    for k in ("A", "B1", "B2", "V") if dem_khoi[k])
    print("  Chương %d: %2d câu (%s) · %d thẻ · %d dòng tự đánh giá"
          % (n, len(qs), ta or "chưa gắn khối",
             len(d.get("cards") or []), len(d.get("selfcheck") or [])))


# Trang đề cương chỉ đăng kết luận cuối cùng. Những cụm này là dấu hiệu của
# đoạn giải trình thay đổi hoặc ghi chú dành cho người ra đề — nếu lọt lên site
# nghĩa là bộ lọc DE_CUONG_BO trong build_docs.py cần bổ sung.
DAU_HIEU_DIEN_GIAI = [
    "bản đề cương gốc", "người ra đề", "đoàn kiểm định", "constructive alignment",
    "Bắt buộc khi ra đề", "Khuyến nghị 2 giảng viên", "Cảnh báo về tính giá trị",
    "Ma trận đề bắt buộc", "Lưu ý kỹ thuật khi nhập điểm", "khoản dư",
    "bỏ tiêu chí này", "là mắt xích duy nhất", "là chỗ duy nhất đo",
]


def soat_de_cuong(canh):
    """Bắt đoạn diễn giải lọt lên trang đề cương dành cho người học."""
    p = os.path.join(DOCS, "de-cuong.md")
    if not os.path.exists(p):
        return
    txt = io.open(p, encoding="utf-8").read()
    thay = [c for c in DAU_HIEU_DIEN_GIAI if c in txt]
    if thay:
        for c in thay:
            canh.append('de-cuong.md: còn đoạn diễn giải chứa "%s" — bổ sung vào '
                        'DE_CUONG_BO trong build_docs.py' % c)
    else:
        print("  Đề cương: sạch, không còn đoạn diễn giải nào")


def soat_lien_ket(loi):
    """Mọi data-src trong trang phải trỏ tới file có thật."""
    for thu_muc, _, files in os.walk(DOCS):
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(thu_muc, f)
            txt = io.open(p, encoding="utf-8").read()
            for src in re.findall(r'data-src="([^"]+)"', txt):
                dich = os.path.join(DOCS, src)
                if not os.path.exists(dich):
                    loi.append("%s: data-src trỏ tới %s nhưng file không tồn tại"
                               % (os.path.relpath(p, ROOT), src))


def main():
    utf8_stdout()
    loi, canh = [], []
    if not os.path.isdir(QUIZ):
        print("✖ Không có thư mục docs/quiz")
        return 1

    print("SOÁT ngân hàng câu hỏi")
    co = False
    for n in sorted(KE_HOACH):
        p = os.path.join(QUIZ, "chuong-%d.json" % n)
        if os.path.exists(p):
            co = True
            soat_chuong(n, p, loi, canh)
        else:
            print("  Chương %d: chưa soạn" % n)
    if not co:
        loi.append("chưa có file câu hỏi nào trong docs/quiz")

    soat_de_cuong(canh)
    soat_lien_ket(loi)

    print()
    for c in canh:
        print("  ▲ %s" % c)
    for e in loi:
        print("  ✖ %s" % e)
    print("\n%d lỗi · %d cảnh báo" % (len(loi), len(canh)))
    if loi:
        print("✖ Dừng: sửa hết lỗi rồi chạy lại.")
        return 1
    print("✔ Đạt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
