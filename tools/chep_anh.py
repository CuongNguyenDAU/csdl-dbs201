#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chep_anh.py — chép những ảnh mà bài giảng tham chiếu từ thư mục soạn thảo
sang `docs/hinh-ve/`, nén lại cho vừa web.

    python tools/chep_anh.py                       # nguồn mặc định: ../BAI-GIANG-MOI/hinh-ve
    python tools/chep_anh.py "D:/duong/dan/hinh-ve"

Chỉ chép ảnh có trong `![…](hinh-ve/…)` của `noi-dung/*.md`, không chép cả
thư mục (bên soạn thảo còn nhiều ảnh dùng cho slide). Ảnh JPEG thu về tối đa
1400 px cạnh dài, chất lượng 82 — ảnh Wikimedia gốc 1–2 MB xuống còn 100–300
KB mà trên trang không phân biệt được. PNG (sơ đồ vẽ tay) giữ nguyên.

Chạy lại được nhiều lần: ảnh đích mới hơn ảnh nguồn thì bỏ qua.
"""
import glob
import io
import os
import re
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC_MAC_DINH = os.path.join(os.path.dirname(ROOT), "BAI-GIANG-MOI", "hinh-ve")
DICH = os.path.join(ROOT, "docs", "hinh-ve")

CANH_DAI_MAX = 1400
CHAT_LUONG = 82


def anh_tham_chieu():
    refs = set()
    for f in glob.glob(os.path.join(ROOT, "noi-dung", "Bai-giang_Chuong-*.md")):
        txt = io.open(f, encoding="utf-8").read()
        refs |= set(re.findall(r"!\[[^\]]*\]\(hinh-ve/([^)\s]+)", txt))
    return sorted(refs)


def chep(src, dst):
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return "giữ"
    d = os.path.dirname(dst)
    if not os.path.exists(d):
        os.makedirs(d)
    if not src.lower().endswith((".jpg", ".jpeg")):
        with open(src, "rb") as a, open(dst, "wb") as b:
            b.write(a.read())
        return "chép"
    im = Image.open(src)
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    w, h = im.size
    ty_le = min(1.0, CANH_DAI_MAX / float(max(w, h)))
    if ty_le < 1.0:
        im = im.resize((int(w * ty_le), int(h * ty_le)), Image.LANCZOS)
    im.save(dst, "JPEG", quality=CHAT_LUONG, optimize=True, progressive=True)
    return "nén"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    src_dir = sys.argv[1] if len(sys.argv) > 1 else SRC_MAC_DINH
    if not os.path.isdir(src_dir):
        print("Không thấy thư mục nguồn: %s" % src_dir)
        return 1
    thieu, tong = [], 0
    for r in anh_tham_chieu():
        src, dst = os.path.join(src_dir, r), os.path.join(DICH, r)
        if not os.path.exists(src):
            thieu.append(r)
            continue
        kq = chep(src, dst)
        kb = os.path.getsize(dst) / 1024.0
        tong += kb
        print("  %-4s %-48s %6.0f KB" % (kq, r, kb))
    print("Tổng %.1f MB trong docs/hinh-ve" % (tong / 1024.0))
    if thieu:
        print("THIẾU %d ảnh trong nguồn:" % len(thieu))
        for r in thieu:
            print("  ✗ " + r)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
