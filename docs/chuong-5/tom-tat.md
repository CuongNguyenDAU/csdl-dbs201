# Tóm tắt Chương 5

**Một cơ sở dữ liệu "tốt"** được định nghĩa bằng **bốn tiêu chí đo được**: không dư thừa, không dị thường, bảo toàn thông tin, bảo toàn phụ thuộc hàm. Ở mức **3NF**, ta luôn đạt được trọn vẹn cả bốn tiêu chí; khi đòi hỏi lên tới **BCNF**, đôi khi phải đánh đổi giữa tiêu chí 1 và tiêu chí 4.

**Ba loại phụ thuộc hàm**: đầy đủ *(vô hại)*, **bộ phận** *(vi phạm 2NF)*, **bắc cầu** *(vi phạm 3NF)*. Hai loại sau là **hai thủ phạm** gây dị thường. Tập `F` đến từ **quy tắc nghiệp vụ**, không phải từ dữ liệu mẫu.

**Hệ luật Armstrong** gồm ba luật gốc *(phản xạ, tăng trưởng, bắc cầu)* và ba luật dẫn xuất *(hợp, tách, bắc cầu giả)*. Nó **đúng đắn và đầy đủ**.

**Bao đóng `X⁺`** là tập mọi thuộc tính suy ra được từ `X` nhờ `F`, tính bằng thuật toán lăn quả cầu tuyết *(phải quét lặp nhiều vòng cho tới khi không thêm được thuộc tính mới)*. Ba công dụng thực hành: kiểm tra `X → Y` có suy ra được không (`Y ⊆ X⁺`), kiểm tra `X` có phải siêu khóa không (`X⁺ = R`), và kiểm tra hai tập phụ thuộc có tương đương không. **`X⁺` là một túi đựng các chữ cái; `F⁺` là một kho chứa các mũi tên.**

**Thuật toán tìm khóa** chia thuộc tính thành `TN` *(bắt buộc trong khóa)*, `TG` *(phải thử)*, `TĐ` *(không bao giờ trong khóa)*. Tìm **tất cả** khóa bằng cách duyệt `2^|TG|` tập con, với **mẹo rút gọn**: đã là siêu khóa thì mọi tập cha đều không tối thiểu, loại luôn.

**Phủ tối thiểu** thỏa mãn ba điều kiện: vế phải một thuộc tính, không thừa thuộc tính vế trái, không thừa phụ thuộc. **Thứ tự ba bước là bắt buộc.**

**Ba dạng chuẩn cơ bản**: **1NF** *(mọi ô chứa giá trị đơn)*, **2NF** *(đạt 1NF + không có phụ thuộc bộ phận vào khóa)*, **3NF** *(đạt 2NF + không có phụ thuộc bắc cầu — tức với mọi `X → A`, hoặc `X` là siêu khóa hoặc `A` là thuộc tính khóa)* — tóm tắt bằng câu *"the key, the whole key, and nothing but the key"*.

**Phép tách lược đồ** phải thỏa hai tiêu chuẩn: ① **Bảo toàn thông tin** *(không sinh **bộ giả** — điều kiện cần và đủ cho phép tách đôi là `(R₁ ∩ R₂)` phải là siêu khóa của `R₁` hoặc `R₂`)*; ② **Bảo toàn phụ thuộc hàm** *(mọi quy tắc nghiệp vụ vẫn kiểm tra được mà không cần `JOIN` bảng)*. **Quy tắc vàng:** luôn tách bảng theo một phụ thuộc hàm `X → Y` có trong `F`.

**Quy trình chuẩn hóa 5 bước** từ bảng phẳng về 3NF: ① Đưa về 1NF & lập tập `F` → ② Tìm tất cả khóa (`TN–TG`) & phân loại thuộc tính khóa/không khóa → ③ Chẩn đoán bằng bảng hai câu hỏi → ④ Tách khử phụ thuộc bộ phận lên 2NF → ⑤ Tách khử phụ thuộc bắc cầu lên 3NF và kiểm chứng bảo toàn.

**Các dạng chuẩn mức cao và phi chuẩn hóa**: **BCNF** đòi hỏi mọi vế trái `X` đều phải là siêu khóa *(bỏ quyền miễn trừ "`A` là thuộc tính khóa" của 3NF)*, nhưng khi có nhiều khóa chồng lấn thì việc tách lên BCNF có thể làm đứt phụ thuộc hàm — nên thực tế thường dừng ở 3NF. **Phụ thuộc đa trị `X ↠ Y`** gây bùng nổ tích ngay cả khi bảng đã đạt BCNF; **4NF** loại bỏ nó bằng phép tách luôn bảo toàn thông tin *(định lý Fagin)*. **Phi chuẩn hóa** là cố ý đưa dư thừa có kiểm soát trở lại để đổi lấy tốc độ đọc — chỉ làm **sau khi đã chuẩn hóa** và phải có cơ chế đồng bộ dữ liệu.

---


## Tài liệu tham khảo của chương

**[1]** Tô Văn Nam (2005). *Giáo trình cơ sở dữ liệu*. NXB Giáo dục — chương về lý thuyết thiết kế cơ sở dữ liệu quan hệ; phụ thuộc hàm, bao đóng, thuật toán tìm khóa, các dạng chuẩn.

**[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê — hệ luật dẫn Armstrong, phủ tối thiểu, phép tách lược đồ và các thuật toán.

**[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning — **Chapter 6** (*Normalization of Database Tables*): quy trình chuẩn hóa 1NF–3NF, BCNF, 4NF, phụ thuộc đa trị, phi chuẩn hóa và các điều kiện áp dụng, danh mục kiểm tra mô hình hóa dữ liệu.

**Hướng dẫn tự học.** Chương này **chỉ nắm được qua luyện tập** — đọc suông không đủ. Trình tự khuyến nghị: làm hết Bài A4 *(luật Armstrong)* và Bài A1 *(bao đóng)* trước khi đọc mục 5.5; làm Bài B1 *(tìm tất cả khóa và xét dạng chuẩn)* sau khi đọc mục 5.7; làm Bài B3 *(chuẩn hóa hiệu sách theo mẫu Bài tập mẫu 5.8)* sau khi đọc xong mục 5.9. Hai tiểu mục **5.10.2–5.10.3** *(phụ thuộc đa trị và 4NF)* được viết đủ chi tiết để tự đọc nếu lớp không kịp giảng; kèm Bài C2 để tự kiểm tra.

---


## Danh Mục Hình (Chương 5)

| Hình | Tên hình | Mục |
|---|---|---|
| Hình 5.1 | Bốn chương hội tụ về Chương 5 | 5.1.1 |
| Hình 5.2 | Phụ thuộc bộ phận — phép loại suy ổ khóa hai chìa | 5.2.3 |
| Hình 5.3 | Phụ thuộc bắc cầu — phải đi hai chặng | 5.2.4 |
| Hình 5.4 | Thuật toán tính bao đóng `X⁺` — phép loại suy lăn quả cầu tuyết trên lược đồ Trung tâm ABC | 5.4.2 |
| Hình 5.5 | Ba nhóm thuộc tính — và vì sao phân nhóm | 5.5.1 |
| Hình 5.6 | Lưới tám tập con của `TG = {A, B, C}` — ba siêu khóa ở tầng 1 chặn toàn bộ các tầng trên | 5.5.5 |
| Hình 5.7 | Thuật toán tìm phủ tối thiểu — phải làm đúng thứ tự | 5.6.3 |
| Hình 5.8 | Cây quyết định xác định dạng chuẩn trong phạm vi 1NF – 2NF – 3NF | 5.7.6 |
| Hình 5.9 | Nghịch lý bộ giả — không mất dòng nào mà vẫn mất sự thật | 5.8.1 |
| Hình 5.10 | Sơ đồ quy trình chuẩn hóa từng bước từ bảng phẳng `GHIDANH_PHANG` về 4 bảng đạt 3NF | 5.9.5 |
| Hình 5.11 | Mở rộng cây quyết định từ 3NF lên BCNF | 5.10.1 |
| Hình 5.12 | Sự đánh đổi giữa 3NF và BCNF khi có hai khóa chồng lấn — "Leo cao hơn chưa chắc tốt hơn" | 5.10.1 |
| Hình 5.13 | Phụ thuộc đa trị `MAGV ↠ MALOP` và `MAGV ↠ CHUNGCHI` — hai nhánh `1–N` độc lập gây bùng nổ tích | 5.10.2 |
| Hình 5.14 | Trực giác, bản vẽ, toán học — ba con đường cùng hội tụ về một thiết kế đúng | 5.11.1 |
| Hình 5.15 | Hành trình năm chương của học phần Cơ sở dữ liệu | 5.11.4 |


## Danh Mục Bảng (Chương 5)

| Bảng | Tên bảng | Mục |
|---|---|---|
| Bảng 5.1 | Bốn chương — căn cứ ra quyết định | 5.1.1 |
| Bảng 5.2 | Bốn tiêu chí — công cụ kiểm tra tương ứng | 5.1.2 |
| Bảng 5.3 | Ba loại phụ thuộc hàm | 5.2.1 |
| Bảng 5.4 | Phụ thuộc bộ phận nhìn trên dữ liệu — `GHIDANH_MORONG` với khóa `(MAHV, MALOP)` | 5.2.3 |
| Bảng 5.5 | Phụ thuộc bắc cầu nhìn trên dữ liệu — `LOP` với khóa `MALOP` | 5.2.4 |
| Bảng 5.6 | Ba luật gốc và ba luật dẫn xuất | 5.3.2 |
| Bảng 5.7 | Chứng minh ba luật dẫn xuất từ ba luật gốc của Armstrong | 5.3.2 |
| Bảng 5.8 | Sáu luật, mỗi luật một ví dụ tại ABC | 5.3.2 |
| Bảng 5.9 | Ba ngụy biện thường gặp khi suy diễn bằng luật Armstrong | 5.3.4 |
| Bảng 5.10 | Dữ liệu `GHIDANH_MORONG` bác bỏ cả ba ngụy biện suy diễn | 5.3.4 |
| Bảng 5.11 | Bảng vết từng bước tính `(MAHV, MALOP)⁺` khớp với Hình 5.4 | 5.4.2 |
| Bảng 5.12 | Tính `A⁺` với `F = {B → C, A → B}` trên `R(A, B, C)` — quét một lượt thì sót, hai vòng mới đủ | 5.4.2 |
| Bảng 5.13 | Tóm tắt ba câu hỏi lớn quy về phép tính bao đóng — minh họa trên `R(A, B, C, D)`, `F = {A → B, B → C, CD → A}` | 5.4.4 |
| Bảng 5.14 | Đối chiếu trực diện `X⁺` và `F⁺` | 5.4.5 |
| Bảng 5.15 | Phân nhóm bảy thuộc tính của `GHIDANH_PHANG` — gạch vế trái, gạch vế phải | 5.5.1 |
| Bảng 5.16 | Tổng hợp cách phân loại thuộc tính khóa và không khóa của Ví dụ 5.10 | 5.7.1 |
| Bảng 5.17 | Minh họa Dạng chuẩn 1 (1NF) — Trước và Sau khi khử ô đa giá trị | 5.7.2 |
| Bảng 5.18 | Minh họa Dạng chuẩn 2 (2NF) — Trước và Sau khi khử phụ thuộc bộ phận | 5.7.3 |
| Bảng 5.19 | Minh họa Dạng chuẩn 3 (3NF) — Trước và Sau khi khử phụ thuộc bắc cầu | 5.7.4 |
| Bảng 5.20 | Bảng chẩn đoán bằng "hai câu hỏi" cho ba lược đồ của Ví dụ 5.14 | 5.7.5 |
| Bảng 5.21 | Bảng vàng tổng hợp ba dạng chuẩn 1NF, 2NF, 3NF — điều kiện, thủ phạm bị diệt và cách sửa | 5.7.6 |
| Bảng 5.22 | Tách sai `R` theo `MAGV` — không mất dòng nào, nhưng ghép lại sinh ra hai bộ giả | 5.8.1 |
| Bảng 5.23 | Tách đúng `R` theo `MALOP` — ghép lại thu được đúng 3 dòng gốc, không có bộ giả | 5.8.2 |
| Bảng 5.24 | Phép tách bảo toàn thông tin nhưng đánh mất phụ thuộc hàm `MAGV → HOTEN_GV` | 5.8.3 |
| Bảng 5.25 | Tổng quan quy trình 5 bước chuẩn hóa một bảng phẳng về 3NF | 5.9 |
| Bảng 5.26 | Tập phụ thuộc hàm `F` của `GHIDANH_PHANG` — rút từ quy tắc nghiệp vụ | 5.9.2 |
| Bảng 5.27 | Chẩn đoán từng phụ thuộc hàm của `GHIDANH_PHANG` với khóa duy nhất `K = (MAHV, MALOP)` | 5.9.4 |
| Bảng 5.28 | Tổng hợp kết quả chẩn đoán dạng chuẩn của `GHIDANH_PHANG` | 5.9.4 |
| Bảng 5.29 | Ba dòng của `GHIDANH_PHANG` sau khi chuẩn hóa về 3NF — bốn bảng, không còn bất kỳ giá trị nào bị chép lặp | 5.9.5 |
| Bảng 5.30 | Kiểm chứng cả ba phép tách trong quy trình chuẩn hóa `GHIDANH_PHANG` | 5.9.6 |
| Bảng 5.31 | Đối chiếu trực diện 3NF và BCNF | 5.10.1 |
| Bảng 5.32 | Phân tích `HV_KH_GV(MAHV, MAKH, MAGV)` — đạt 3NF, vi phạm BCNF, và hậu quả khi tách lên BCNF | 5.10.1 |
| Bảng 5.33 | Bảng tổng hợp toàn bộ thang đo các dạng chuẩn từ 1NF đến 4NF | 5.10.3 |
| Bảng 5.34 | Bốn điều kiện bắt buộc để quyết định phi chuẩn hóa là hợp lý | 5.10.4 |
| Bảng 5.35 | Ba dị thường của Chương 1 khi đặt lên lược đồ 3NF cuối cùng | 5.11.2 |
| Bảng 5.36 | Mọi lời hẹn suốt học phần và nơi giải quyết tại Chương 5 | 5.11.3 |


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
| **UNF** | Unnormalized Form | Dạng chưa chuẩn hóa *(chưa đạt 1NF)* |
| **X⁺** | closure of attribute set X | Bao đóng của tập thuộc tính `X` |
| **→** | functional dependency | Phụ thuộc hàm |
| **↠** | multivalued dependency | Phụ thuộc đa trị |
| **⋈** | natural join | Phép kết tự nhiên |
