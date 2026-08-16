# Tóm tắt Chương 5

**Một cơ sở dữ liệu "tốt"** được định nghĩa bằng **bốn tiêu chí đo được**: không dư thừa, không dị thường, bảo toàn thông tin, bảo toàn phụ thuộc hàm. Bốn tiêu chí này **không phải lúc nào cũng đạt được cùng lúc**.

**Ba loại phụ thuộc hàm**: đầy đủ *(vô hại)*, **bộ phận** *(vi phạm 2NF)*, **bắc cầu** *(vi phạm 3NF)*. Hai loại sau là **hai thủ phạm** gây dị thường. Tập `F` đến từ **quy tắc nghiệp vụ**, không phải từ dữ liệu mẫu.

**Hệ luật Armstrong** gồm ba luật gốc *(phản xạ, tăng trưởng, bắc cầu)* và ba luật dẫn xuất *(hợp, tách, bắc cầu giả)*. Nó **đúng đắn và đầy đủ**.

**Bao đóng `X⁺`** là công cụ trung tâm, tính bằng thuật toán lăn quả cầu tuyết. Hai công dụng: kiểm tra một phụ thuộc có suy ra được không, và kiểm tra một tập có phải siêu khóa không. **`F⁺` là tập các mũi tên; `X⁺` là tập các chữ cái.**

**Thuật toán tìm khóa** chia thuộc tính thành `TN` *(bắt buộc trong khóa)*, `TG` *(phải thử)*, `TĐ` *(không bao giờ trong khóa)*. Tìm **tất cả** khóa bằng cách duyệt `2^|TG|` tập con, với **mẹo rút gọn**: đã là siêu khóa thì mọi tập cha đều không tối thiểu, loại luôn.

**Phủ tối thiểu** thỏa mãn ba điều kiện: vế phải một thuộc tính, không thừa thuộc tính vế trái, không thừa phụ thuộc. **Thứ tự ba bước là bắt buộc.**

**Ba dạng chuẩn**: 1NF *(ô đơn trị)*, 2NF *(không bộ phận)*, 3NF *(không bắc cầu)* — tóm tắt bằng câu *"the key, the whole key, and nothing but the key"*.

**Phép tách sai sinh ra bộ giả** — những dòng chưa từng tồn tại. Điều này **nguy hiểm hơn mất dữ liệu**, vì hệ thống trả về nhiều hơn sự thật mà mọi dòng đều trông hợp lệ. Điều kiện tránh: **thuộc tính chung phải là siêu khóa của ít nhất một bảng con**. Quy tắc thực hành: **luôn tách theo phụ thuộc hàm**.

**Định lý quan trọng**: 3NF luôn đạt được cả bảo toàn thông tin lẫn bảo toàn phụ thuộc; **BCNF thì không phải lúc nào cũng**. Vì vậy **3NF thường là đích đến hợp lý** — "chuẩn hơn" không đồng nghĩa với "tốt hơn".

**BCNF** chặt hơn 3NF ở chỗ bỏ vế *"hoặc `A` là thuộc tính khóa"*. **Phụ thuộc đa trị `X ↠ Y`** gây bùng nổ tích ngay cả khi bảng đã đạt BCNF; **4NF** loại bỏ nó, và **phép tách theo phụ thuộc đa trị luôn bảo toàn thông tin** *(định lý Fagin)*.

**Phi chuẩn hóa** là cố ý đưa dư thừa trở lại để đổi lấy tốc độ — chỉ hợp lý với hệ thống đọc nhiều sửa ít, và **chỉ được làm sau khi đã chuẩn hóa**, có ghi lại lý do.

**Kết quả cuối cùng**: chuẩn hóa bằng toán học cho ra **đúng bốn bảng** mà trực giác ở Chương 1 và bản vẽ ở Chương 2–3 đã đoán được. Trực giác **đoán đúng**, bản vẽ **làm rõ**, toán học **chứng minh**.

---


## Tài liệu tham khảo của chương

**[1]** Tô Văn Nam (2005). *Giáo trình cơ sở dữ liệu*. NXB Giáo dục — chương về lý thuyết thiết kế cơ sở dữ liệu quan hệ; phụ thuộc hàm, bao đóng, thuật toán tìm khóa, các dạng chuẩn.

**[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê — hệ luật dẫn Armstrong, phủ tối thiểu, phép tách lược đồ và các thuật toán.

**[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning — **Chapter 6** (*Normalization of Database Tables*): quy trình chuẩn hóa 1NF–3NF, BCNF, 4NF, phụ thuộc đa trị, phi chuẩn hóa và các điều kiện áp dụng, danh mục kiểm tra mô hình hóa dữ liệu.

**Hướng dẫn tự học.** Chương này **chỉ nắm được qua luyện tập** — đọc suông không đủ. Trình tự khuyến nghị: làm hết Bài A1 *(bao đóng)* trước khi đọc mục 5.5; làm Bài B1 *(tìm tất cả khóa)* trước khi đọc mục 5.7; làm Bài B3 *(chuẩn hóa hiệu sách)* sau khi đọc xong mục 5.9. Hai tiểu mục **5.10.2–5.10.3** *(phụ thuộc đa trị và 4NF)* được viết đủ chi tiết để tự đọc nếu lớp không kịp giảng; kèm Bài C2 để tự kiểm tra.

---


## Danh Mục Hình (Chương 5)

| Hình | Tên hình | Mục |
|---|---|---|
| Hình 5.1 | Bốn chương hội tụ về Chương 5 | 5.1.1 |
| Hình 5.2 | Phụ thuộc bộ phận — phép loại suy ổ khóa hai chìa | 5.2.3 |
| Hình 5.3 | Phụ thuộc bắc cầu — phải đi hai chặng | 5.2.4 |
| Hình 5.4 | Bao đóng — phép loại suy quả cầu tuyết | 5.4.1 |
| Hình 5.5 | Ba nhóm thuộc tính — và vì sao phân nhóm | 5.5.1 |
| Hình 5.6 | Thuật toán tìm phủ tối thiểu — phải làm đúng thứ tự | 5.6.3 |
| Hình 5.7 | Cây quyết định — xác định dạng chuẩn cao nhất | 5.7.5 |
| Hình 5.8 | Nghịch lý bộ giả — không mất dòng nào mà vẫn mất sự thật | 5.8.1 |
| Hình 5.9 | Leo cao hơn chưa chắc tốt hơn | 5.8.4 |
| Hình 5.10 | Quy trình chuẩn hóa từng bước | 5.9.5 |
| Hình 5.11 | Phụ thuộc đa trị — hai nhánh độc lập gây bùng nổ tích | 5.10.2 |
| Hình 5.12 | Trực giác, bản vẽ, toán học — cùng ra một kết quả | 5.11.1 |
| Hình 5.13 | Hành trình năm chương | 5.11.4 |


## Danh Mục Bảng (Chương 5)

| Bảng | Tên bảng | Mục |
|---|---|---|
| Bảng 5.1 | Bốn chương — căn cứ ra quyết định | 5.1.1 |
| Bảng 5.2 | Bốn tiêu chí — công cụ kiểm tra tương ứng | 5.1.2 |
| Bảng 5.3 | Ba loại phụ thuộc hàm | 5.2.1 |
| Bảng 5.4 | Ba luật gốc và ba luật dẫn xuất | 5.3.2 |
| Bảng 5.5 | `F⁺` và `X⁺` — hai thứ khác nhau | 5.4.4 |
| Bảng 5.6 | Dạng chuẩn diệt dị thường nào | 5.7.6 |
| Bảng 5.7 | Tập phụ thuộc hàm `F` — rút từ quy tắc nghiệp vụ | 5.9.2 |
| Bảng 5.8 | Chẩn đoán với khóa `K = (MAHV, MALOP)` | 5.9.4 |
| Bảng 5.9 | Kiểm chứng từng phép tách | 5.9.6 |
| Bảng 5.10 | 3NF và BCNF khác nhau ở đâu | 5.10.1 |
| Bảng 5.11 | Khi nào phi chuẩn hóa là hợp lý | 5.10.4 |
| Bảng 5.12 | Ba dị thường trên lược đồ 3NF | 5.11.2 |
| Bảng 5.13 | Mọi lời hẹn và nơi trả | 5.11.3 |


## Danh Mục Từ Viết Tắt

| Viết tắt | Tiếng Anh | Tiếng Việt |
|---|---|---|
| **1NF · 2NF · 3NF** | First / Second / Third Normal Form | Dạng chuẩn 1 · 2 · 3 |
| **4NF · 5NF** | Fourth / Fifth Normal Form | Dạng chuẩn 4 · 5 |
| **BCNF** | Boyce–Codd Normal Form | Dạng chuẩn Boyce–Codd |
| **CSDL** | — | Cơ sở dữ liệu |
| **F** | set of functional dependencies | Tập phụ thuộc hàm |
| **F⁺** | closure of F | Bao đóng của tập phụ thuộc hàm |
| **PTH** | functional dependency | Phụ thuộc hàm |
| **RBTV** | — | Ràng buộc toàn vẹn |
| **TN · TG · TĐ** | — | Tập nguồn · tập trung gian · tập đích |
| **X⁺** | closure of attribute set X | Bao đóng của tập thuộc tính `X` |
| **→** | functional dependency | Phụ thuộc hàm |
| **↠** | multivalued dependency | Phụ thuộc đa trị |
| **⋈** | natural join | Phép kết tự nhiên |
