# Tóm tắt Chương 3

**Quan hệ nghĩa là bảng, không phải mối liên hệ.** Đây là cạm bẫy thuật ngữ lớn nhất của chương. Một bảng chỉ là quan hệ khi thỏa mãn **tám đặc trưng**, trong đó hai đặc trưng quan trọng nhất là *mỗi ô một giá trị đơn* và *thứ tự dòng cột không quan trọng*.

**Phụ thuộc hàm `A → B`** nghĩa là biết `A` thì biết chắc `B`; nó **có chiều** và là một **quy tắc nghiệp vụ**, không phải quan sát trên dữ liệu hiện có.

**Năm loại khóa** thu hẹp dần: siêu khóa *(duy nhất)* → khóa dự tuyển *(thêm tối thiểu)* → khóa chính *(được chọn)*. Ngoài ra có khóa phụ để tra cứu và khóa ngoại để liên kết.

**Hai ràng buộc toàn vẹn**: *thực thể* — khóa chính duy nhất và không rỗng; *tham chiếu* — khóa ngoại hoặc rỗng hoặc phải tồn tại. Khóa chính cấm rỗng vì rỗng nghĩa là không có danh tính; khóa ngoại được phép rỗng vì rỗng nghĩa là *chưa liên kết* — đó chính là cách cài đặt **tham gia tùy chọn** của Chương 2.

**Bốn quy tắc ánh xạ**: thực thể mạnh thành bảng; 1:1 đưa khóa sang một bên; **1:M đưa khóa ngoại sang phía "nhiều"**; M:N tạo bảng mới. Thực thể yếu thành bảng có khóa phức hợp; phân cấp cha/con có **ba phương án**, chọn theo hai ràng buộc rời nhau/chồng lấn và đầy đủ/không đầy đủ.

**Đại số quan hệ có tính đóng kín** — kết quả lại là quan hệ nên ghép nối được. Tám phép toán chia hai nhóm: **tập hợp** *(∪, ∩, −, ×)* và **quan hệ** *(σ, π, ⋈, ÷)*. Ba phép ∪, ∩, − đòi **khả hợp**; **tích Descartes thì không**, vì nó chỉ nối bộ chứ không so sánh bộ.

**Phép kết thực chất là ba bước**: tích Descartes, chọn, chiếu. **Kết ngoài** giữ lại cả những bộ không khớp, và nhờ đó **dò được khóa ngoại mồ côi**. **Phép chia** trả lời các câu hỏi có chữ *"tất cả"*, tính bằng kỹ thuật phủ định hai lần.

**Ví dụ ABC** cho ra **bảy bảng** với đầy đủ khóa chính và khóa ngoại — lần đầu tiên thiết kế trở thành thứ máy tính xử lý được.

---


## Tài liệu tham khảo của chương

**[1]** Tô Văn Nam (2005). *Giáo trình cơ sở dữ liệu*. NXB Giáo dục — chương về mô hình dữ liệu quan hệ và đại số quan hệ.

**[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê.

**[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning — **Chapter 3** (*The Relational Database Model*): cạm bẫy thuật ngữ *relation* (tr. 60), tám đặc trưng của bảng quan hệ (tr. 60), các loại khóa, hai ràng buộc toàn vẹn, đại số quan hệ và các phép toán, kỹ thuật dùng kết ngoài phát hiện lỗi toàn vẹn tham chiếu, ánh xạ ER sang quan hệ (tr. 113), mười hai quy tắc của Codd.

**Hướng dẫn tự học.** Nên đọc Chapter 3 của [3] song song với các mục 3.1–3.3. Phần đại số quan hệ *(mục 3.5–3.7)* cần **làm bài tập mới hiểu** — đọc suông không đủ; khuyến nghị làm hết Bài B2 trước khi sang Chương 4. Bài B1 *(ánh xạ lược đồ thư viện)* nên hoàn thành trước buổi học Chương 4, vì lược đồ thu được sẽ tiếp tục dùng để phát hiện ràng buộc toàn vẹn ở chương sau.

---


## Danh Mục Hình (Chương 3)

| Hình | Tên hình | Mục |
|---|---|---|
| Hình 3.1 | Từ điển phiên dịch — từ mô hình ER sang mô hình quan hệ | 3.1.4 |
| Hình 3.2 | Phụ thuộc hàm có chiều — như một mũi tên một chiều | 3.2.2 |
| Hình 3.3 | Ba loại khóa lồng nhau — thu hẹp dần từ siêu khóa tới khóa chính | 3.2.3 |
| Hình 3.4 | Khóa chính là "căn cước", khóa ngoại là "địa chỉ liên hệ" | 3.2.4 |
| Hình 3.5 | Bốn quy tắc ánh xạ và trường hợp thực thể yếu — từ mảnh lược đồ Chen sang bảng | 3.4.1 |
| Hình 3.6 | Làm sai để thấy vì sao — khóa ngoại đặt nhầm bên | 3.4.2 |
| Hình 3.7 | Ba phương án ánh xạ phân cấp cha/con | 3.4.5 |
| Hình 3.8 | Phép chọn cắt ngang, phép chiếu cắt dọc | 3.5.2 |
| Hình 3.9 | Cây biểu thức của Ví dụ 3.9 — tính từ lá lên ngọn | 3.5.3 |
| Hình 3.10 | Phép kết tự nhiên thực chất là ba bước | 3.7.1 |
| Hình 3.11 | Dùng kết ngoài trái để phát hiện khóa ngoại mồ côi | 3.7.3 |
| Hình 3.12 | Tám phép toán của đại số quan hệ | 3.7.5 |
| Hình 3.13 | Ánh xạ lược đồ Chen sang tập quan hệ | 3.8.1 |
| Hình 3.14 | Lược đồ quan hệ của Trung tâm Anh ngữ ABC — bảy bảng | 3.8.2 |


## Danh Mục Bảng (Chương 3)

| Bảng | Tên bảng | Mục |
|---|---|---|
| Bảng 3.1 | Hai thuật ngữ dễ lẫn — *quan hệ* và *liên kết* | 3.1.1 |
| Bảng 3.2 | Ba lớp thuật ngữ song song | 3.1.2 |
| Bảng 3.3 | Bậc, lực lượng và miền giá trị nhìn trên một bảng `HOCVIEN` thu nhỏ | 3.1.2 |
| Bảng 3.4 | Tám đặc trưng của một bảng quan hệ | 3.1.3 |
| Bảng 3.5 | Một bảng tính trông hợp lý nhưng không phải là quan hệ | 3.1.3 |
| Bảng 3.6 | Bảng tính và bảng quan hệ — hai cách nghĩ về "vị trí" | 3.1.3 |
| Bảng 3.7 | Phép thử hai dòng cho hai phụ thuộc hàm ngược chiều nhau | 3.2.2 |
| Bảng 3.8 | Năm loại khóa — minh họa trên bảng `HOCVIEN(MAHV, CCCD, HOTEN, NGAYSINH, MALOP)` | 3.2.3 |
| Bảng 3.9 | Dữ liệu `HOCVIEN` có hai cột cùng đủ tư cách khóa dự tuyển | 3.2.3 |
| Bảng 3.10 | Cùng một cột `MAGV`, hai vai trò ở hai bảng | 3.2.4 |
| Bảng 3.11 | Bốn lần thử chèn dữ liệu và phán quyết của hai ràng buộc toàn vẹn | 3.3.3 |
| Bảng 3.12 | Ba loại lỗi mà toàn vẹn thực thể và tham chiếu không phát hiện được | 3.3.4 |
| Bảng 3.13 | Bốn quy tắc ánh xạ ER sang quan hệ | 3.4.1 |
| Bảng 3.14 | Cùng một sự thật "cô Lê Hoa phụ trách bốn lớp", hai cách đặt khóa ngoại | 3.4.2 |
| Bảng 3.15 | Dữ liệu của hai liên kết đệ quy sau khi ánh xạ | 3.4.4 |
| Bảng 3.16 | Ba người, ba phương án — ô rỗng, dòng lặp và người "mất chỗ" hiện ra ở đâu | 3.4.5 |
| Bảng 3.17 | Chọn phương án theo hai ràng buộc của phân cấp | 3.4.5 |
| Bảng 3.18 | Kiểm tra khả hợp bằng cách xếp cột thẳng hàng | 3.6.1 |
| Bảng 3.19 | Bốn phép toán tập hợp tính trên hai bảng khả hợp `A` và `B` | 3.6.2 |
| Bảng 3.20 | Bốn phép toán tập hợp — đối chiếu | 3.6.3 |
| Bảng 3.21 | Tích Descartes `LOP × GIAOVIEN` — mọi cặp, kể cả cặp vô nghĩa | 3.6.3 |
| Bảng 3.22 | Các biến thể của phép kết | 3.7.2 |
| Bảng 3.23 | Kết trong và ba kết ngoài trên cùng một cặp bảng có bộ không khớp ở cả hai phía | 3.7.2 |
| Bảng 3.24 | `GHIDANH` xếp thành ma trận học viên × lớp — phép chia là "đủ ✓ ở các cột bắt buộc" | 3.7.4 |
| Bảng 3.25 | Bảng tra ký hiệu đại số quan hệ | 3.7.5 |
| Bảng 3.26 | Từ điển dịch yêu cầu bằng lời sang phép toán | 3.7.5 |
| Bảng 3.27 | Ánh xạ từng thành phần | 3.8.1 |
| Bảng 3.28 | Đối chiếu toàn vẹn cho bảy bảng | 3.8.3 |
| Bảng 3.29 | Sáu truy vấn trên lược đồ ABC | 3.8.4 |
| Bảng 3.30 | Bộ dữ liệu mẫu để tính tay sáu truy vấn | 3.8.4 |
| Bảng 3.31 | Kết quả sáu truy vấn trên bộ dữ liệu mẫu | 3.8.4 |
| Bảng 3.32 | Ba chương, ba mức độ trưởng thành của cùng một thiết kế | 3.8.5 |


## Danh Mục Từ Viết Tắt

| Viết tắt | Tiếng Anh | Tiếng Việt |
|---|---|---|
| **CSDL** | — | Cơ sở dữ liệu |
| **EER** | Extended Entity–Relationship | Mô hình thực thể – liên kết mở rộng |
| **ER** | Entity–Relationship | Mô hình thực thể – liên kết |
| **FK** | Foreign Key | Khóa ngoại |
| **PK** | Primary Key | Khóa chính |
| **QT1–QT4** | — | Bốn quy tắc ánh xạ ER sang quan hệ |
| **RBTV** | — | Ràng buộc toàn vẹn |
| **SQL** | Structured Query Language | Ngôn ngữ truy vấn có cấu trúc |
| **σ** | selection | Phép chọn |
| **π** | projection | Phép chiếu |
| **⋈** | join | Phép kết |
| **⟕** | left outer join | Phép kết ngoài trái |
| **÷** | division | Phép chia |
