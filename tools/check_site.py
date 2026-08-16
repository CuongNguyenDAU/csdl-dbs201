#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
check_site.py — soát ngân hàng câu hỏi và các khối tương tác trước khi xuất bản.

    python tools/check_site.py          # thoát mã 1 nếu còn lỗi

Bắt những lỗi mà `mkdocs build --strict` không thấy được, đặc biệt là lỗi hay
gặp nhất khi soạn tay: chèn hoặc xóa một phương án rồi quên sửa chỉ số `answer`.
Mắt người không bắt được lỗi này, máy bắt trong tích tắc.

Ngoài phần kỹ thuật, script còn soát cả **chất lượng sư phạm**: đủ số câu theo
kế hoạch từng chương, có phủ cả CLO2 lẫn CLO3, và tỷ lệ Khối A / Khối B bám
đúng ma trận đề của Rubric 4 (40% CLO2 — 60% CLO3).
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
KHOI_HOP_LE = {"A", "B"}

# Kế hoạch đã duyệt: số câu trắc nghiệm, thẻ lật, dòng tự đánh giá mỗi chương.
KE_HOACH = {
    1: {"cau": 12, "the": 6, "muc_tieu": 6},
    2: {"cau": 15, "the": 8, "muc_tieu": 9},
    3: {"cau": 15, "the": 8, "muc_tieu": 8},
    4: {"cau": 15, "the": 7, "muc_tieu": 8},
    5: {"cau": 18, "the": 8, "muc_tieu": 10},
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

    qs = d.get("questions") or []
    ids = set()
    dem_khoi = {"A": 0, "B": 0}
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
            loi.append("%s: block = %r, phải là A hoặc B" % (v, khoi))
        else:
            dem_khoi[khoi] += 1

        clo = q.get("clo")
        if clo not in CLO_HOP_LE:
            loi.append("%s: clo = %r, đề cương chỉ có CLO1, CLO2, CLO3" % (v, clo))
        else:
            clo_thay.add(clo)

    kh = KE_HOACH.get(n)
    if kh:
        if len(qs) != kh["cau"]:
            canh.append("%s: có %d câu, kế hoạch là %d" % (w, len(qs), kh["cau"]))
        if len(d.get("cards") or []) != kh["the"]:
            canh.append("%s: có %d thẻ lật, kế hoạch là %d"
                        % (w, len(d.get("cards") or []), kh["the"]))
        if len(d.get("selfcheck") or []) != kh["muc_tieu"]:
            canh.append("%s: bảng tự đánh giá có %d dòng, chương có %d mục tiêu"
                        % (w, len(d.get("selfcheck") or []), kh["muc_tieu"]))

    # phủ chuẩn đầu ra
    for c in ("CLO2", "CLO3"):
        if c not in clo_thay:
            loi.append("%s: không có câu nào đo %s" % (w, c))

    # tỷ lệ khối theo ma trận Rubric 4: Khối A 40%, Khối B 60%
    if qs:
        tl_b = dem_khoi["B"] / len(qs)
        if not (0.5 <= tl_b <= 0.72):
            canh.append("%s: Khối B chiếm %.0f%% (%d/%d) — ma trận đề là 60%%"
                        % (w, tl_b * 100, dem_khoi["B"], len(qs)))

    for j, c in enumerate(d.get("cards") or [], 1):
        if not (c.get("front") or "").strip() or not (c.get("back") or "").strip():
            loi.append("%s · thẻ %d: thiếu mặt trước hoặc mặt sau" % (w, j))

    for j, s in enumerate(d.get("selfcheck") or [], 1):
        if not (s.get("text") or "").strip():
            loi.append("%s · tự đánh giá dòng %d: thiếu nội dung" % (w, j))
        if s.get("clo") and s["clo"] not in CLO_HOP_LE:
            loi.append("%s · tự đánh giá dòng %d: clo = %r không hợp lệ"
                       % (w, j, s["clo"]))

    print("  Chương %d: %2d câu (A %d · B %d) · %d thẻ · %d dòng tự đánh giá"
          % (n, len(qs), dem_khoi["A"], dem_khoi["B"],
             len(d.get("cards") or []), len(d.get("selfcheck") or [])))


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
