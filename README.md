# Học liệu học phần Cơ sở dữ liệu (DBS201)

Website học liệu của học phần Cơ sở dữ liệu — Khoa Công nghệ Thông tin, Trường Đại
học Kiến trúc Đà Nẵng. Sinh viên đọc tại **<https://cuongnguyendau.github.io/csdl-dbs201/>**.

Site gồm năm chương bài giảng và phần củng cố kiến thức mỗi chương: hộp tự kiểm tra
cuối các mục (đáp án gập ngay bên dưới), trắc nghiệm tự chấm có giải thích, thẻ lật
khái niệm, bảng tự đánh giá theo chuẩn đầu ra.

## Cách sửa nội dung

Nguồn thật nằm ở `noi-dung/`, **không sửa trực tiếp trong `docs/`** — thư mục đó do
script sinh ra và sẽ bị ghi đè.

| Muốn sửa gì | Sửa ở đâu |
|---|---|
| Nội dung bài giảng | `noi-dung/Bai-giang_Chuong-N_*.md` |
| Ảnh minh họa trong bài | chép từ thư mục soạn thảo bằng `tools/chep_anh.py` (xem dưới) |
| Câu trắc nghiệm, thẻ lật, bảng tự đánh giá | `docs/quiz/chuong-N.json` |
| Lời giải bài tập | `loi-giai/chuong-N.md` |
| Trang chủ, tài liệu tham khảo | `docs/index.md`, `docs/tai-lieu.md` |
| Giao diện | `docs/assets/hoclieu.css`, `docs/assets/hoclieu.js` |
| Mục lục trái | `mkdocs.yml`, mục `nav` |

Sau khi sửa nội dung bài giảng hoặc lời giải, chạy lại script sinh trang:

```bash
python tools/build_docs.py        # cả 5 chương
python tools/build_docs.py 2      # chỉ chương 2
```

Bài giảng có thêm ảnh mới thì chép ảnh vào trước khi build. Script chỉ lấy những ảnh
mà `noi-dung/*.md` thật sự tham chiếu, nén JPEG về cỡ web (tối đa 1400 px, ~100–300
KB) rồi đặt vào `docs/hinh-ve/` đúng đường dẫn tương đối:

```bash
python tools/chep_anh.py                          # nguồn mặc định: ../BAI-GIANG-MOI/hinh-ve
python tools/chep_anh.py "D:/duong/dan/hinh-ve"   # nguồn khác
```

## Chạy thử trên máy

```bash
pip install -r requirements.txt
python tools/build_docs.py
python -m mkdocs serve             # mở http://127.0.0.1:8000
```

## Kiểm tra trước khi đẩy lên

```bash
python tools/check_site.py         # soát ngân hàng câu hỏi
python -m mkdocs build --strict    # bắt liên kết và neo hỏng
node tools/smoke.mjs               # bấm thật trong Chrome headless
```

`smoke.mjs` kiểm những thứ mà build không thấy: sơ đồ có render thật không, trắc
nghiệm chấm đúng chưa, tiến độ có được nhớ không, và các khối tương tác có gắn lại
được sau khi chuyển trang hay không.

## Xuất bản

Đẩy lên nhánh `main` là GitHub Actions tự build và xuất bản. Lần đầu cần vào
**Settings → Pages → Source = GitHub Actions**.

## Vài quyết định kỹ thuật đáng biết

- **Sơ đồ dùng mermaid, tải từ chính site.** Material mặc định tải mermaid từ
  `unpkg.com`; mạng trường chặn CDN là mất sạch 58 sơ đồ. Bản tự chứa nằm ở
  `docs/assets/mermaid.min.js`, và `overrides/main.html` chỉ nạp nó ở trang có sơ đồ.
- **Không đặt khối ```mermaid trong khối gập `???`.** Material dựng sơ đồ vào shadow
  DOM ngay khi trang tải, lúc đó khối gập còn đóng nên chiều rộng bằng 0 và sơ đồ ra
  méo. Lược đồ trong lời giải viết bằng ký hiệu văn bản.
- **Không bật `pymdownx.smartsymbols`.** Bài tập đánh nhãn `(a) (b) (c)` và tiện ích
  ấy sẽ lặng lẽ đổi `(c)` thành `©`.
- **Mọi JS tự viết phải đi qua `document$` của Material.** Theme bật
  `navigation.instant` nên chuyển trang không bắn `DOMContentLoaded`; dùng sự kiện
  thường thì trắc nghiệm chỉ hiện khi tải lại trang.
- **Phụ lục "Gợi ý tổ chức dạy học" không lên site.** Script loại bỏ khi sinh trang,
  vì phần đó bài giảng ghi rõ là dành cho giảng viên.
- **Đáp án tự kiểm tra đi theo từng hộp.** Bản in gom mục "Đáp án tự kiểm tra" ở cuối
  chương; script tách từng đáp án và chèn thành khối gập ngay dưới hộp "Tự kiểm tra"
  tương ứng, để sinh viên tự làm rồi mở.
- **Hai khối `>` cách nhau một dòng trống là hai khối riêng** (đúng CommonMark). Trong
  khối, dòng trống giữa các đoạn phải viết `>`; script không nối hai khối qua dòng
  trống trần — nếu nối thì "Chú ý" rồi tới "Tự kiểm tra" sẽ bị gộp làm một.
- **Nút mermaid nền đậm cần chữ trắng.** Material ép `.nodeLabel p` về màu chữ mặc định,
  đè lên `color:#fff` trong nguồn; `overrides/main.html` bọc `mermaid.initialize` để
  nối thêm một luật vào `themeCSS` vì SVG nằm trong shadow DOM đóng.

## Bản quyền

Nội dung bài giảng và hình vẽ do giảng viên biên soạn. Ảnh minh họa thực tế trong
`docs/hinh-ve/slide/internet/` lấy từ Wikimedia Commons (CC BY / CC BY-SA / CC0 / PD),
tác giả và giấy phép ghi ngay dưới mỗi ảnh trong bài. Sách của nhà xuất bản
**không** được đưa vào repo này — xem danh mục tham khảo trong `docs/tai-lieu.md`.
`.gitignore` và một bước trong workflow cùng chặn `*.pdf`, `*.pptx`, `*.docx`.
