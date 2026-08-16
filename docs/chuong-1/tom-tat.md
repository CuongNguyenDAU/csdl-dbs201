# Tóm tắt Chương 1

**Dữ liệu và thông tin không phải là một.** Dữ liệu là sự kiện thô; thông tin là kết quả xử lý dữ liệu trong một ngữ cảnh xác định. Vì ngữ cảnh mang tính quyết định, cơ sở dữ liệu buộc phải lưu kèm cả phần mô tả ngữ cảnh, gọi là **metadata**. Cơ sở dữ liệu quan hệ làm việc với **dữ liệu có cấu trúc**.

**Cần phân biệt ba khái niệm:** cơ sở dữ liệu là *dữ liệu*, hệ quản trị cơ sở dữ liệu là *phần mềm* quản lý dữ liệu ấy, còn hệ cơ sở dữ liệu là *toàn bộ hệ thống* gồm năm thành phần: con người, thủ tục, phần cứng, phần mềm và dữ liệu.

**Hệ thống tệp có bốn hạn chế:** dư thừa, không nhất quán, dị thường khi cập nhật và phụ thuộc dữ liệu. Bốn hạn chế này nối thành một chuỗi nhân quả có gốc là **dư thừa** và có ngọn là **quyết định sai** — với chi phí tăng dần theo từng mắt xích.

**Lược đồ là cấu trúc, thể hiện là dữ liệu tại một thời điểm.** Lược đồ gần như đứng yên, thể hiện thay đổi liên tục.

**Kiến trúc ba mức ANSI/SPARC** — ngoài, quan niệm, trong — tạo ra **tính độc lập dữ liệu**, cho phép thay đổi ở một mức mà không phải sửa mức cao hơn. Cần phân biệt kiến trúc này với **ba mức của mô hình dữ liệu** (quan niệm, logic, vật lý): một bên là ba tầng cùng tồn tại, một bên là ba chặng nối tiếp của quy trình thiết kế.

**Các lệnh cơ sở dữ liệu chia thành bốn nhóm** DDL, DML, DQL, DCL — trong đó DDL tác động lên metadata còn DML và DQL tác động lên dữ liệu. **Giao dịch** là đơn vị công việc không thể chia nhỏ, phải thỏa mãn bốn tính chất **ACID**.

**Ví dụ Trung tâm ABC** cho thấy một bảng phẳng sinh ra ba dị thường thêm, sửa, xóa, và việc tách thành ba bảng liên kết loại bỏ được cả ba — vì mỗi sự thật chỉ còn nằm ở đúng một chỗ.

**Nối sang Chương 2.** Chương này đã cho thấy *vấn đề*; điều còn thiếu là *phương pháp*. Việc tách bảng vừa rồi dựa trên trực giác, không có cơ sở để chứng minh và không mở rộng được cho hệ thống lớn. Chương 2 giới thiệu **mô hình thực thể – liên kết (ER)** — công cụ giúp người thiết kế phát hiện một cách có hệ thống rằng cần bao nhiêu bảng, mỗi bảng gồm những gì, và chúng liên hệ với nhau ra sao.

---


## Tài liệu tham khảo của chương

**[1]** Tô Văn Nam (2005). *Giáo trình cơ sở dữ liệu*. NXB Giáo dục — chương mở đầu.

**[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê.

**[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning — **Chapter 1** (*Database Systems*): các mục về dữ liệu và thông tin (tr. 5–7), khái niệm cơ sở dữ liệu và metadata (tr. 7–9), chức năng của hệ quản trị (tr. 12–15), phân loại hệ quản trị (tr. 15–19), các dạng dữ liệu (tr. 22–24), hạn chế của hệ thống tệp (tr. 26–33); **Chapter 2** (*Data Models*): các mức trừu tượng dữ liệu (tr. 46–49), các thế hệ mô hình dữ liệu.

**Hướng dẫn tự học.** Người học nên đọc trước Chapter 1 của [3] để có cái nhìn tổng quan, sau đó đọc chương mở đầu của [1] để đối chiếu thuật ngữ tiếng Việt. Phần mục 2.6 của [3] về các mức trừu tượng nên đọc **sau khi** đã học xong mục 1.5 của giáo trình này, vì nó dùng ngay các khái niệm ở đó.

---


## Danh Mục Hình (Chương 1)

| Hình | Tên hình | Mục |
|---|---|---|
| Hình 1.1 | Vai trò trung gian của hệ quản trị cơ sở dữ liệu | 1.2.1 |
| Hình 1.2 | Hệ thống tệp và cách tiếp cận cơ sở dữ liệu | 1.3.1 |
| Hình 1.3 | Trung tâm ABC trong mô hình phân cấp — Trần An buộc phải lưu hai lần | 1.4.2 |
| Hình 1.4 | Trung tâm ABC trong mô hình mạng — Trần An chỉ còn một bản | 1.4.2 |
| Hình 1.5 | Một lược đồ — nhiều thể hiện theo thời gian | 1.4.4 |
| Hình 1.6 | Kiến trúc ba mức ANSI/SPARC và hai loại độc lập dữ liệu | 1.5.1 |
| Hình 1.7 | Năm thành phần của một hệ cơ sở dữ liệu | 1.6.4 |
| Hình 1.8 | Từ một bảng phẳng thành ba bảng liên kết | 1.7 |


## Danh Mục Bảng (Chương 1)

| Bảng | Tên bảng | Mục |
|---|---|---|
| Bảng 1.1 | Bốn tầng của tháp DIKW, minh họa tại Trung tâm Anh ngữ ABC | 1.1.2 |
| Bảng 1.2 | Ba dạng dữ liệu | 1.1.3 |
| Bảng 1.3 | Metadata của bảng `SINHVIEN` | 1.1.4 |
| Bảng 1.4 | Ba cách phân loại hệ quản trị cơ sở dữ liệu | 1.2.3 |
| Bảng 1.5 | Tệp phẳng `HOCVIEN_LOP` của Trung tâm Anh ngữ ABC | 1.3.2 |
| Bảng 1.6 | So sánh hệ thống tệp và cách tiếp cận cơ sở dữ liệu | 1.3.4 |
| Bảng 1.7 | Các thế hệ mô hình dữ liệu | 1.4.2 |
| Bảng 1.8 | Hai bộ "ba mức" — không được lẫn lộn | 1.5.2 |
| Bảng 1.9 | Bốn nhóm ngôn ngữ cơ sở dữ liệu | 1.6.1 |
| Bảng 1.10 | Bốn tính chất ACID của giao dịch | 1.6.2 |
| Bảng 1.11 | Ba dị thường trên bảng phẳng và cách thiết kế mới khắc phục | 1.7 |
| Bảng 1.12 | Cùng dữ liệu ấy sau khi tách thành ba bảng | 1.7 |


## Danh Mục Từ Viết Tắt

| Viết tắt | Tiếng Anh | Tiếng Việt |
|---|---|---|
| **ACID** | Atomicity, Consistency, Isolation, Durability | Nguyên tố, nhất quán, cô lập, bền vững |
| **ANSI/SPARC** | American National Standards Institute / Standards Planning and Requirements Committee | Ủy ban đề xuất kiến trúc ba mức |
| **CSDL** | — | Cơ sở dữ liệu |
| **DBMS** | Database Management System | Hệ quản trị cơ sở dữ liệu |
| **DCL** | Data Control Language | Ngôn ngữ kiểm soát dữ liệu |
| **DDL** | Data Definition Language | Ngôn ngữ định nghĩa dữ liệu |
| **DIKW** | Data, Information, Knowledge, Wisdom | Dữ liệu, thông tin, tri thức, minh triết |
| **DML** | Data Manipulation Language | Ngôn ngữ thao tác dữ liệu |
| **DQL** | Data Query Language | Ngôn ngữ truy vấn dữ liệu |
| **ERD** | Entity–Relationship Diagram | Sơ đồ thực thể – liên kết |
| **OLTP** | Online Transaction Processing | Xử lý giao dịch trực tuyến |
| **RBTV** | — | Ràng buộc toàn vẹn |
| **SQL** | Structured Query Language | Ngôn ngữ truy vấn có cấu trúc |
