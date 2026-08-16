# Tóm tắt Chương 4

**Ràng buộc toàn vẹn** là điều kiện dữ liệu phải **luôn luôn** thỏa mãn. Nó chứa phần quy tắc nghiệp vụ mà mô hình ER và cấu trúc bảng chưa diễn đạt được. Hai ràng buộc của Chương 3 chỉ là **hai trường hợp riêng** trong bộ sáu loại.

**Ràng buộc phải đặt ở tầng cơ sở dữ liệu**, vì một cơ sở dữ liệu có **nhiều cửa vào** mà ứng dụng chỉ khóa được một. Tầng ứng dụng cải thiện trải nghiệm; tầng cơ sở dữ liệu bảo đảm đúng đắn. **Dữ liệu sống lâu hơn ứng dụng.**

**Ba yếu tố** mô tả đầy đủ một ràng buộc: điều kiện *(viết bằng ký hiệu logic)*, bối cảnh *(quyết định loại)*, và bảng tầm ảnh hưởng.

**Bảng tầm ảnh hưởng** trả lời câu hỏi *đặt chốt kiểm tra ở đâu*, lập bằng **một câu hỏi duy nhất**: *"thao tác này có thể biến điều kiện từ đúng thành sai không?"*. Với ràng buộc khóa ngoại, kết quả luôn là **"thêm ở con, xóa ở cha"**. Lỗi phổ biến nhất là đánh dấu `+` cho tất cả các ô.

**Ba hành động khi vi phạm** — từ chối, lan truyền, gán rỗng — do **nghiệp vụ quyết định**. Chỉ dùng lan truyền khi bản ghi con thật sự vô nghĩa nếu thiếu cha.

**Bốn cơ chế khai báo** `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY` xử lý được bốn loại ràng buộc đầu. Hai loại liên quan hệ khó nhất phải dùng **trigger** — mạnh nhưng chạy ngầm, dễ gọi dây chuyền và làm chậm hệ thống, nên chỉ dùng khi khai báo không đủ.

**Sáu loại ràng buộc** phân theo bối cảnh và phạm vi. Phép thử phân biệt liên thuộc tính với liên bộ là **"che các dòng khác đi, còn kiểm tra được không"**.

**Cờ đỏ thiết kế:** một ràng buộc quá khó thực thi thường **tố cáo thiết kế** chứ không phải công cụ. Ràng buộc R6 với 5/6 ô `+` dẫn tới chẩn đoán `SISO` là **thuộc tính dẫn xuất tạo hai nguồn sự thật**; bỏ nó đi thì ràng buộc tự biến mất.

**Nối sang Chương 5.** Sau bốn chương, thiết kế đã tốt lên nhiều nhưng **mọi quyết định vẫn dựa trên cảm tính**. Chương 5 cung cấp công cụ để **chứng minh**.

---


## Tài liệu tham khảo của chương

**[1]** Tô Văn Nam (2005). *Giáo trình cơ sở dữ liệu*. NXB Giáo dục — chương về ràng buộc toàn vẹn; khung *điều kiện – bối cảnh – bảng tầm ảnh hưởng*.

**[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê — phần toàn vẹn dữ liệu và phân loại ràng buộc.

**[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning — **Chapter 3** (*The Relational Database Model*): toàn vẹn thực thể và toàn vẹn tham chiếu, các cơ chế khai báo `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY … ON DELETE`, các hành động xử lý khi vi phạm.

**Hướng dẫn tự học.** Nên đọc phần ràng buộc toàn vẹn của [1] và [2] song song với các mục 4.5–4.6. Kỹ năng **lập bảng tầm ảnh hưởng** *(mục 4.3)* chỉ thành thạo qua luyện tập — khuyến nghị làm hết Bài B2 trước khi sang Chương 5. Bài B1 *(phát hiện ràng buộc trên lược đồ thư viện)* nên hoàn thành và giữ lại, vì lược đồ ấy sẽ tiếp tục được chuẩn hóa ở Chương 5.

---


## Danh Mục Hình (Chương 4)

| Hình | Tên hình | Mục |
|---|---|---|
| Hình 4.1 | Hai ràng buộc của Chương 3 chỉ là trường hợp riêng | 4.1.3 |
| Hình 4.2 | Năm cửa vào cơ sở dữ liệu — ứng dụng chỉ khóa được một | 4.1.4 |
| Hình 4.3 | Ba yếu tố của một ràng buộc toàn vẹn | 4.2.1 |
| Hình 4.4 | Quy tắc vàng — một câu hỏi cho mọi ô | 4.3.2 |
| Hình 4.5 | Câu thần chú cho mọi ràng buộc khóa ngoại | 4.3.4 |
| Hình 4.6 | Cùng thao tác "xóa giáo viên" — ba lựa chọn, ba hệ quả | 4.4.2 |
| Hình 4.7 | Phép thử "che các dòng khác đi" | 4.5.4 |
| Hình 4.8 | Trigger hoạt động thế nào | 4.6.4 |
| Hình 4.9 | Ba lỗ hổng của Chương 3 và ràng buộc bịt chúng | 4.7.4 |
| Hình 4.10 | Chẩn đoán và đơn thuốc cho R6 | 4.7.5 |


## Danh Mục Bảng (Chương 4)

| Bảng | Tên bảng | Mục |
|---|---|---|
| Bảng 4.1 | Ba lỗ hổng của một cơ sở dữ liệu "hoàn hảo" | 4.1.1 |
| Bảng 4.2 | Ba tầng có thể đặt ràng buộc | 4.1.4 |
| Bảng 4.3 | Sáu loại ràng buộc toàn vẹn | 4.2.4 |
| Bảng 4.4 | Suy luận từng ô — ràng buộc khóa ngoại | 4.3.3 |
| Bảng 4.5 | Ba hành động khi phát hiện vi phạm | 4.4.1 |
| Bảng 4.6 | Bốn cơ chế khai báo ràng buộc | 4.4.3 |
| Bảng 4.7 | Hai cách đối phó với lỗi toàn vẹn tham chiếu | 4.4.4 |
| Bảng 4.8 | Sáu câu hỏi phát hiện ràng buộc | 4.7.2 |
| Bảng 4.9 | Sáu ràng buộc toàn vẹn của Trung tâm ABC | 4.7.3 |
| Bảng 4.10 | Bảng tầm ảnh hưởng của R6 | 4.7.5 |
| Bảng 4.11 | So sánh mức độ khó của hai ràng buộc | 4.7.5 |
| Bảng 4.12 | Cùng thao tác "xóa", ba khóa ngoại, ba hành động khác nhau | 4.8.1 |
| Bảng 4.13 | Bốn chương — và một điểm chung đáng lo | 4.8.3 |


## Danh Mục Từ Viết Tắt

| Viết tắt | Tiếng Anh | Tiếng Việt |
|---|---|---|
| **CSDL** | — | Cơ sở dữ liệu |
| **DBMS** | Database Management System | Hệ quản trị cơ sở dữ liệu |
| **FK** | Foreign Key | Khóa ngoại |
| **PK** | Primary Key | Khóa chính |
| **QH** | — | Quan hệ |
| **RBTV** | — | Ràng buộc toàn vẹn |
| **SQL** | Structured Query Language | Ngôn ngữ truy vấn có cấu trúc |
| **∀** | for all | Với mọi |
| **∃** | there exists | Tồn tại |
| **⇒** | implies | Kéo theo, thì |
