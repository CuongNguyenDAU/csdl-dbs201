# ĐỀ CƯƠNG CHI TIẾT HỌC PHẦN — BẢN CHỈNH SỬA v2

> **Ghi chú biên tập (v2 — 27/07/2026):** Bản này làm lại **khung chương trình** và **nội dung giảng dạy** theo yêu cầu:
> ① **Bỏ hai chuyên đề tách riêng** — nội dung được **tích hợp vào các chương**;
> ② **Đào sâu kiến thức** từng chương, bổ sung nội dung nâng cao tham khảo **[3] Coronel & Morris, *Database Systems*** (đặc biệt Ch.5 *Advanced Data Modeling* và Ch.6 *Normalization*);
> ③ **Nhịp giảng dạy 4 tiết/tuần** (tuần 11: 5 tiết) — mỗi chương **trọn tuần**, dễ xếp lịch;
> ④ **Thiết kế 90 tiết tự học** có cấu trúc (khắc phục điểm yếu "tự học không có thiết kế");
> ⑤ Bổ sung **ma trận CLO ↔ Chương ↔ Công cụ đánh giá**.
>
> *Kế thừa v1:* bỏ CLO4/CO4 (gộp *toàn vẹn* vào CLO3; hoãn *SQL · an toàn · giao dịch · Client‑Server* sang học phần **Hệ quản trị CSDL**). Chỗ `«CẦN THẦY ĐIỀN»` cần thầy bổ sung.

---

## 1. Thông tin chung (General Information)

|                                              |                                                    |
| -------------------------------------------- | -------------------------------------------------- |
| 1.1. Trình độ đào tạo*(Level)*       | Đại học*(Undergraduate)*                      |
| 1.2. Chương trình đào tạo*(Program)* | Công nghệ thông tin*(Information Technology)* |

## 2. Thông tin chung học phần (Course Information)

|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1. Tên học phần                             | Cơ sở dữ liệu —*Database Systems*                                                                                                                                                                                                                                                                                                                                                                             |
| 2.2. Mã học phần                              | DBS201                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2.3. Nhóm học phần                            | Cơ sở ngành                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2.4. Số tín chỉ                               | 3.0                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2.5. Phân phối thời gian                      | **135 tiết** — Lý thuyết: **45**; Đồ án: 0; Thực hành/Thí nghiệm: 0; Tự học: **90**                                                                                                                                                                                                                                                                                                   |
| 2.6. Số tuần thực hiện                       | **11 tuần** — *nhịp **4 tiết/tuần**, riêng tuần 11: **5 tiết***                                                                                                                                                                                                                                                                                                                          |
| 2.7. Niên khóa áp dụng                       | 2024‑2025; 2025‑2026                                                                                                                                                                                                                                                                                                                                                                                               |
| 2.8. Giảng viên phụ trách chính             | Nguyễn Tất Phú Cường —*Cùng giảng dạy:* Phạm Thị Dung                                                                                                                                                                                                                                                                                                                                                   |
| 2.9–2.10. Khoa/Bộ môn phụ trách & quản lý | Công nghệ thông tin                                                                                                                                                                                                                                                                                                                                                                                               |
| 2.11. Nơi tiến hành                           | Phòng học lý thuyết                                                                                                                                                                                                                                                                                                                                                                                              |
| 2.12. Loại học phần                           | Bắt buộc                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2.13. Điều kiện tham gia                      | *Học trước:* (BIN101) Tin học cơ bản — *Tiên quyết:* không — *Song hành:* không                                                                                                                                                                                                                                                                                                                   |
| 2.14. 🆕 Giả định về nền tảng người học | Sinh viên**chỉ mới học Tin học cơ bản**, **chưa học SQL hay hệ quản trị CSDL**. Vì vậy mọi **bài tập và nhiệm vụ tự học** của học phần chỉ đòi hỏi **tư duy thiết kế trên giấy** và **công cụ vẽ sơ đồ miễn phí** (draw.io); phần thao tác trên DBMS chỉ xuất hiện dưới dạng **demo minh họa của giảng viên** trên lớp |

---

## 3. Mô tả vắn tắt học phần (Course Description)

Học phần Cơ sở dữ liệu trang bị **nền tảng mô hình hóa và thiết kế cơ sở dữ liệu**, gồm: các khái niệm cơ bản của một hệ cơ sở dữ liệu và kiến trúc ba mức; **mô hình thực thể–liên kết (ER)** và **mô hình ER mở rộng (EER)**; **mô hình dữ liệu quan hệ** và **đại số quan hệ**; **ràng buộc toàn vẹn** dữ liệu; **lý thuyết thiết kế** — phụ thuộc hàm, các dạng chuẩn (1NF–BCNF) và kỹ thuật chuẩn hóa lược đồ quan hệ.

> 📌 *Ngôn ngữ **SQL**, **an toàn – bảo mật** và **quản lý giao dịch** được bố trí ở học phần **Hệ quản trị cơ sở dữ liệu** kế tiếp; học phần này tập trung vào **THIẾT KẾ ĐÚNG** — nền móng cho mọi hệ thống dữ liệu.*

*The course provides foundations of database modeling and design: basic concepts of a database system and the three‑level architecture; Entity–Relationship (ER) and Extended ER (EER) models; the relational data model and relational algebra; data integrity constraints; design theory — functional dependencies, normal forms (1NF–BCNF) and normalization techniques. (SQL, security, and transaction management are placed in the subsequent Database Management Systems course.)*

---

## 4. Mục tiêu học phần (Course Objectives – COs)

| CO            | Mô tả                                                                                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CO1** | Nghiêm túc, chủ động, hợp tác, tuân thủ đạo đức khi nghiên cứu và áp dụng hệ CSDL.                                                                                      |
| **CO2** | Mô tả, phân tích các khái niệm, mô hình hóa dữ liệu (ER, EER, quan hệ), cơ chế lưu trữ và**ràng buộc toàn vẹn** dữ liệu.                                     |
| **CO3** | Thiết kế mô hình dữ liệu (ER/EER, UML), ánh xạ ER sang quan hệ, phân tích ràng buộc toàn vẹn,**chuẩn hóa lược đồ** và vận dụng các thuật toán thiết kế. |

## 5. Chuẩn đầu ra học phần (Course Learning Outcomes – CLOs)

| CLO            | Mô tả                                                                                                                                                                                                                                                             | Mức Bloom                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **CLO1** | Thể hiện tinh thần trách nhiệm, chủ động học tập, tuân thủ nội quy,**hợp tác nhóm hiệu quả** trong các hoạt động học tập và bài tập củng cố.                                                                                     | *Hưởng ứng – Hình thành giá trị*         |
| **CLO2** | **Trình bày và giải thích** các khái niệm, mô hình ER/EER, mô hình quan hệ, đại số quan hệ, thuật toán thiết kế, cấu trúc DBMS và các vấn đề cơ bản của CSDL.                                                                  | **Hiểu**                                    |
| **CLO3** | **Phân tích** bài toán thực tế, **thiết kế** mô hình ER, **ánh xạ** sang lược đồ quan hệ, **đánh giá tính toàn vẹn**, **chuẩn hóa** lược đồ và **chứng minh** phép tách bảo toàn thông tin. | **Vận dụng – Phân tích – Đánh giá** |

---

## 6. Ma trận CLO ↔ PLO và chỉ số PI

Mức đóng góp: **I** *(Introduced)* – giới thiệu · **R** *(Reinforced)* – nâng cao, có thực hành · **M** *(Mastery)* – thuần thục · **A** *(Assessment)* – thu thập minh chứng đánh giá PLO.

| CLO  | PLO…                 | PLO… | PLO… | PI |
| ---- | --------------------- | ----- | ----- | -- |
| CLO1 | «CẦN THẦY ĐIỀN» |       |       |    |
| CLO2 | «CẦN THẦY ĐIỀN» |       |       |    |
| CLO3 | «CẦN THẦY ĐIỀN» |       |       |    |

> ⚠️ **Trước khi chốt:** đối chiếu ma trận gốc — nếu **CLO4 cũ** là chỗ *duy nhất* đóng góp cho một PLO nào, hãy chuyển đóng góp đó sang **CLO2/CLO3** rồi mới bỏ, tránh **hụt phủ PLO**.

### 6.1. 🆕 Ma trận CLO ↔ Chương ↔ Công cụ đánh giá *(chứng minh constructive alignment)*

| Chương                                               |  Số tiết  |    CLO1    |    CLO2    |       CLO3       | Đánh giá bằng                                                                                                          |
| ------------------------------------------------------ | :----------: | :---------: | :---------: | :--------------: | -------------------------------------------------------------------------------------------------------------------------- |
| **Ch1.** Tổng quan về CSDL                     |      4      |            | **I** |                  | KT viết · Trắc nghiệm                                                                                                  |
| **Ch2.** Mô hình ER và ER mở rộng           |      8      |      R      | **R** | **I → R** | KT viết ·**KT thực hành** · Trắc nghiệm                                                                       |
| **Ch3.** Mô hình quan hệ & đại số quan hệ |      8      |      R      | **R** |   **R**   | KT viết ·**KT thực hành** · Trắc nghiệm                                                                       |
| **Ch4.** Ràng buộc toàn vẹn                  |      8      |      R      |      R      | **R → M** | **KT thực hành** · Trắc nghiệm                                                                                  |
| **Ch5.** Lý thuyết thiết kế & chuẩn hóa    |      12      |      R      | **M** | **M · A** | **KT thực hành** · Trắc nghiệm                                                                                  |
| **Ôn tập & tổng hợp**                        |      5      | **A** |      A      |   **A**   | Bài tập nhóm*(CLO1 — Rubric 1b)* · ✏️ **KT thực hành** *(CLO3 — Rubric 3)* · Trắc nghiệm *(CLO2)* |
| **TỔNG**                                        | **45** |            |            |                  |                                                                                                                            |

> 💡 **Đọc bảng:** CLO3 được **giới thiệu ở Ch2**, **củng cố ở Ch3–Ch4**, **thuần thục ở Ch5** và **thu thập minh chứng ở tuần ôn tập** *(KT thực hành)* — đúng nguyên tắc *xoắn ốc* (spiral) của OBE.
>
> ✏️ *Đã sửa khi rà rubric:* dòng **Ôn tập & tổng hợp** trước đây ghi *"Đánh giá bằng: Bài tập nhóm"* cho **cả ba CLO** — mâu thuẫn với Mục 7.2 *(bài tập nhóm chỉ gán CLO1)* và với **Rubric 1b** *(chỉ có tiêu chí đóng góp & phối hợp, **không** chấm chất lượng chuyên môn của sản phẩm)*. Nay ghi đúng công cụ cho từng CLO.

---

## 7. Đánh giá học phần (Assessment)

### 7.1. Thang điểm đánh giá (Grading Scale)

Dùng **thang điểm 10** để chấm, lấy đến **1 chữ số thập phân**; quy đổi sang **điểm chữ** và **thang 4,0**.

| STT | Điểm thang 10                   | Điểm chữ | Thang 4,0 | Xếp loại                       |
| :-: | --------------------------------- | :----------: | :-------: | -------------------------------- |
|  1  | Từ**9,5** đến 10,0       | **A+** |    4,0    | Xuất sắc                       |
|  2  | Từ**8,5** đến dưới 9,5 | **A** |    4,0    | Giỏi                            |
|  3  | Từ**8,0** đến dưới 8,5 | **B+** |    3,5    | Khá giỏi                       |
|  4  | Từ**7,0** đến dưới 8,0 | **B** |    3,0    | Khá                             |
|  5  | Từ**6,5** đến dưới 7,0 | **C+** |    2,5    | Trung bình khá                 |
|  6  | Từ**5,5** đến dưới 6,5 | **C** |    2,0    | Trung bình                      |
|  7  | Từ**5,0** đến dưới 5,5 | **D+** |    1,5    | Trung bình yếu                 |
|  8  | Từ**4,0** đến dưới 5,0 | **D** |    1,0    | Yếu*(đạt có điều kiện)* |
|  9  | Từ**0,0** đến dưới 4,0 | **F** |     0     | **Không đạt**           |

> ✏️ *Bảng này trước đây chỉ được ghi chú "giữ nguyên như đề cương gốc" — nay **chép đầy đủ** để đề cương tự chứa, không phải tra chéo tài liệu khác.*

### 7.2. Kế hoạch đánh giá

| Thành phần & phương pháp                                       | Trọng số (%) | CLO                              | Rubric    | Thời điểm           |
| ------------------------------------------------------------------- | :------------: | -------------------------------- | --------- | ---------------------- |
| **Đánh giá thường xuyên**                               |  **30**  |                                  |           |                        |
| — Chuyên cần (đi học, ý thức kỷ luật)                      |      10.0      | CLO1                             | Rubric 1  | Cả học phần         |
| —**Bài tập nhóm (củng cố)**                             |      5.0      | CLO1                             | Rubric 1b | Tuần 11               |
| — Bài kiểm tra viết                                             |      15.0      | CLO2                             | Rubric 2  | Tuần 5                |
| **Đánh giá giữa học phần**                              |  **20**  |                                  |           |                        |
| —**Bài kiểm tra thực hành** *(thiết kế trên giấy)* |      20.0      | CLO3                             | Rubric 3  | ✏️**Tuần 11** |
| **Đánh giá cuối học phần**                              |  **50**  |                                  |           |                        |
| — Bài kiểm tra trắc nghiệm                                     |      50.0      | **CLO2: 40% · CLO3: 60%** | Rubric 4  | Theo lịch Trường    |

**Phủ CLO trong đánh giá:** CLO1 = **15%** *(10 + 5)* · CLO2 = **35%** *(15 + 50×40%)* · CLO3 = **50%** *(20 + 50×60%)*. → Tổng **100%** ✔

> ✏️ **Vì sao chuyển KT thực hành từ tuần 8 sang tuần 11:** Rubric 3 chấm cả **chuẩn hóa** và **chứng minh phép tách bảo toàn thông tin** — các mục 5.7–5.9 chỉ dạy ở **tuần 9–10**. Ở tuần 8 sinh viên mới học đến bao đóng `X⁺`, nên đề thi cũ **kiểm tra nội dung chưa được dạy**. Đặt ở tuần 11 thì toàn bộ quy trình thiết kế đã hoàn tất, bài kiểm tra mới đo đúng CLO3.
>
> ⚠️ *Cần xác nhận với Khoa:* thành phần này mang tên **"đánh giá giữa học phần"** nhưng nay tổ chức ở tuần cuối. Nếu quy chế Trường buộc đánh giá giữa kỳ phải nằm trong nửa đầu học phần, phương án thay thế là **giữ tuần 8** và **thu hẹp Rubric 3** còn 3 tiêu chí *(bỏ chuẩn hóa)* — khi đó phần chuẩn hóa chỉ còn được đo bằng trắc nghiệm cuối kỳ.

### 7.3. Rubric đánh giá (Assessment Rubrics) — ✏️ **xây dựng lại đầy đủ ở v2**

#### 7.3.0. Quy ước chung khi dùng rubric

| Nội dung                          | Quy định                                                                                                                                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Số mức chất lượng**   | Thống nhất**5 mức** cho mọi rubric: Kém **0%** · Yếu **25%** · Trung bình **50%** · Khá **75%** · Giỏi/Xuất sắc **100%**                              |
| **Tổng trọng số**         | Mỗi rubric có tổng trọng số các tiêu chí =**100**                                                                                                                                          |
| **Công thức tính**        | `Điểm thành phần (thang 10) = Σ (Trọng số tiêu chí × Mức đạt) ÷ 100` — trong đó *Mức đạt* lấy giá trị 0 / 2,5 / 5,0 / 7,5 / 10,0                                              |
| **Làm tròn**               | Điểm thành phần lấy đến**1 chữ số thập phân**                                                                                                                                           |
| **Vắng mặt / không nộp** | Tính**0 điểm** cho thành phần đó, trừ trường hợp có lý do chính đáng được Khoa chấp thuận                                                                                     |
| **Chọn mức**               | Sinh viên được xếp vào mức mà**mô tả khớp nhất**. Nếu vượt hoàn toàn mức dưới nhưng chưa đạt đủ mức trên → chọn **mức dưới**                                |
| **Công bố**                | Toàn bộ rubric được**phát cho sinh viên trong buổi học đầu tiên** và nhắc lại trước mỗi bài đánh giá — sinh viên phải biết mình được chấm bằng thước đo nào    |
| **Chấm bài thiết kế**    | Bài kiểm tra thực hành*(Rubric 3)* chấm theo **đáp án có sẵn danh mục quy tắc nghiệp vụ**; khuyến nghị 2 giảng viên chấm độc lập một mẫu ~10% số bài để đối chiếu |

---

#### **Rubric 1 — Chuyên cần & thái độ học tập** · *đo **CLO1*** · trọng số học phần **10%**

| Tiêu chí                                                                                 | TS | CLO | Kém (0%)                              | Yếu (25%)                     | Trung bình (50%)                               | Khá (75%)                                    | Giỏi/Xuất sắc (100%)                          |
| ------------------------------------------------------------------------------------------ | :-: | :--: | -------------------------------------- | ------------------------------ | ----------------------------------------------- | --------------------------------------------- | ------------------------------------------------ |
| **1.1.** Đi học đầy đủ, đúng giờ                                            | 40 | CLO1 | Vắng/trễ**> 7 buổi**          | Vắng/trễ**5–6 buổi** | Vắng/trễ**3–4 buổi**                  | Vắng/trễ**1–2 buổi**, có phép     | **Đi học đủ**, luôn đúng giờ       |
| **1.2.** Tuân thủ nội quy, tôn trọng giảng viên và bạn học                 | 30 | CLO1 | Vi phạm nhiều lần, phải nhắc nhở | Vi phạm vài lần             | Cơ bản tuân thủ, đôi lúc mất tập trung | Tuân thủ tốt, tập trung nghe giảng       | Gương mẫu, góp phần giữ nền nếp chung    |
| **1.3.** 🆕 **Chủ động học tập** — nộp sản phẩm tự học *(Mục 9)* | 30 | CLO1 | Nộp**< 30%** số nhiệm vụ     | Nộp**30–49%**          | Nộp**50–69%**                           | Nộp**70–89%**, phần lớn đúng hạn | Nộp**≥ 90%**, đúng hạn, có đầu tư |

> 💡 **Vì sao thêm tiêu chí 1.3.** ① CLO1 nêu rõ *"**chủ động học tập**"* nhưng rubric cũ chỉ đo **đi học** và **nội quy** — thiếu phủ CLO; ② **Mục 9 yêu cầu nộp sản phẩm tự học suốt 11 tuần nhưng không gắn với thành phần điểm nào**, nên sinh viên không có động lực thực hiện. Tiêu chí 1.3 nối hai chỗ đó lại. *(Việc vắng quá tỷ lệ quy định vẫn xử lý theo quy chế Trường, độc lập với rubric.)*

---

#### **Rubric 1b — Bài tập nhóm tổng hợp** · *đo **CLO1** (hợp tác nhóm)* · trọng số học phần **5%** · tuần 11

| Tiêu chí                                                  | TS | CLO | Kém (0%)                         | Yếu (25%)                                                         | Trung bình (50%)                                                 | Khá (75%)                                                        | Giỏi/Xuất sắc (100%)                                                 |
| ----------------------------------------------------------- | :-: | :--: | --------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **1b.1.** Đóng góp cá nhân vào sản phẩm nhóm | 50 | CLO1 | Không tham gia                   | Có tên trong nhóm nhưng đóng góp**không đáng kể** | Làm phần được giao ở**mức tối thiểu**, phải nhắc | **Hoàn thành đầy đủ** phần được giao, đúng hạn | **Chủ động nhận thêm việc**, chất lượng cao, đúng hạn |
| **1b.2.** Phối hợp & trách nhiệm với nhóm       | 50 | CLO1 | Gây cản trở, không phối hợp | Ít trao đổi, làm rời rạc với nhóm                          | Phối hợp khi được yêu cầu                                  | Trao đổi chủ động, tôn trọng ý kiến khác                | **Điều phối / hỗ trợ** thành viên, sản phẩm thống nhất |

**📋 Phiếu đánh giá đồng đẳng** *(bắt buộc — nộp cùng sản phẩm nhóm)*

Giảng viên **không quan sát được** phần việc mỗi thành viên làm ở nhà, nên tiêu chí **1b.1** cần thêm dữ liệu từ chính nhóm:

- Mỗi sinh viên **phân bổ 100 điểm** cho **tất cả** thành viên trong nhóm *(kể cả bản thân)* theo mức đóng góp thực tế, kèm **một câu giải thích** cho người được cho điểm cao nhất và thấp nhất.
- **Tỷ lệ đóng góp** của mỗi sinh viên = trung bình cộng số điểm mà các bạn dành cho người đó.
- Mốc đối chiếu là mức chia đều `100 ÷ n` *(n = số thành viên)*. Nếu tỷ lệ đóng góp của một sinh viên **< 60%** mốc chia đều, giảng viên **hạ ít nhất một mức** ở tiêu chí 1b.1; nếu **> 140%**, được **nâng một mức**.
- Phiếu nộp **riêng, không công khai** giữa các thành viên.

> 💡 *Thay đổi:* rubric cũ chỉ có **3 mức** (0/50/100) trong khi các rubric khác 5 mức — vừa không nhất quán, vừa làm điểm **nhảy bậc thô** (trên thang 5% thì chênh nhau tới 2,5%). Mức 25% và 75% bổ sung để phân biệt *"có tên nhưng không làm"* với *"làm tối thiểu"*, và *"làm đủ phần mình"* với *"hỗ trợ cả nhóm"*.

---

#### **Rubric 2 — Bài kiểm tra viết** · *đo **CLO2*** · trọng số học phần **15%** · tuần 5

| Tiêu chí                                                      | TS | CLO | Kém (0%)                                               | Yếu (25%)                                        | Trung bình (50%)                                                | Khá (75%)                                             | Giỏi/Xuất sắc (100%)                                        |
| --------------------------------------------------------------- | :-: | :--: | ------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| **2.1.** Trả lời đúng trọng tâm câu hỏi           | 60 | CLO2 | Đúng**< 30%** nội dung *(hoặc không làm)* | Đúng**30–49%**                           | Đúng**50–69%**                                          | Đúng**70–89%**, diễn đạt rõ               | Đúng**≥ 90%**, giải thích mạch lạc                |
| **2.2.** 🆕 **Giải thích bằng ví dụ TỰ NÊU** | 25 | CLO2 | Không có ví dụ                                      | **Chép nguyên** ví dụ trong bài giảng | Ví dụ tự nêu nhưng sơ sài / chưa khớp ý cần minh họa | Ví dụ tự nêu**đúng**, minh họa được ý | Ví dụ tự nêu,**liên hệ thực tiễn**, làm bật ý |
| **2.3.** Dùng đúng thuật ngữ, trình bày            | 15 | CLO2 | Sai thuật ngữ cơ bản, trình bày khó theo dõi    | Nhiều lỗi thuật ngữ                           | Đúng cơ bản, diễn đạt còn lủng củng                    | Đúng chuẩn thuật ngữ, rõ ràng                   | Chính xác, sáng rõ, lập luận chặt chẽ                  |

> 💡 **Hai thay đổi.** ① Tiêu chí 2.2 đổi từ *"Phân tích, liên hệ, dẫn chứng"* → **"Giải thích bằng ví dụ TỰ NÊU"**: đo đúng mức Bloom *Hiểu* của CLO2 và **chống học vẹt** — sinh viên chép ví dụ bài giảng chỉ đạt mức Yếu. ② Tiêu chí 2.1 trước đây **hở thang đo**: bài đúng **50–59%** không thuộc mức nào *(mức Yếu ghi "< 50%", mức TB ghi "60–70%")*, còn mức Khá/Giỏi mô tả định tính *("gần đầy đủ", "hoàn toàn đúng")* nên hai người chấm dễ ra hai điểm khác nhau. Nay chia dải **liền mạch, không hở, không chồng lấn**.

---

#### **Rubric 3 — Bài kiểm tra thực hành** *(thiết kế trên giấy)* · *đo **CLO3*** · trọng số học phần **20%** · ✏️ tuần 11

| Tiêu chí                                                                               | TS | CLO | Kém (0%)                                | Yếu (25%)                                                     | Trung bình (50%)                                                                                       | Khá (75%)                                                   | Giỏi/Xuất sắc (100%)                                                                  |
| ---------------------------------------------------------------------------------------- | :-: | :--: | ---------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **3.1.** Phân tích đề bài, phát biểu **quy tắc nghiệp vụ**         | 20 | CLO3 | Không phát biểu được quy tắc nào | Nêu**< 30%** số quy tắc trong đáp án               | Nêu**30–59%**, phát biểu còn mơ hồ                                                         | Nêu**60–84%**, phát biểu rõ, *"đếm được"*  | Nêu**≥ 85%**, chính xác, đủ **bản số** và *bắt buộc/tùy chọn* |
| **3.2.** **Thiết kế mô hình ER và ánh xạ** sang lược đồ quan hệ  | 40 | CLO3 | Không làm / sai hoàn toàn            | Thiếu nhiều thực thể–liên kết;**sai loại khóa** | Đủ thực thể chính; còn**sai bản số** hoặc ánh xạ **M:N / đa trị** chưa đúng | Đúng phần lớn; PK/FK hợp lý; trình bày rõ           | Đúng và đủ; xử lý chuẩn**M:N, đa trị, thực thể yếu**                  |
| **3.3.** **Ràng buộc toàn vẹn & chuẩn hóa**                            | 30 | CLO3 | Không thực hiện                       | Nêu vài RBTV rời rạc;**chưa chuẩn hóa**           | Chuẩn hóa**đến 2NF**, hoặc xác định sai một số phụ thuộc hàm                         | Chuẩn hóa**đúng đến 3NF**; nêu đủ RBTV chính | Đạt 3NF**và chứng minh được phép tách bảo toàn thông tin**             |
| **3.4.** 🆕 **Thuyết minh & bảo vệ quyết định thiết kế** *(viết)* | 10 | CLO3 | Không viết phần thuyết minh          | Nêu chung chung, không gắn với đề bài                   | Giải thích được**1 quyết định**                                                           | Giải thích**≥ 3 quyết định**, lý do hợp lý    | Lập luận theo**nghiệp vụ**, có **so sánh phương án thay thế**      |

> ⚠️ **Yêu cầu bắt buộc khi ra đề — nếu thiếu, Rubric 3 không dùng được:**
>
> 1. **Đáp án phải liệt kê sẵn `N` quy tắc nghiệp vụ** *(khuyến nghị N = 8–12)*. Tiêu chí 3.1 neo theo tỷ lệ trên `N`; không có `N` thì quay lại chấm cảm tính.
> 2. **Đề phải có một câu thuyết minh viết bắt buộc**, dạng: *"Giải thích ít nhất 3 quyết định thiết kế của em — ví dụ: vì sao chọn khóa chính này, vì sao tách bảng cho liên kết M:N, vì sao dừng ở 3NF mà không chuẩn hóa tiếp."* Không có câu này thì sinh viên **không có chỗ để "bảo vệ"** và tiêu chí 3.4 vô nghĩa.
>
> 💡 **Ba thay đổi.** ① Mức Yếu và Trung bình của tiêu chí 3.2 trong đề cương gốc **trùng nhau từng chữ** *("Có mô hình cơ bản, chỗ sai")* — lỗi kỹ thuật khiến không phân biệt được hai mức. ② Mức Trung bình của 3.1 ghi *"Đáp ứng phần lớn yêu cầu"*: không nhắc đến quy tắc nghiệp vụ *(thứ đang chấm)*, mâu thuẫn về mức độ *("phần lớn" nghe cao hơn 50%)*, lại gần trùng mức Khá. ③ Bổ sung tiêu chí **3.4** để đo phần *"đánh giá"* trong CLO3 — thiết kế đúng chưa đủ, phải **giải thích được vì sao chọn thế**.

---

#### **Rubric 4 — Bài kiểm tra trắc nghiệm** · *đo **CLO2 + CLO3*** · trọng số học phần **50%** · theo lịch Trường

| Khối câu hỏi                                                                                                                                                          | TS | CLO | Kém (0%)                       | Yếu (25%)              | Trung bình (50%)       | Khá (75%)              | Giỏi/Xuất sắc (100%)  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-: | :--: | ------------------------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ |
| **A.** Khái niệm CSDL, kiến trúc 3 mức, mô hình **ER/EER**, mô hình quan hệ, đại số quan hệ, cấu trúc DBMS                                   | 40 | CLO2 | Đúng**≤ 30%** số câu | Đúng**31–54%** | Đúng**55–69%** | Đúng**70–84%** | Đúng**85–100%** |
| **B.** Thiết kế ER, ánh xạ sang lược đồ quan hệ, đánh giá **ràng buộc toàn vẹn**, phụ thuộc hàm, các **dạng chuẩn**, phép tách | 60 | CLO3 | Đúng**≤ 30%** số câu | Đúng**31–54%** | Đúng**55–69%** | Đúng**70–84%** | Đúng**85–100%** |

**📐 Ma trận đề — đặc tả bắt buộc**

|    Khối    | Tỷ lệ số câu | Dạng câu hỏi                                                                                                                                                                                                                               | Mức Bloom cần đạt         |
| :---------: | :--------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **A** |       40%       | Nhận biết · giải thích ·**phân biệt cặp khái niệm dễ nhầm** *(CSDL ↔ DBMS; khóa chính ↔ khóa ứng viên; thực thể ↔ kiểu thực thể)*                                                                           | *Nhớ · Hiểu*             |
| **B** |       60%       | ⚠️**Câu hỏi tình huống — mỗi câu phải kèm dữ kiện** *(lược đồ quan hệ, tập phụ thuộc hàm, ERD, hoặc bảng dữ liệu mẫu)* để sinh viên **suy luận / tính toán** rồi mới chọn được đáp án | *Vận dụng · Phân tích* |

> ⚠️ **Cảnh báo về tính giá trị (validity) — cần lưu ý khi ra đề.** CLO3 chiếm **50%** tổng điểm học phần, trong đó **30/50 điểm đến từ trắc nghiệm**. Nhưng CLO3 ở mức Bloom **Vận dụng – Phân tích – Đánh giá**, còn trắc nghiệm nếu ra theo lối *tái hiện định nghĩa* thì chỉ đo được mức **Nhớ**. Khi đó đề cương **tuyên bố** đo Phân tích nhưng **thực tế** đo Ghi nhớ — đây là lỗi *constructive alignment* mà đoàn kiểm định thường soi.
>
> **Cách khắc phục đã ràng buộc trong ma trận trên:** khối B **không** được dùng câu kiểu *"Dạng chuẩn 3NF là gì?"*, mà phải là:
>
>> *Cho `R(A, B, C, D)` với `F = {A → B, B → C}` và khóa chính là `A`. Lược đồ `R` đạt dạng chuẩn cao nhất là:* &nbsp; `A. 1NF` &nbsp; `B. 2NF` &nbsp; `C. 3NF` &nbsp; `D. BCNF`
>>
>
> — sinh viên buộc phải **làm bài** *(tìm khóa, phát hiện phụ thuộc bắc cầu `A → B → C`)* mới trả lời được.

> 📌 **Lưu ý kỹ thuật khi chấm:** đề trắc nghiệm phải **tách riêng phần điểm khối A và khối B** khi nhập điểm, vì Mục 7.5 cần hai con số này để tính mức đạt CLO2 và CLO3. Nếu chỉ lưu tổng điểm trắc nghiệm thì **không báo cáo được mức đạt CLO**.

---

### 7.4. 🆕 Cách tính điểm học phần — ví dụ minh họa

**Công thức:**

```
Điểm học phần = 10% × Rubric 1  +  5% × Rubric 1b  +  15% × Rubric 2
              + 20% × Rubric 3  +  50% × Rubric 4
```

**Ví dụ — sinh viên Nguyễn Văn A:**

| Rubric                       | Mức đạt từng tiêu chí                                     | Tính điểm                              |  Điểm /10  | × TS |    Góp vào    |
| ---------------------------- | --------------------------------------------------------------- | ----------------------------------------- | :-----------: | :---: | :-------------: |
| **1** Chuyên cần     | 1.1 = 100% · 1.2 = 75% · 1.3 = 75%*(nộp 8/11 nhiệm vụ)*  | (40×10 + 30×7,5 + 30×7,5)/100          | **8,5** |  10%  |      0,85      |
| **1b** Bài tập nhóm | 1b.1 = 75% · 1b.2 = 100%                                       | (50×7,5 + 50×10)/100                    | **8,8** |  5%  |      0,44      |
| **2** KT viết         | 2.1 = 75%*(đúng 78%)* · 2.2 = 50% · 2.3 = 75%             | (60×7,5 + 25×5 + 15×7,5)/100           | **6,9** |  15%  |      1,035      |
| **3** KT thực hành   | 3.1 = 75% · 3.2 = 75% · 3.3 = 50% · 3.4 = 75%                | (20×7,5 + 40×7,5 + 30×5 + 10×7,5)/100 | **6,8** |  20%  |      1,36      |
| **4** Trắc nghiệm    | Khối A = 75%*(đúng 80%)* · Khối B = 50% *(đúng 62%)* | (40×7,5 + 60×5)/100                     | **6,0** |  50%  |      3,00      |
|                              |                                                                 | **CỘNG**                           |              |      | **6,685** |

→ Làm tròn 1 chữ số thập phân: **6,7**. Tra Mục 7.1, **6,7** thuộc dải *"từ 6,5 đến dưới 7,0"* ⇒ điểm chữ **C+**, thang 4,0 = **2,5**.

---

### 7.5. 🆕 Ngưỡng đạt CLO và báo cáo mức đạt chuẩn đầu ra

**Điểm từng CLO** tính bằng trung bình có trọng số của các thành phần đo CLO đó:

|      CLO      | Thành phần đo                                          | Công thức                   |      Ví dụ*(SV Nguyễn Văn A)*      |
| :------------: | --------------------------------------------------------- | ----------------------------- | :--------------------------------------: |
| **CLO1** | Chuyên cần (10) + Bài tập nhóm (5)                   | `(R1×10 + R1b×5) ÷ 15`   | (8,5×10 + 8,8×5)/15 =**8,6** ✔ |
| **CLO2** | KT viết (15) + Trắc nghiệm**khối A** (20)       | `(R2×15 + R4ᴀ×20) ÷ 35` | (6,9×15 + 7,5×20)/35 =**7,2** ✔ |
| **CLO3** | KT thực hành (20) + Trắc nghiệm**khối B** (30) | `(R3×20 + R4ʙ×30) ÷ 50` | (6,8×20 + 5,0×30)/50 =**5,7** ✔ |

*(Trọng số 20 và 30 của trắc nghiệm chính là 50% × 40% và 50% × 60% — xem Mục 7.2.)*

**Ngưỡng đánh giá:**

| Cấp                      | Ngưỡng                                                                          | Ý nghĩa                                                                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cá nhân**       | Sinh viên**đạt một CLO** khi điểm CLO đó **≥ 5,0/10**        | Dưới ngưỡng ⇒ ghi nhận để tư vấn học tập, dù điểm tổng vẫn có thể đạt                                                           |
| **Lớp học phần** | CLO được xem là**đạt** khi **≥ 70%** sinh viên đạt CLO đó | Dưới ngưỡng ⇒ giảng viên**rà lại nội dung, phương pháp dạy và đề thi** của phần tương ứng, ghi vào báo cáo cải tiến |

> 📌 **Vì sao cần mục này.** Đề cương gốc có ma trận CLO và có rubric, nhưng **không nói cách nào ra được con số "mức đạt CLO"** — trong khi đây chính là dữ liệu mà kiểm định chương trình *(AUN-QA, Thông tư 17/2021)* yêu cầu để chứng minh vòng lặp cải tiến **PDCA**. Ba công thức trên biến điểm thành phần sẵn có thành báo cáo CLO mà **không cần thu thập thêm dữ liệu gì**.

---

### 7.6. 🆕 Phiếu chấm mẫu *(in dùng trên lớp)*

**Phiếu chấm Rubric 3 — Bài kiểm tra thực hành**

| Họ tên: …………………………… | Lớp: ………… | MSSV: ………… |
| -------------------------------- | -------------- | -------------- |

| Tiêu chí                                                                      | TS | ☐ 0% | ☐ 25% | ☐ 50% | ☐ 75% |       ☐ 100%       | Điểm |
| ------------------------------------------------------------------------------- | :-: | :---: | :----: | :----: | :----: | :-----------------: | :----: |
| 3.1. Quy tắc nghiệp vụ*(nêu …… / N = …… quy tắc)*                    | 20 |  ☐  |   ☐   |   ☐   |   ☐   |         ☐         |  ……  |
| 3.2. Thiết kế ER và ánh xạ                                                 | 40 |  ☐  |   ☐   |   ☐   |   ☐   |         ☐         |  ……  |
| 3.3. Ràng buộc toàn vẹn & chuẩn hóa                                       | 30 |  ☐  |   ☐   |   ☐   |   ☐   |         ☐         |  ……  |
| 3.4. Thuyết minh & bảo vệ quyết định*(giải thích …… quyết định)* | 10 |  ☐  |   ☐   |   ☐   |   ☐   |         ☐         |  ……  |
|                                                                                 |    |      |        |        |        | **TỔNG /10** |  ……  |

*Nhận xét của giảng viên:* ………………………………………………………………………

**Phiếu đánh giá đồng đẳng — Bài tập nhóm** *(mỗi sinh viên nộp 1 phiếu, không công khai)*

| Nhóm: ………… | Người đánh giá: …………………………… | Số thành viên n = ……… |
| --------------- | ------------------------------------------- | --------------------------- |

| Họ tên thành viên*(kể cả bản thân)* | Điểm phân bổ*(tổng = 100)* |
| --------------------------------------------- | :-------------------------------: |
| …………………………………                    |              ………              |
| …………………………………                    |              ………              |
| …………………………………                    |              ………              |
| …………………………………                    |              ………              |
| **TỔNG**                               |           **100**           |

*Bạn cho ai điểm cao nhất? Vì sao:* ……………………………………………………………

*Bạn cho ai điểm thấp nhất? Vì sao:* ……………………………………………………………

---

## 8. 🆕 KẾ HOẠCH VÀ NỘI DUNG GIẢNG DẠY *(làm lại v2 — 5 chương, không tách chuyên đề)*

> **Nguyên tắc thiết kế khung:** ① mỗi chương **trọn tuần** để dễ xếp lịch; ② nội dung hai chuyên đề cũ *(chuẩn hóa – phụ thuộc hàm; phép tách – thuật toán nâng cao)* **đã tích hợp vào Chương 5**; ③ nội dung nâng cao cần thiết từ [3] Coronel & Morris **đã đưa thẳng vào các mục tương ứng** — không tách phần "đào sâu" riêng.

### 📅 Bảng tổng quan phân bổ

| Tuần | Chương                                                                     |  Số tiết  | CLO              |
| :---: | ---------------------------------------------------------------------------- | :----------: | ---------------- |
|   1   | **Chương 1.** Tổng quan về cơ sở dữ liệu                       |      4      | CLO2             |
| 2–3 | **Chương 2.** Mô hình thực thể–liên kết (ER) và ER mở rộng |      8      | CLO2, CLO3       |
| 4–5 | **Chương 3.** Mô hình dữ liệu quan hệ và các phép toán      |      8      | CLO2, CLO3       |
| 6–7 | **Chương 4.** Ràng buộc toàn vẹn                                 |      8      | CLO2, CLO3       |
| 8–10 | **Chương 5.** Lý thuyết thiết kế CSDL quan hệ (chuẩn hóa)     |      12      | CLO2, CLO3       |
|  11  | **Ôn tập – Tổng hợp – Bài tập nhóm**                          |      5      | CLO1, CLO2, CLO3 |
|      | **TỔNG**                                                              | **45** |                  |

### 📖 Nội dung chi tiết theo chương

#### **CHƯƠNG 1: TỔNG QUAN VỀ CƠ SỞ DỮ LIỆU** *(4 tiết · CLO2)*

| Nội dung                                                                                                                                                                                                                                                                   | Tiết |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---: |
| 1.1. Dữ liệu và thông tin · Tháp DIKW · Khái niệm CSDL và**metadata**                                                                                                                                                                                       |  1.0  |
| 1.2. Hệ quản trị CSDL (DBMS) · Phân biệt CSDL – DBMS – hệ CSDL                                                                                                                                                                                                     |  0.5  |
| 1.3. Vì sao cần CSDL —**bốn hạn chế của hệ thống tệp** và chuỗi nhân quả *(dư thừa → dị thường → quyết định sai)*                                                                                                                           |  1.0  |
| 1.4. Mô hình dữ liệu ·**Lược đồ (schema) và thể hiện (instance)**                                                                                                                                                                                         |  0.5  |
| 1.5.**Kiến trúc ba mức ANSI/SPARC** và tính độc lập dữ liệu (logic · vật lý)                                                                                                                                                                             |  0.5  |
| 1.6. Các ngôn ngữ CSDL (DDL/DML/DQL/DCL) · Giao dịch và**ACID** *(mức nhận biết)* · Chức năng, thành phần của DBMS · **Từ điển dữ liệu** trong DBMS thực tế (`INFORMATION_SCHEMA`) — *giảng viên demo trên lớp* *[3, Ch.1]* |  0.5  |

- **Hoạt động dạy:** thuyết giảng · đặt vấn đề bằng tình huống *Trung tâm Anh ngữ ABC* · thảo luận *"Excel có phải CSDL không?"* · **demo DBMS của giảng viên** (tạo CSDL mẫu, xem từ điển dữ liệu) — sinh viên quan sát
- **Hoạt động học:** nghe, ghi chép, tham gia thảo luận, làm bài tập nhanh
- **Đánh giá:** quan sát chuyên cần *(Rubric 1)*

#### **CHƯƠNG 2: MÔ HÌNH ER VÀ ER MỞ RỘNG** *(8 tiết · CLO2, CLO3)*

| Nội dung                                                                                                                                                                                                                                      | Tiết |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---: |
| 2.1. Quá trình thiết kế CSDL ·**Quy tắc nghiệp vụ** và tiêu chí "đếm được"                                                                                                                                               |  1.0  |
| 2.2. Thực thể ·**Bốn loại thuộc tính** · Xử lý **thuộc tính đa trị**                                                                                                                                                 |  1.5  |
| 2.3. Khóa/định danh · Hai tiêu chí bắt buộc của khóa · Khóa**tự nhiên** vs khóa **thay thế (surrogate)** — cách chọn *[3, Ch.5]*                                                                              |  0.5  |
| 2.4. Liên kết · ⭐**Kỹ thuật hỏi hai chiều** xác định 1:1 / 1:M / M:N                                                                                                                                                          |  1.0  |
| 2.5. Kết nối ·**Lực lượng** · **Sự tham gia** (tùy chọn/bắt buộc)                                                                                                                                                      |  1.0  |
| 2.6. Bậc liên kết ·**Liên kết đệ quy** · Thực thể **mạnh/yếu** · **Thực thể kết hợp** (tách M:N)                                                                                                          |  1.5  |
| 2.7. 🆕**Mô hình ER mở rộng (EER)**: thực thể **cha/con** (supertype/subtype) · phân cấp chuyên biệt hóa · **kế thừa** · ràng buộc **rời nhau/chồng lấn**, **đầy đủ/không đầy đủ** |  1.0  |
| 2.8. Quy trình 5 bước vẽ ERD · Ký pháp**Chen / Crow's Foot** · Sơ lược **UML class diagram**                                                                                                                            |  0.5  |

- **Hoạt động dạy:** thuyết giảng · làm mẫu **hỏi hai chiều** trên bảng · tổ chức **"phòng thiết kế"** (nhóm vẽ ERD, gallery walk phản biện chéo)
- **Hoạt động học:** vẽ ERD theo nhóm · phản biện chéo · làm bài tập cá nhân
- **Đánh giá:** quan sát hoạt động nhóm *(Rubric 1b)* · chấm bài tập ERD

#### **CHƯƠNG 3: MÔ HÌNH DỮ LIỆU QUAN HỆ VÀ CÁC PHÉP TOÁN** *(8 tiết · CLO2, CLO3)*

| Nội dung                                                                                                                                                                  | Tiết |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---: |
| 3.1. Quan hệ, bộ, thuộc tính, miền giá trị ·**Tám đặc trưng** của bảng quan hệ                                                                        |  1.0  |
| 3.2.**Phụ thuộc hàm** (X → Y) và tính có chiều · Siêu khóa – khóa dự tuyển – khóa chính – khóa ngoại                                            |  1.5  |
| 3.3.**Toàn vẹn thực thể** và **toàn vẹn tham chiếu** · Vì sao PK cấm null còn FK cho phép                                                         |  1.0  |
| 3.4. ⭐**Bốn quy tắc ánh xạ ER → quan hệ** (QT1–QT4) · Xử lý thực thể yếu và M:N                                                                       |  1.5  |
| 3.5.**Đại số quan hệ** — phép chọn σ, chiếu π                                                                                                              |  1.0  |
| 3.6. Phép toán tập hợp ∪, ∩, −, × · Điều kiện**khả hợp**                                                                                               |  1.0  |
| 3.7.**Phép kết ⋈** (tự nhiên, bằng, trong/ngoài) · Ứng dụng **kết ngoài dò lỗi toàn vẹn tham chiếu** *[3, Ch.3]* · **Phép chia ÷** |  1.0  |

- **Hoạt động dạy:** thuyết giảng · **làm sai để thấy vì sao** (khóa ngoại đặt nhầm bên) · giải mẫu biểu thức đại số quan hệ
- **Hoạt động học:** đổi ERD giữa các nhóm để **ánh xạ chéo** · luyện viết đại số quan hệ
- **Đánh giá:** **Bài kiểm tra viết 15%** *(Rubric 2 — tuần 5)*

#### **CHƯƠNG 4: RÀNG BUỘC TOÀN VẸN** *(8 tiết · CLO2, CLO3)*

| Nội dung                                                                                                                                                                                                                                                                                                             | Tiết |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---: |
| 4.1. Khái niệm**RBTV** · Vì sao đặt ràng buộc ở **tầng CSDL** thay vì chỉ ở ứng dụng                                                                                                                                                                                                       |  1.0  |
| 4.2.**Ba yếu tố** của một RBTV: điều kiện · bối cảnh · **bảng tầm ảnh hưởng**                                                                                                                                                                                                             |  1.5  |
| 4.3. ⭐**Lập bảng tầm ảnh hưởng** — quy tắc *"ĐÚNG thành SAI"* · Câu thần chú **"Thêm ở CON, Xóa ở CHA"**                                                                                                                                                                            |  1.5  |
| 4.4.**Hành động khi vi phạm**: từ chối · CASCADE · SET NULL — cách chọn theo **nghiệp vụ** · *Đọc hiểu* cú pháp khai báo `CHECK`, `NOT NULL`, `UNIQUE`, `FOREIGN KEY … ON DELETE` — **giảng viên minh họa**, không yêu cầu sinh viên viết SQL *[3, Ch.3]* |  1.0  |
| 4.5. RBTV bối cảnh**một quan hệ**: miền giá trị · liên thuộc tính · liên bộ                                                                                                                                                                                                                       |  1.0  |
| 4.6. RBTV bối cảnh**nhiều quan hệ**: khóa ngoại · liên thuộc tính liên QH · liên bộ liên QH · Giới thiệu **trigger** cho ràng buộc liên bộ liên quan hệ                                                                                                                           |  1.0  |
| 4.7. 🆕**Thực hành phát hiện RBTV** trên bài toán thực tế — bộ 6 loại đầy đủ · **"cờ đỏ thiết kế"** *(RBTV khó ⇒ thiết kế cần cải thiện)*                                                                                                                                  |  1.0  |

- **Hoạt động dạy:** thuyết giảng · suy luận **từng ô** bảng tầm ảnh hưởng cùng lớp · thảo luận *"CSDL hay ứng dụng?"*
- **Hoạt động học:** đóng vai **"đội thanh tra dữ liệu"** — săn RBTV trên lược đồ nhóm khác
- **Đánh giá:** chấm bảng tầm ảnh hưởng · chuẩn bị cho KT thực hành

#### **CHƯƠNG 5: LÝ THUYẾT THIẾT KẾ CSDL QUAN HỆ (CHUẨN HÓA)** *(12 tiết · CLO2, CLO3)*

> 📌 **Đã tích hợp trọn vẹn nội dung hai chuyên đề cũ**: *"Chuẩn hóa lược đồ, phụ thuộc hàm"* và *"Phép tách lược đồ, thuật toán nâng cao"*.

| Nội dung                                                                                                                                                                                       | Tiết |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---: |
| 5.1. Thế nào là một CSDL**"tốt"** — định nghĩa **đo được** · Vị trí của chuẩn hóa trong quy trình thiết kế                                                    |  0.5  |
| 5.2.**Ba loại phụ thuộc hàm**: đầy đủ · **bộ phận** · **bắc cầu**                                                                                               |  1.0  |
| 5.3.**Hệ luật dẫn Armstrong** (3 luật gốc + 3 luật dẫn xuất)                                                                                                                      |  1.0  |
| 5.4. ⭐**Bao đóng `X⁺`** — thuật toán · hai công dụng · phân biệt với `F⁺`                                                                                              |  1.5  |
| 5.5. ⭐**Thuật toán tìm khóa** (TN – TG) · Tìm **tất cả** khóa                                                                                                            |  2.0  |
| 5.6.**Phủ tối thiểu** — ba điều kiện · thuật toán ba bước *(nội dung chuyên đề cũ)*                                                                                    |  1.5  |
| 5.7.**Các dạng chuẩn 1NF · 2NF · 3NF** · Câu thần chú *"the key, the whole key, and nothing but the key"*                                                                      |  1.5  |
| 5.8.**Phép tách lược đồ** — **bảo toàn thông tin** (lossless join) và **bộ giả** · bảo toàn phụ thuộc hàm *(nội dung chuyên đề cũ)*                 |  1.5  |
| 5.9.**Quy trình chuẩn hóa hoàn chỉnh** — ví dụ tổng hợp từ bảng phẳng về 3NF                                                                                                |  1.0  |
| 5.10. 🆕**Dạng chuẩn mức cao**: **BCNF** *(so sánh với 3NF)* · giới thiệu **4NF** · **Phi chuẩn hóa (denormalization)** — khi nào hợp lý *[3, Ch.6]* |  0.5  |

- **Hoạt động dạy:** thuyết giảng · giải mẫu **từng thuật toán** trên bảng · tổ chức **"bệnh viện lược đồ"** (nhóm chẩn đoán – điều trị – tái khám)
- **Hoạt động học:** luyện bao đóng, tìm khóa, phủ tối thiểu · chuẩn hóa lược đồ theo nhóm · phản biện chéo
- **Đánh giá:** chấm bài tập chuẩn hóa *(thường xuyên)* — nội dung chương này được đo chính thức ở **KT thực hành tuần 11** *(Rubric 3)* và **trắc nghiệm cuối kỳ**

#### **ÔN TẬP – TỔNG HỢP – BÀI TẬP NHÓM** *(5 tiết · CLO1, CLO2, CLO3)*

| Nội dung                                                                                                                           | Tiết |
| ----------------------------------------------------------------------------------------------------------------------------------- | :---: |
| Hệ thống hóa**toàn bộ quy trình thiết kế**: quy tắc nghiệp vụ → ERD → ánh xạ → RBTV → chuẩn hóa            |  1.0  |
| **Bài tập nhóm tổng hợp** — thiết kế trọn vẹn một CSDL từ đề bài thực tế · trình bày · phản biện chéo |  2.0  |
| ✏️**BÀI KIỂM TRA THỰC HÀNH — 20%** *(thiết kế trên giấy · Rubric 3)*                                            |  1.5  |
| Giải đáp – định hướng ôn thi cuối kỳ                                                                                     |  0.5  |

- **Hoạt động dạy:** hệ thống hóa bằng **sơ đồ một trang** *(business rules → ERD → quan hệ → RBTV → 3NF)* · tổ chức phản biện chéo · coi kiểm tra
- **Hoạt động học:** hoàn thiện sản phẩm nhóm · trình bày & phản biện · làm bài kiểm tra thực hành
- **Đánh giá:** **Bài tập nhóm 5%** *(Rubric 1b)* · ✏️ **Bài kiểm tra thực hành 20%** *(Rubric 3)*

---

## 9. 🆕 KẾ HOẠCH TỰ HỌC *(90 tiết — có cấu trúc)*

> Khắc phục điểm yếu *"90 tiết tự học không có thiết kế"*. Tỷ lệ chuẩn: **1 tiết lên lớp ⇒ 2 tiết tự học**.
>
> ⚠️ **Nguyên tắc thiết kế nhiệm vụ:** mọi nhiệm vụ chỉ cần **giấy bút** và **công cụ vẽ sơ đồ miễn phí** (draw.io) — **KHÔNG yêu cầu cài đặt hay sử dụng DBMS/SQL**, vì các kỹ năng đó thuộc học phần *Hệ quản trị CSDL* kế tiếp mà sinh viên **chưa học**. Phần thao tác trên DBMS do **giảng viên demo trên lớp** để minh họa.
>
> ✏️ **Các sản phẩm nộp dưới đây được tính điểm** qua tiêu chí *"Chủ động học tập"* của **Rubric 1** *(30% của thành phần chuyên cần)*. Trước đây bảng này yêu cầu nộp bài hằng tuần nhưng **không gắn với thành phần điểm nào** — sinh viên không có động lực thực hiện.

| Tuần | Nhiệm vụ tự học                                                                                                                                                                                                                                                                                         | Sản phẩm nộp                                                                   |    Tiết    |
| :---: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | :----------: |
|   1   | Đọc [1] chương mở đầu; [3] Ch.1. Chọn một bảng dữ liệu quen thuộc (danh bạ, bảng điểm…),**lập bảng metadata trên giấy** (tên cột · kiểu · bắt buộc? · ràng buộc). Phân tích một **bảng phẳng** cho trước: chỉ ra dư thừa và **3 dị thường** | Bảng metadata + bài phân tích dị thường                                    |      8      |
|   2   | Đọc [3] Ch.4 (mục 4.1). Vẽ lại**ERD Trung tâm ABC** bằng draw.io                                                                                                                                                                                                                               | File PNG sơ đồ ERD                                                             |      8      |
|   3   | Đọc [3] Ch.5 (EER). Làm**bài tập ERD thư viện** *(quy tắc nghiệp vụ → bảng hỏi hai chiều → ERD)*                                                                                                                                                                                     | Bài tập ERD + thuyết minh                                                      |      8      |
|   4   | Đọc [1] chương mô hình quan hệ; [3] Ch.3 (3.1–3.4).**Ánh xạ** ERD thư viện sang lược đồ quan hệ                                                                                                                                                                                      | Lược đồ quan hệ có PK/FK                                                    |      8      |
|   5   | Luyện**đại số quan hệ** (10 biểu thức). **Kiểm tra toàn vẹn trên giấy**: với bộ dữ liệu mẫu cho trước của 7 bảng ABC, chỉ ra thao tác nào **vi phạm toàn vẹn tham chiếu** và giải thích                                                                    | Bài tập đại số quan hệ + bài kiểm tra toàn vẹn                          |      8      |
|   6   | Đọc [1] chương RBTV; [2] phần toàn vẹn.**Phát hiện ≥ 8 RBTV** trên lược đồ thư viện                                                                                                                                                                                                  | Bảng 8 RBTV đủ 6 loại                                                         |      8      |
|   7   | Lập**bảng tầm ảnh hưởng** cho 3 RBTV; đề xuất hành động cho mọi khóa ngoại                                                                                                                                                                                                             | Bảng tầm ảnh hưởng + lý do nghiệp vụ                                      |      8      |
|   8   | Đọc [3] Ch.6 (6.1–6.3); [2] phần phụ thuộc hàm. Luyện**bao đóng & tìm khóa**                                                                                                                                                                                                              | Bài tập 5 câu                                                                  |      8      |
|   9   | Luyện**phủ tối thiểu** và **xác định dạng chuẩn**                                                                                                                                                                                                                                     | Bài tập 5 câu                                                                  |      8      |
|  10  | **Chuẩn hóa lược đồ thư viện** về 3NF; chứng minh phép tách bảo toàn thông tin                                                                                                                                                                                                         | Bài tổng hợp — ✏️*bài tập dượt cho **KT thực hành tuần 11*** |      10      |
|  11  | Ôn tập tổng hợp; chuẩn bị bài tập nhóm;**ôn cho KT thực hành**                                                                                                                                                                                                                            | Sản phẩm nhóm                                                                  |      8      |
|      | **TỔNG**                                                                                                                                                                                                                                                                                             |                                                                                   | **90** |

---

## 10. Tài liệu học tập (Learning Resources)

**Giáo trình chính:**

- **[1]** Nguyễn Tuệ (2009).  *Giáo trình nhập môn hệ cơ sở dữ liệu* . NXB
  Giáo dục.

**Tài liệu tham khảo:**

- **[2]** Vũ Đức Thi (1997). *Cơ sở dữ liệu — kiến thức và thực hành*. NXB Thống kê.
- **[3]** Coronel, C. & Morris, S. *Database Systems: Design, Implementation & Management*. Cengage Learning. — 🆕 *nguồn cho các nội dung nâng cao đã tích hợp: Ch.1 (khái niệm, từ điển dữ liệu), Ch.3 (mô hình quan hệ, ràng buộc), Ch.4 (ER), **Ch.5 (EER, chọn khóa thay thế)**, **Ch.6 (chuẩn hóa, BCNF, 4NF, phi chuẩn hóa)***

**Học liệu khác:**

- Tập bài giảng học phần *(5 chương, có hình vẽ minh họa)* và bộ slide bài giảng.
- Công cụ: **draw.io** *(vẽ ERD, miễn phí — sinh viên sử dụng)* · MySQL Workbench / SSMS *(chỉ dùng cho **demo của giảng viên** trên lớp — sinh viên **không bắt buộc** cài đặt)*.

---

## 11. Chính sách học phần

- **Liêm chính học thuật:** bài tập thiết kế nộp về nhà phải là sản phẩm của cá nhân/nhóm; nêu rõ mức độ được phép sử dụng công cụ hỗ trợ/AI.
- **Nộp bài:** bài tập tự học nộp **đầu buổi học tuần kế tiếp**; nộp muộn trừ điểm theo quy định.
- **Vắng học, thi lại, khiếu nại điểm:** theo quy chế đào tạo của Trường.

---

*Đà Nẵng, ngày … tháng … năm 2026*

| Trưởng khoa   | Trưởng bộ môn  | Người biên soạn                 |
| --------------- | ------------------ | ----------------------------------- |
| Trần Mạnh Huy | Nguyễn Văn Hưng | **Nguyễn Tất Phú Cường** |

---

## PHỤ LỤC A — Bảng đối chiếu THAY ĐỔI so với đề cương gốc

| # | Nội dung gốc                                                                        | Thay đổi ở bản v2                                                                                                                                       | Lý do                                                                                                                |
| :-: | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1 | Mô tả có**SQL**, *phép tính vị từ*                                     | **Bỏ SQL** khỏi mô tả; giữ đại số quan hệ                                                                                                    | SQL học ở học phần**Hệ quản trị CSDL**                                                                   |
| 2 | **CO4 / CLO4** (an toàn, giao dịch, Client‑Server)                           | **Bỏ**; phần *toàn vẹn* gộp vào **CLO3**                                                                                                | Nội dung hoãn sang học phần sau; tránh**CLO mồ côi**                                                     |
| 3 | **Chương 6** (Client‑Server) — *bỏ trống*                               | **Bỏ hẳn**                                                                                                                                          | Không đủ thời lượng; thuộc học phần sau                                                                      |
| 4 | *"An toàn & toàn vẹn dữ liệu"* chung một chương                             | Tách: giữ**toàn vẹn** *(Ch4)*, bỏ *an toàn*                                                                                                 | An toàn thuộc học phần sau                                                                                        |
| 5 | **Hai chuyên đề** tách riêng (8 tiết)                                     | 🆕**Tích hợp vào Chương 5**                                                                                                                      | *Theo yêu cầu — nội dung liền mạch hơn*                                                                      |
| 6 | Tổng số tiết**không khớp 45**                                              | **Cân lại đủ 45 tiết**, nhịp **4 tiết/tuần**                                                                                            | Khớp Mục 2.5                                                                                                        |
| 7 | Trắc nghiệm có khối**Client‑Server**                                       | **Bỏ**; còn 2 khối *(CLO2 40% · CLO3 60%)*                                                                                                      | Đồng bộ với CLO                                                                                                   |
| 8 | **Rubric 3** trùng mức 25% và 50%                                            | **Sửa lại**; thêm tiêu chí *"bảo vệ quyết định thiết kế"*                                                                               | Lỗi kỹ thuật; tăng độ đo được                                                                               |
| 9 | **Rubric 2** tiêu chí *"phân tích, liên hệ"*                            | Đổi thành**"giải thích bằng ví dụ tự nêu"**                                                                                                 | Đo đúng mức Bloom; chống học vẹt                                                                               |
| 10 | Không có**bài tập nhóm** đo CLO1                                          | 🆕 Thêm**5%** + **Rubric 1b**                                                                                                                  | CLO1 nêu*"hợp tác nhóm"* nhưng chỉ đo bằng chuyên cần                                                     |
| 11 | **90 tiết tự học** không có thiết kế                                     | 🆕**Mục 9** — kế hoạch tự học theo tuần, có sản phẩm nộp                                                                                   | Điểm yếu kiểm định                                                                                              |
| 12 | Không có**ma trận CLO ↔ Chương**                                          | 🆕**Mục 6.1**                                                                                                                                        | Chứng minh constructive alignment                                                                                    |
| 13 | Học liệu chỉ có [1], [2]*(1997, 2005)*                                          | 🆕 Bổ sung**[3] Coronel & Morris**                                                                                                                   | Cập nhật; nguồn cho nội dung nâng cao                                                                            |
| 14 | Không có mục**chính sách học phần**                                      | 🆕**Mục 11** *(liêm chính học thuật/AI)*                                                                                                       | Chuẩn mực hiện hành                                                                                               |
| 15 | Nội dung chi tiết chia**theo tuần**, có dòng *"đào sâu"* tách riêng | 🆕 Chi tiết tổ chức**theo chương**; nội dung nâng cao **hòa vào đúng đề mục**, phần không thiết yếu **đã lược bỏ** | *Theo yêu cầu — tránh phụ lục rời, dễ tra cứu khi soạn bài*                                              |
| 16 | Nhiệm vụ tự học yêu cầu**cài đặt DBMS, tạo bảng, chụp màn hình**  | 🆕 Thay bằng nhiệm vụ**thiết kế trên giấy / draw.io**; thao tác DBMS chuyển thành **demo của giảng viên** *(bổ sung Mục 2.14)* | Sinh viên**chưa học SQL / Hệ quản trị CSDL** — nhiệm vụ cũ vượt nền tảng, **bất khả thi** |

### ✏️ Bổ sung sau đợt **rà soát rubric**

| # | Vấn đề phát hiện                                                                                                                                                                             | Xử lý                                                                                                                                        |            Mức            |
| :-: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------: |
| 17 | **KT thực hành đặt ở tuần 8** nhưng Rubric 3 chấm *chuẩn hóa* và *chứng minh phép tách* — nội dung dạy ở **tuần 9–10** ⇒ **kiểm tra thứ chưa dạy** | Chuyển sang**tuần 11**; cân lại 5 tiết tuần 11 để chứa 1,5 tiết kiểm tra                                                      | 🔴**Nghiêm trọng** |
| 18 | **Rubric 1 không được viết ra** *(chỉ ghi "giữ nguyên đề cương gốc")* và **thiếu phủ CLO1** — không đo *"chủ động học tập"*                               | Viết đầy đủ**3 tiêu chí × 5 mức**; thêm tiêu chí **"chủ động học tập"** (30) gắn với sản phẩm tự học Mục 9 |          🟠 Lớn          |
| 19 | **90 tiết tự học có sản phẩm nộp nhưng không gắn với thành phần điểm nào**; Mục 9 tuần 10 lại ghi *"(3 điểm)"* **mồ côi**                                    | Sản phẩm tự học nay tính qua**Rubric 1**; bỏ *"(3 điểm)"*, đổi thành **bài tập dượt** cho KT thực hành          |          🟠 Lớn          |
| 20 | **Rubric 2** tiêu chí 1 có **khoảng trống thang đo**: bài đúng **50–59%** không thuộc mức nào                                                                     | Chia dải liền mạch**<30 / 30–49 / 50–69 / 70–89 / ≥90**                                                                           |          🟠 Lớn          |
| 21 | **Mục 6.1 mâu thuẫn Mục 7.2**: ma trận ghi bài tập nhóm đo **cả 3 CLO**, nhưng Rubric 1b **không chấm chất lượng chuyên môn**                                 | Sửa dòng*Ôn tập* — ghi đúng công cụ cho từng CLO                                                                                   |          🟡 Vừa          |
| 22 | **Rubric 1b chỉ có 3 mức** trong khi các rubric khác 5 mức ⇒ điểm **nhảy bậc thô**                                                                                        | Mở thành**5 mức** 0/25/50/75/100                                                                                                      |          🟡 Vừa          |
| 23 | **Rubric 3** tiêu chí 1 & 4 mô tả **không đo được** *("đáp ứng phần lớn yêu cầu")*; tiêu chí *"bảo vệ"* không có chỗ để bảo vệ trên bài viết        | Neo mọi mức bằng**tỷ lệ đếm được / lỗi cụ thể**; thêm **ghi chú ra đề** bắt buộc                                |          🟡 Vừa          |
| 24 | **Rubric 4** thiếu đặc tả; **30/50 điểm CLO3 đo bằng trắc nghiệm** trong khi CLO3 ở mức *Phân tích* ⇒ nguy cơ **lệch constructive alignment**                | Bổ sung**ma trận đề**; quy định khối B phải là **câu hỏi tình huống có dữ kiện**                                   |          🟡 Vừa          |

## PHỤ LỤC B — Checklist còn lại

- [ ] **Điền ma trận CLO ↔ PLO** (Mục 6) cho 3 CLO; kiểm tra **không hụt phủ PLO** khi bỏ CLO4.
- [ ] Rà **đánh số bảng** toàn văn bản *(đề cương gốc thiếu "Bảng 4")*.
- [ ] ✏️ **Xác nhận với Khoa:** KT thực hành đã chuyển sang **tuần 11** *(vì tuần 8 chưa dạy xong chuẩn hóa)*. Nếu quy chế buộc *"đánh giá giữa học phần"* phải nằm ở nửa đầu, chọn phương án thay thế nêu tại Mục 7.2. KT viết giữ **tuần 5**.
- [ ] ✏️ **Khi ra đề KT thực hành:** đáp án phải **liệt kê sẵn N quy tắc nghiệp vụ** *(8–12)* và đề phải có **câu thuyết minh bắt buộc** — nếu thiếu, tiêu chí 1 và 4 của Rubric 3 **không dùng được**.
- [ ] ✏️ **Khi ra đề trắc nghiệm:** khối B (60%, đo CLO3) phải là **câu hỏi có dữ kiện để suy luận**, không hỏi tái hiện định nghĩa.
- [ ] Cân nhắc bổ sung **giáo trình tiếng Việt cập nhật** nếu Khoa yêu cầu.
