# Tóm tắt Chương 2

**Thiết kế cơ sở dữ liệu đi qua ba mức** quan niệm, logic, vật lý; Chương 2 làm việc ở mức quan niệm. Nguyên liệu đầu vào là **quy tắc nghiệp vụ** — phải rõ ràng và **đếm được**, nêu cả hai chiều của mỗi mối liên hệ.

**Thực thể là loại sự vật, thể hiện thực thể là cá thể cụ thể** — cặp khái niệm song song với lược đồ và thể hiện ở Chương 1. Thuộc tính phân loại theo bốn cặp tiêu chí; trong đó **thuộc tính đa trị bắt buộc phải tách** thành thực thể riêng, và **thuộc tính dẫn xuất thường không nên lưu**.

**Thuộc tính khóa phải thỏa mãn đồng thời tính duy nhất và tính tối thiểu.** Nên ưu tiên **khóa thay thế** làm khóa chính vì tính ổn định, đồng thời vẫn khai báo khóa tự nhiên như một ràng buộc duy nhất.

**Kỹ thuật hỏi hai chiều** loại bỏ gần hết khả năng nhầm loại liên kết: luôn hỏi cả *"một A liên quan bao nhiêu B"* lẫn chiều ngược lại. **Tính tham gia có thể khác nhau ở hai chiều** của cùng một liên kết.

**Ba trường hợp đặc biệt phải xử lý ở Bước 4:** thuộc tính đa trị, liên kết M:N *(tách thành thực thể kết hợp)*, và liên kết đệ quy. **Thực thể yếu** phải thỏa mãn đồng thời phụ thuộc tồn tại và khóa không đầy đủ.

**Mô hình EER** bổ sung quan hệ **cha–con** để xử lý tình huống nhiều loại sự vật vừa giống vừa khác nhau. Thực thể con **kế thừa** mọi thuộc tính và liên kết của cha, và dùng chung thuộc tính khóa với cha. Mỗi phân cấp phải xác định **hai ràng buộc**: rời nhau hay chồng lấn, đầy đủ hay không đầy đủ. Phép thử để nhận biết quan hệ cha–con là câu **"LÀ MỘT"**.

**Quy trình năm bước** — thực thể, thuộc tính và khóa, liên kết, ca đặc biệt, vẽ và kiểm tra — là một quá trình **lặp**, không phải một chiều.

**Ví dụ Trung tâm ABC** cho ra **bảy thực thể**, so với ba bảng mà trực giác ở Chương 1 tìm được. Bốn thực thể chênh lệch cho thấy thiết kế cơ sở dữ liệu là **mô hình hóa nghiệp vụ**, không phải dọn dẹp dữ liệu có sẵn.

**Nối sang Chương 3.** Lược đồ ER vừa xây dựng là một sơ đồ dành cho **con người đọc** — nó chưa phải là thứ máy tính hiểu được. Chương 3 giới thiệu **mô hình quan hệ**, cho ta cấu trúc toán học chặt chẽ để biểu diễn dữ liệu, cùng **quy tắc ánh xạ** từ lược đồ ER sang tập các quan hệ. Khi ấy bảy thực thể trong Hình 2.17 sẽ trở thành bảy bảng cụ thể, có khóa chính và khóa ngoại rõ ràng.

---


## Tài liệu tham khảo của chương

**[1]** Tô Văn Nam (2005). *Giáo trình cơ sở dữ liệu*. NXB Giáo dục — chương về mô hình thực thể – liên kết.

**[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê.

**[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning — **Chapter 4** (*Entity Relationship Modeling*): quy tắc nghiệp vụ (tr. 148–150), các thành phần của mô hình ER, kết nối và lực lượng, thực thể yếu, thực thể kết hợp, quy trình thiết kế và các bẫy thiết kế; **Chapter 5** (*Advanced Data Modeling*): mô hình EER, thực thể cha–con, chuyên biệt hóa và tổng quát hóa, các ràng buộc rời nhau/chồng lấn và đầy đủ/không đầy đủ, khóa tự nhiên và khóa thay thế.

**Hướng dẫn tự học.** Nên đọc Chapter 4 của [3] song song với các mục 2.1–2.6 của giáo trình này. Chapter 5 chỉ nên đọc **sau khi** đã nắm chắc mục 2.7, vì nó dùng ngay các khái niệm cha–con và ràng buộc phân cấp. Bài tập B1 *(thư viện)* nên làm trước khi đọc Chương 3, vì lược đồ thu được sẽ tiếp tục dùng làm bài tập ánh xạ ở chương sau.

---


## Danh Mục Hình (Chương 2)

| Hình | Tên hình | Mục |
|---|---|---|
| Hình 2.1 | Một lược đồ ER nhỏ — ba thành phần cơ bản | 2.1.4 |
| Hình 2.2 | Bộ ký hiệu Chen — tổng quan | 2.2.2 |
| Hình 2.3 | Thuộc tính của thực thể `HOCVIEN` — ký pháp Chen và ký pháp Crow's Foot | 2.2.3 |
| Hình 2.4 | Ba cách xử lý thuộc tính đa trị — chỉ một cách đúng | 2.2.4 |
| Hình 2.5 | Kỹ thuật hỏi hai chiều — quy trình xác định loại liên kết | 2.4.2 |
| Hình 2.6 | Ký pháp Chen — ba loại kết nối, minh họa tại Trung tâm ABC | 2.5.1 |
| Hình 2.7 | Bốn ký hiệu đầu mút của ký pháp Crow's Foot | 2.5.3 |
| Hình 2.8 | Ba ví dụ liên kết đệ quy, vẽ theo ký pháp Chen | 2.6.2 |
| Hình 2.9 | Thực thể yếu trong ký pháp Chen — trường hợp `DIENTHOAI` | 2.6.3 |
| Hình 2.10 | Liên kết M:N ẩn chứa một thực thể | 2.6.4 |
| Hình 2.11 | Phân cấp chuyên biệt hóa tại Trung tâm ABC | 2.7.2 |
| Hình 2.12 | Quy trình năm bước xây dựng lược đồ ER | 2.8.1 |
| Hình 2.13 | Cùng một liên kết vẽ bằng hai ký pháp | 2.8.3 |
| Hình 2.14 | Bước 1–2 — bốn thực thể với thuộc tính, ký pháp Chen | 2.9.2 |
| Hình 2.15 | Bước 3 — thêm liên kết và lực lượng, ký pháp Chen | 2.9.3 |
| Hình 2.16 | Lược đồ ER hoàn chỉnh của Trung tâm Anh ngữ ABC — ký pháp Chen | 2.9.5 |
| Hình 2.17 | Lược đồ ER của Trung tâm Anh ngữ ABC — ký pháp Crow's Foot | 2.9.5 |


## Danh Mục Bảng (Chương 2)

| Bảng | Tên bảng | Mục |
|---|---|---|
| Bảng 2.1 | Phiên dịch quy tắc nghiệp vụ sang thành phần ER | 2.1.5 |
| Bảng 2.2 | Bộ ký hiệu của ký pháp Chen | 2.2.2 |
| Bảng 2.3 | Bốn cặp phân loại thuộc tính | 2.2.3 |
| Bảng 2.4 | Kiểm chứng cách 3 bằng bốn câu hỏi khó | 2.2.4 |
| Bảng 2.5 | Hai tiêu chí bắt buộc của một thuộc tính khóa | 2.3.1 |
| Bảng 2.6 | So sánh khóa tự nhiên và khóa thay thế | 2.3.2 |
| Bảng 2.7 | Bảng hỏi hai chiều cho Trung tâm ABC | 2.4.3 |
| Bảng 2.8 | Ký hiệu đầu mút Crow's Foot — gộp kết nối và tham gia | 2.5.3 |
| Bảng 2.9 | Cùng một sự vật, hai cách đặt thuộc tính khóa cho hai kết luận khác nhau | 2.6.3 |
| Bảng 2.10 | Bốn tổ hợp ràng buộc và ví dụ tại Trung tâm ABC | 2.7.5 |
| Bảng 2.11 | Đối chiếu mô hình ER và sơ đồ lớp UML | 2.8.4 |
| Bảng 2.12 | Nhận diện bẫy thiết kế ngay khi đọc đề | 2.9.1 |
| Bảng 2.13 | Bảy thực thể của lược đồ cuối cùng | 2.9.5 |
| Bảng 2.14 | Cùng một cặp thực thể, hai quy tắc nghiệp vụ khác nhau cho hai lược đồ khác nhau | 2.9.6 |


## Danh Mục Từ Viết Tắt

| Viết tắt | Tiếng Anh | Tiếng Việt |
|---|---|---|
| **1:1** | one-to-one | Liên kết một–một |
| **1:M** | one-to-many | Liên kết một–nhiều |
| **M:N** | many-to-many | Liên kết nhiều–nhiều |
| **CSDL** | — | Cơ sở dữ liệu |
| **EER** | Extended Entity–Relationship | Mô hình thực thể – liên kết mở rộng |
| **ER** | Entity–Relationship | Mô hình thực thể – liên kết |
| **ERD** | Entity–Relationship Diagram | Sơ đồ thực thể – liên kết |
| **FK** | Foreign Key | Khóa ngoại |
| **PK** | Primary Key | Khóa chính |
| **UML** | Unified Modeling Language | Ngôn ngữ mô hình hóa thống nhất |
