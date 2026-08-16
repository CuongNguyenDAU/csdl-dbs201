**BỘ GIÁO DỤC VÀ ĐÀO TẠO** — **TRƯỜNG ĐẠI HỌC KIẾN TRÚC ĐÀ NẴNG**

**CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM — Độc lập – Tự do – Hạnh phúc**

# ĐỀ CƯƠNG CHI TIẾT HỌC PHẦN *(Syllabus)*

*(Ban hành kèm theo Quyết định số 346/QĐ-ĐHKTĐN ngày 25 tháng 06 năm 2024 của Hiệu trưởng Trường Đại học Kiến trúc Đà Nẵng)*

---

## 1. Thông tin chung *(General Information)*

| Mục | Nội dung |
|:--|:--|
| 1.1. Trình độ đào tạo *(Level)* | Đại học (Undergraduate) |
| 1.2. Chương trình đào tạo *(Program)* | Công nghệ thông tin (Information Technology) |

## 2. Thông tin chung học phần *(Course Information)*

| Mục | Nội dung |
|:--|:--|
| 2.1. Tên học phần | Cơ sở dữ liệu — *Database Systems* |
| 2.2. Mã học phần | DBS201 |
| 2.3. Nhóm học phần | Cơ sở ngành |
| 2.4. Số tín chỉ | 3,0 |
| 2.5. Phân phối thời gian | **135 tiết** — Lý thuyết: 45; Đồ án: 0; Thực hành/Thí nghiệm: 0; Tự học: 90 |
| 2.6. Số tuần thực hiện | 11 tuần — *nhịp 4 tiết/tuần, riêng tuần 11: 5 tiết — mỗi chương trọn tuần để dễ xếp lịch* |
| 2.7. Niên khóa áp dụng | 2026-2031; 2027-2032 |
| 2.8. Giảng viên phụ trách chính | Nguyễn Tất Phú Cường |
| — Giảng viên cùng giảng dạy | Phạm Thị Dung |
| 2.9. Khoa/Bộ môn phụ trách giảng dạy | Công nghệ thông tin |
| 2.10. Khoa/Bộ môn quản lý | Công nghệ thông tin |
| 2.11. Nơi tiến hành học phần | Phòng học lý thuyết |
| 2.12. Loại học phần | Bắt buộc |
| 2.13. Điều kiện tham gia | *Tiên quyết:* không — *Học trước:* (BIN101) Tin học cơ bản — *Song hành:* không |
| 2.14. Giả định về nền tảng người học | Sinh viên **chỉ mới học Tin học cơ bản**, **chưa học SQL hay hệ quản trị cơ sở dữ liệu**. Vì vậy mọi bài tập, bài đánh giá và nhiệm vụ tự học của học phần chỉ đòi hỏi **tư duy thiết kế trên giấy** và **công cụ vẽ sơ đồ miễn phí** (draw.io); phần thao tác trên hệ quản trị CSDL chỉ xuất hiện dưới dạng **demo minh họa của giảng viên** trên lớp, sinh viên không phải cài đặt phần mềm nào.<br><br>Học phần tập trung vào **THIẾT KẾ ĐÚNG** — nền móng cho mọi hệ thống dữ liệu. Ngôn ngữ SQL, an toàn – bảo mật và quản lý giao dịch được bố trí ở học phần **Hệ quản trị cơ sở dữ liệu** kế tiếp; đề cương này không lấn sang phần đó. |

## 3. Mô tả vắn tắt học phần *(Course Description)*

Học phần Cơ sở dữ liệu trang bị nền tảng mô hình hóa và thiết kế cơ sở dữ liệu, gồm: các khái niệm cơ bản của một hệ cơ sở dữ liệu và kiến trúc ba mức; mô hình thực thể–liên kết (ER) và mô hình ER mở rộng (EER); mô hình dữ liệu quan hệ và đại số quan hệ; ràng buộc toàn vẹn dữ liệu; lý thuyết thiết kế — phụ thuộc hàm, các dạng chuẩn (1NF–BCNF) và kỹ thuật chuẩn hóa lược đồ quan hệ. Toàn bộ nội dung được tổ chức thành năm chương, mỗi chương trọn tuần, khép lại bằng một tuần ôn tập – tổng hợp có bài tập nhóm thiết kế trọn vẹn một cơ sở dữ liệu từ đề bài thực tế.

> 📌 Ngôn ngữ SQL, an toàn – bảo mật và quản lý giao dịch được bố trí ở học phần Hệ quản trị cơ sở dữ liệu kế tiếp; học phần này tập trung vào THIẾT KẾ ĐÚNG — nền móng cho mọi hệ thống dữ liệu.

Về bộ chuẩn đầu ra: CO4/CLO4 của bản đề cương gốc (an toàn, giao dịch, kiến trúc Client–Server) đã được bỏ và phần *toàn vẹn dữ liệu* gộp vào CLO3, do nội dung ấy hoãn sang học phần sau; ma trận CLO ↔ PLO ở mục 6 đã được rà để đóng góp của CLO4 cũ chuyển sang CLO2 và CLO3, tránh hụt phủ PLO ở cấp chương trình. Hai chuyên đề tách riêng của bản gốc (*chuẩn hóa – phụ thuộc hàm* và *phép tách – thuật toán nâng cao*) đã tích hợp trọn vẹn vào Chương 5; các nội dung nâng cao lấy từ [3] Coronel & Morris được đưa thẳng vào đề mục tương ứng, không tách thành phụ lục rời.

Một điều chỉnh về câu chữ của CLO3 cần nêu rõ để người ra đề nắm được: mệnh đề cuối của CLO3 là **"xác định một phép tách có bảo toàn thông tin hay không"** chứ không phải *"chứng minh phép tách bảo toàn thông tin"*. Lý do: nội dung Chương 4 và Chương 5 — 20/45 tiết của học phần — được đo bằng khối tình huống của đề trắc nghiệm cuối kỳ; câu hỏi trắc nghiệm có dữ kiện đo được việc sinh viên **chạy thuật toán rồi kết luận**, nhưng không đo được việc **viết ra một chứng minh**. Giữ động từ "chứng minh" thì đề cương tuyên bố một năng lực không có công cụ nào đo — vì vậy động từ được chỉnh cho khớp đúng công cụ đánh giá hiện có.

*The course provides foundations of database modeling and design: basic concepts of a database system and the three-level architecture; Entity–Relationship (ER) and Extended ER (EER) models; the relational data model and relational algebra; data integrity constraints; design theory — functional dependencies, normal forms (1NF–BCNF) and normalization techniques. Content is organised into five chapters, each occupying whole weeks, closing with a synthesis week featuring a group assignment that designs a complete database from a real-world brief. (SQL, security, and transaction management are placed in the subsequent Database Management Systems course.)*

## 4. Mục tiêu học phần *(Course Objectives – COs)*

**Bảng 1: Mục tiêu của học phần**

| COs | Mô tả *(Description)* |
|:--:|:--|
| CO1 | Nghiêm túc, chủ động, hợp tác, tuân thủ đạo đức khi nghiên cứu và áp dụng hệ cơ sở dữ liệu. |
| CO2 | Mô tả, phân tích các khái niệm, mô hình hóa dữ liệu (ER, EER, quan hệ), cơ chế lưu trữ và ràng buộc toàn vẹn dữ liệu. |
| CO3 | Thiết kế mô hình dữ liệu (ER/EER, UML), ánh xạ ER sang quan hệ, phân tích ràng buộc toàn vẹn, chuẩn hóa lược đồ và vận dụng các thuật toán thiết kế. |

## 5. Chuẩn đầu ra học phần *(Course Learning Outcomes – CLOs)*

**Bảng 2: Chuẩn đầu ra của học phần**

| CLOs | Mô tả *(Description)* | Thang đo *(Bloom's Taxonomy)* | CO1 | CO2 | CO3 |
|:--:|:--|:--:|:--:|:--:|:--:|
| CLO1 | Thể hiện tinh thần trách nhiệm và chủ động học tập: thực hiện đầy đủ, đúng hạn các nhiệm vụ tự học; tuân thủ nội quy lớp học và chuẩn mực liêm chính học thuật; hợp tác nhóm hiệu quả trong bài tập tổng hợp — nhận và hoàn thành phần việc được giao, phối hợp và tôn trọng ý kiến của thành viên khác. | Thái độ / tự chủ – trách nhiệm — Mức 3/5: Hình thành giá trị | X |  |  |
| CLO2 | Trình bày và giải thích các khái niệm của hệ cơ sở dữ liệu: dữ liệu và metadata, phân biệt CSDL – DBMS – hệ CSDL, kiến trúc ba mức và tính độc lập dữ liệu, mô hình ER và ER mở rộng, mô hình quan hệ và tám đặc trưng của bảng quan hệ, các phép toán đại số quan hệ, khái niệm ràng buộc toàn vẹn, phụ thuộc hàm và các dạng chuẩn. | Nhận thức — Mức 2/6: Hiểu |  | X |  |
| **CLO3** ◆ | Phân tích một bài toán nghiệp vụ thực tế để phát biểu quy tắc nghiệp vụ đếm được và **thiết kế mô hình ER**; **ánh xạ** mô hình ER sang lược đồ quan hệ với khóa chính, khóa ngoại và ràng buộc toàn vẹn tham chiếu; **viết biểu thức đại số quan hệ** trả lời yêu cầu truy vấn; **đánh giá tính toàn vẹn** của lược đồ, **chuẩn hóa** về 3NF và **xác định một phép tách có bảo toàn thông tin hay không**. | Nhận thức — Mức 5/6: Tổng hợp, đánh giá |  |  | X |

◆ **CLO cốt lõi** — chuẩn đầu ra đóng góp nhiều nhất vào chuẩn đầu ra của chương trình đào tạo (PLO).

## 6. Mối liên hệ giữa CLO và chuẩn đầu ra chương trình (PLO) và chỉ số PI

**Bảng 3: Ma trận đóng góp của CLO vào PLO**

> **I** *(Introduced)* giới thiệu · **R** *(Reinforced)* nâng cao, có thực hành · **M** *(Mastery)* thuần thục · **A** *(Assessment)* thu thập minh chứng đánh giá PLO.

| CLO | PLO4 | PLO6 | PLO7 | PLO9 | PI |
|:--:|:--:|:--:|:--:|:--:|:--:|
| CLO1 | R |  |  |  | PI 4.2 |
| CLO2 |  | R |  |  | PI 6.1 |
| CLO3 |  |  | M | R | PI 7.2 · PI 9.3 |

### 6.1. Ma trận CLO ↔ nội dung ↔ công cụ đánh giá *(constructive alignment)*

| Nội dung | Số tiết | CLO1 | CLO2 | CLO3 | Đánh giá bằng |
|:--|:--:|:--:|:--:|:--:|:--|
| Chương 1: Tổng quan về cơ sở dữ liệu | 4 | ✔ | ✔ |  | Quan sát chuyên cần và nội quy (Rubric 1); chấm sản phẩm tự học tuần 1; nội dung chương này thuộc khối A của đề trắc nghiệm cuối kỳ (Rubric 4) |
| Chương 2: Mô hình thực thể–liên kết (ER) và ER mở rộng | 8 | ✔ | ✔ | ✔ | Quan sát chuyên cần và hoạt động nhóm (Rubric 1); chấm bài tập ERD và sản phẩm tự học tuần 2–3; **chương này là toàn bộ phạm vi của Bài kiểm tra viết 15% (Rubric 2) tổ chức ở tuần 5** |
| Chương 3: Mô hình dữ liệu quan hệ và các phép toán | 8 |  | ✔ | ✔ | **Bài kiểm tra viết 15% (Rubric 2) tổ chức ở tuần 5, phạm vi Chương 2**; quan sát chuyên cần (Rubric 1); chấm sản phẩm tự học tuần 4–5; **chương này là mốc cuối của phạm vi Bài kiểm tra giữa học phần (Rubric 3) tổ chức ở tuần 6** |
| Chương 4: Ràng buộc toàn vẹn | 8 |  | ✔ | ✔ | **Bài kiểm tra giữa học phần 20% (Rubric 3) tổ chức đầu tuần 6, phạm vi Chương 2–3**; chấm bảng tầm ảnh hưởng và sản phẩm tự học tuần 6–7; nội dung chương này được đo ở **khối B1** của đề trắc nghiệm cuối kỳ (Rubric 4) |
| Chương 5: Lý thuyết thiết kế CSDL quan hệ (chuẩn hóa) | 12 |  | ✔ | ✔ | Chấm bài tập chuẩn hóa (thường xuyên, không tính điểm thành phần); chấm sản phẩm tự học tuần 8–10; **nội dung chương này được đo chính thức ở khối B2 của đề trắc nghiệm cuối kỳ (Rubric 4) — chiếm 25% trọng số đề** |
| Ôn tập – Tổng hợp – Bài tập nhóm | 5 | ✔ | ✔ | ✔ | **Chốt điểm Nhận thức thái độ 15% (Rubric 1)** — trong đó tiêu chí 1.4 chấm hợp tác nhóm dựa trên sản phẩm nhóm tuần này và phiếu đánh giá đồng đẳng |
| **TỔNG** | **45** |  |  |  |  |

## 7. Đánh giá học phần *(Assessment)*

### 7.1. Thang điểm đánh giá *(Grading Scale)*

Dùng **thang điểm 10** để chấm, lấy đến **1 chữ số thập phân**; quy đổi sang **điểm chữ** và **thang 4,0**.

**Bảng 5: Thang điểm đánh giá kết quả học tập**

| STT | Điểm thang 10 | Điểm chữ | Thang 4,0 | Xếp loại |
|:--:|:--|:--:|:--:|:--|
| 1 | Từ 9,5 đến 10,0 | A+ | 4,0 | Xuất sắc |
| 2 | Từ 8,5 đến dưới 9,5 | A | 4,0 | Giỏi |
| 3 | Từ 8,0 đến dưới 8,5 | B+ | 3,5 | Khá giỏi |
| 4 | Từ 7,0 đến dưới 8,0 | B | 3,0 | Khá |
| 5 | Từ 6,5 đến dưới 7,0 | C+ | 2,5 | Trung bình khá |
| 6 | Từ 5,5 đến dưới 6,5 | C | 2,0 | Trung bình |
| 7 | Từ 5,0 đến dưới 5,5 | D+ | 1,5 | Trung bình yếu |
| 8 | Từ 4,0 đến dưới 5,0 | D | 1,0 | Yếu (đạt có điều kiện) |
| 9 | Từ 0,0 đến dưới 4,0 | F | 0 | Không đạt |

### 7.2. Kế hoạch đánh giá *(Assessment Plan)*

**Bảng 6: Phương pháp, hình thức kiểm tra – đánh giá**

| Thành phần & phương pháp | Trọng số (%) | Chuẩn đầu ra (CLO) | Rubric | Thời điểm |
|:--|:--:|:--|:--:|:--|
| **Nhận thức thái độ** | **15** |  |  |  |
| — Nhận thức, thái độ học tập (chuyên cần · nội quy · hồ sơ tự học · hợp tác nhóm) | 15 | CLO1: 100% | Rubric 1 | Cả học phần, chốt tuần 11 |
| **Đánh giá thường xuyên** | **15** |  |  |  |
| — Bài kiểm tra viết — chuyển quy tắc nghiệp vụ thành mô hình ER | 15 | CLO3: 100% | Rubric 2 | 5 |
| **Đánh giá giữa học phần** | **20** |  |  |  |
| — Bài kiểm tra viết — ánh xạ mô hình ER sang lược đồ quan hệ và đại số quan hệ | 20 | CLO3: 100% | Rubric 3 | 6 |
| **Đánh giá cuối học phần** | **50** |  |  |  |
| — Bài kiểm tra trắc nghiệm theo khối kiến thức | 50 | CLO2: 60% · CLO3: 40% | Rubric 4 | 12 |

**Phủ CLO trong đánh giá:** CLO1 = **15%** · CLO2 = **30%** · CLO3 = **55%** → tổng **100%**

### 7.3. Rubric đánh giá *(Assessment Rubrics)*

| Nội dung | Quy định |
|---|---|
| Số mức chất lượng | Thống nhất **5 mức**: Kém (0%) · Yếu (25%) · Trung bình (50%) · Khá (75%) · Giỏi/Xuất sắc (100%) |
| Tổng trọng số | Mỗi rubric có tổng trọng số các tiêu chí = **100** |
| Công thức | `Điểm thành phần (thang 10) = Σ (Trọng số tiêu chí × Mức đạt) ÷ 100` — *Mức đạt* lấy 0 / 2,5 / 5,0 / 7,5 / 10,0 |
| Làm tròn | Lấy đến **1 chữ số thập phân** |
| Vắng mặt / không nộp | Tính **0 điểm** cho thành phần đó, trừ trường hợp có lý do chính đáng được Khoa chấp thuận |
| Chọn mức | Xếp vào mức **mô tả khớp nhất**; vượt hoàn toàn mức dưới nhưng chưa đủ mức trên → chọn **mức dưới** |
| Công bố | Phát rubric cho sinh viên **buổi học đầu tiên** và nhắc lại trước mỗi bài đánh giá |

#### Rubric 1 — Nhận thức thái độ · *đo **CLO1*** · trọng số học phần **15%** · cả học phần, chốt tuần 11

| Tiêu chí | TS | CLO | Kém (0%) | Yếu (25%) | Trung bình (50%) | Khá (75%) | Giỏi/Xuất sắc (100%) |
|:--|:--:|:--:|:--|:--|:--|:--|:--|
| **1.1.** Đi học đầy đủ, đúng giờ | 30 | CLO1 | Vắng hoặc trễ > 7 buổi | Vắng hoặc trễ 5–6 buổi | Vắng hoặc trễ 3–4 buổi | Vắng hoặc trễ 1–2 buổi, đều có phép | Đi học đủ mọi buổi, luôn đúng giờ |
| **1.2.** Tuân thủ nội quy, tôn trọng giảng viên và bạn học | 20 | CLO1 | Vi phạm nội quy ≥ 4 lần, phải nhắc nhở nhiều lần | Vi phạm nội quy 2–3 lần | Vi phạm nội quy 1 lần; đôi lúc mất tập trung nhưng không ảnh hưởng lớp | Không vi phạm lần nào; tập trung nghe giảng, tôn trọng ý kiến bạn học | Không vi phạm; chủ động góp phần giữ trật tự và nền nếp chung của lớp |
| **1.3.** Chủ động học tập — nộp sản phẩm tự học (11 nhiệm vụ, mục Kế hoạch tự học) | 30 | CLO1 | Nộp < 30% số nhiệm vụ (0–3 / 11) | Nộp 30–49% số nhiệm vụ (4–5 / 11) | Nộp 50–69% số nhiệm vụ (6–7 / 11) | Nộp 70–89% số nhiệm vụ (8–9 / 11), đa số đúng hạn | Nộp ≥ 90% số nhiệm vụ (10–11 / 11), đúng hạn, trình bày đúng quy ước của lớp |
| **1.4.** Hợp tác nhóm trong bài tập tổng hợp (tuần 11) | 20 | CLO1 | Không tham gia bài tập nhóm | Có tên trong nhóm nhưng đóng góp không đáng kể; không trao đổi với nhóm | Làm phần được giao ở mức tối thiểu, phải nhắc; chỉ phối hợp khi được yêu cầu | Hoàn thành đầy đủ phần được giao đúng hạn; trao đổi chủ động, tôn trọng ý kiến khác | Chủ động nhận thêm việc, chất lượng cao; điều phối hoặc hỗ trợ thành viên khác, sản phẩm nhóm thống nhất |

> Tiêu chí 1.3 là mắt xích duy nhất nối 90 tiết tự học vào điểm số — bỏ tiêu chí này thì hai phần ba khối lượng học phần không gắn với đầu điểm nào và sinh viên không có động lực thực hiện. Mẫu số là 11 nhiệm vụ công bố ở mục Kế hoạch tự học; điều chỉnh số nhiệm vụ thì phải công bố lại mẫu số trước tuần 1.

> Tiêu chí 1.4 là chỗ duy nhất đo mệnh đề "hợp tác nhóm hiệu quả" của CLO1. Bỏ tiêu chí này thì CLO1 hụt phủ: các tiêu chí còn lại chỉ đo việc đi học, nội quy và nộp bài.

> **Phiếu đánh giá đồng đẳng — bắt buộc nộp cùng sản phẩm nhóm.** Giảng viên không quan sát được phần việc mỗi thành viên làm ở nhà, nên tiêu chí 1.4 cần thêm dữ liệu từ chính nhóm: mỗi sinh viên phân bổ 100 điểm cho tất cả thành viên (kể cả bản thân) theo mức đóng góp thực tế, kèm một câu giải thích cho người được cho điểm cao nhất và thấp nhất. Tỷ lệ đóng góp của một sinh viên = trung bình cộng số điểm các bạn dành cho người đó. Mốc đối chiếu là mức chia đều 100 ÷ n. Tỷ lệ < 60% mốc thì hạ một mức; > 140% thì nâng một mức. Phiếu nộp riêng, không công khai giữa các thành viên.

> Việc vắng học vượt tỷ lệ quy định vẫn xử lý theo quy chế đào tạo của Trường, độc lập với điểm rubric này.

#### Rubric 2 — Bài kiểm tra viết — chuyển quy tắc nghiệp vụ thành mô hình ER · *đo **CLO3*** · trọng số học phần **15%** · tuần 5

| Tiêu chí | TS | CLO | Kém (0%) | Yếu (25%) | Trung bình (50%) | Khá (75%) | Giỏi/Xuất sắc (100%) |
|:--|:--:|:--:|:--|:--|:--|:--|:--|
| **2.1.** Phân tích đề bài và phát biểu quy tắc nghiệp vụ | 25 | CLO3 | Không phát biểu được quy tắc nghiệp vụ nào | Nêu < 30% số quy tắc trong đáp án | Nêu 30–59% số quy tắc; phát biểu còn mơ hồ, không đếm được | Nêu 60–84% số quy tắc; phát biểu rõ, có nêu lực lượng | Nêu ≥ 85% số quy tắc; chính xác, đủ lực lượng và ràng buộc bắt buộc / tùy chọn |
| **2.2.** Xác định thực thể, thuộc tính và khóa | 25 | CLO3 | Không xác định được thực thể nào, hoặc nhầm thuộc tính thành thực thể ở toàn bộ bài | Đúng < 50% số thực thể trong đáp án; khóa chọn sai loại hoặc không có khóa | Đúng 50–69% số thực thể; còn nhầm thuộc tính đa trị hoặc thuộc tính dẫn xuất | Đúng 70–89% số thực thể; phân loại đúng bốn loại thuộc tính; mọi khóa đều hợp lệ | Đúng ≥ 90% số thực thể; xử lý đúng thuộc tính đa trị và giải thích được chọn khóa tự nhiên hay khóa thay thế |
| **2.3.** Xác định liên kết, lực lượng và sự tham gia | 30 | CLO3 | Không xác định được liên kết nào | Đúng < 50% số liên kết trong đáp án; sai loại 1:1 / 1:M / M:N | Đúng 50–69% số liên kết; chưa xác định lực lượng hoặc chưa nêu sự tham gia | Đúng 70–89% số liên kết kèm lực lượng; có nêu sự tham gia bắt buộc / tùy chọn | Đúng ≥ 90% số liên kết; áp dụng đúng kỹ thuật hỏi hai chiều và xử lý được liên kết đệ quy hoặc liên kết bậc ba |
| **2.4.** Hoàn chỉnh sơ đồ ER: ký pháp, thực thể yếu, liên kết M:N | 20 | CLO3 | Không vẽ được sơ đồ, hoặc sơ đồ không dùng ký pháp nào | Sai ≥ 3 loại ký hiệu; sơ đồ không đánh dấu khóa | Ký pháp đúng cơ bản, còn sai 1–2 ký hiệu; chưa xử lý thực thể yếu hoặc liên kết M:N | Ký pháp đúng và nhất quán một hệ (Chen hoặc Crow's Foot); xử lý đúng thực thể yếu và M:N | Như mức Khá, đồng thời sơ đồ khớp hoàn toàn với danh mục quy tắc nghiệp vụ đã phát biểu ở tiêu chí 2.1 |

> Bắt buộc khi ra đề: đề cho một **tình huống nghiệp vụ mô tả bằng lời thường**, chưa xuất hiện trên lớp. Đáp án phải liệt kê sẵn ba mẫu số: **số quy tắc nghiệp vụ N** (khuyến nghị N = 8–12), **số thực thể** và **số liên kết** — bốn tiêu chí của rubric đều neo theo tỷ lệ trên ba mẫu số này. Thiếu chúng thì quay lại chấm cảm tính.

> Sinh viên được vẽ sơ đồ bằng tay trên giấy thi; không yêu cầu dùng phần mềm. Chấp nhận cả ký pháp Chen và Crow's Foot, miễn là nhất quán trong toàn bài.

> Bài kiểm tra tổ chức ở tuần 5, sau khi đã dạy xong Chương 2 ở tuần 3; phạm vi giới hạn ở Chương 2 và công bố cho sinh viên chậm nhất tuần 3.

> Khuyến nghị 2 giảng viên chấm độc lập một mẫu ~10% số bài để đối chiếu, vì bài thiết kế có biên độ đánh giá rộng hơn bài tính toán.

#### Rubric 3 — Bài kiểm tra viết — ánh xạ mô hình ER sang lược đồ quan hệ và đại số quan hệ · *đo **CLO3*** · trọng số học phần **20%** · tuần 6

| Tiêu chí | TS | CLO | Kém (0%) | Yếu (25%) | Trung bình (50%) | Khá (75%) | Giỏi/Xuất sắc (100%) |
|:--|:--:|:--:|:--|:--|:--|:--|:--|
| **3.1.** Áp dụng bốn quy tắc ánh xạ ER → quan hệ | 35 | CLO3 | Không ánh xạ được quan hệ nào, hoặc chép lại sơ đồ ER thay vì ánh xạ | Đúng < 50% số quan hệ trong đáp án; không tách được liên kết M:N | Đúng 50–69% số quan hệ; tách được M:N nhưng sai thực thể yếu hoặc thuộc tính đa trị | Đúng 70–89% số quan hệ; xử lý đúng M:N, thực thể yếu và thuộc tính đa trị | Đúng ≥ 90% số quan hệ; áp dụng đủ bốn quy tắc và không sinh ra quan hệ thừa |
| **3.2.** Xác định khóa chính, khóa ngoại và toàn vẹn tham chiếu | 25 | CLO3 | Không xác định khóa chính cho quan hệ nào | Đúng < 50% số khóa chính; không có khóa ngoại nào | Đúng 50–69% số khóa chính; khóa ngoại đặt sai bên ở ≥ 2 quan hệ | Đúng 70–89% số khóa chính và khóa ngoại; nêu được ràng buộc toàn vẹn tham chiếu tương ứng | Đúng ≥ 90%; đồng thời chỉ ra được thao tác nào trên quan hệ nào có thể làm vi phạm toàn vẹn tham chiếu |
| **3.3.** Viết biểu thức đại số quan hệ trả lời yêu cầu truy vấn | 30 | CLO3 | Không viết được biểu thức nào | Đúng < 30% số câu truy vấn; dùng sai ký hiệu phép toán | Đúng 30–59% số câu; làm được phép chọn và phép chiếu, chưa dùng được phép kết | Đúng 60–84% số câu; dùng đúng phép kết và các phép toán tập hợp, có kiểm tra điều kiện khả hợp | Đúng ≥ 85% số câu; biểu thức gọn, dùng được phép chia hoặc phép kết ngoài khi đề yêu cầu |
| **3.4.** Trình bày lược đồ và thuyết minh quyết định ánh xạ | 10 | CLO3 | Không trình bày lược đồ theo dạng quy định | Có lược đồ nhưng không đánh dấu khóa; không viết phần thuyết minh | Lược đồ có đánh dấu khóa; thuyết minh nêu chung chung, không gắn với quyết định ánh xạ nào | Lược đồ rõ ràng, đánh dấu đủ khóa chính và khóa ngoại; giải thích được ≥ 2 quyết định ánh xạ | Như mức Khá, đồng thời nêu được một phương án ánh xạ thay thế đã cân nhắc và lý do loại |

> Bắt buộc khi ra đề: (1) đề **phát sẵn một sơ đồ ER** — không bắt sinh viên vẽ lại, vì phần thiết kế ER đã đo ở Rubric 2 và lặp lại sẽ đo trùng; (2) đáp án phải liệt kê sẵn **số quan hệ**, **số khóa chính và khóa ngoại**, **số câu truy vấn** — ba mẫu số neo cho tiêu chí 3.1, 3.2 và 3.3; (3) đề phải có **một câu thuyết minh bắt buộc**, dạng *"Giải thích ít nhất 2 quyết định ánh xạ của em — ví dụ: vì sao tách bảng cho liên kết M:N, vì sao khóa ngoại đặt ở bên này"*. Không có câu này thì tiêu chí 3.4 không có gì để chấm.

> Sơ đồ ER phát trong đề nên là sơ đồ của một nghiệp vụ khác với đề Rubric 2, để bài giữa kỳ không thành bài làm lại.

> Bài kiểm tra tổ chức ở tuần 6, sau khi đã dạy xong Chương 3 ở tuần 5; phạm vi Chương 2 và Chương 3, công bố cho sinh viên chậm nhất tuần 4.

> Đây là thành phần đánh giá giữa học phần và nằm đúng giữa 11 tuần của học phần — khác với phương án đặt bài thiết kế tổng hợp ở tuần cuối, vốn khiến tên gọi "giữa học phần" không khớp thời điểm tổ chức.

#### Rubric 4 — Bài kiểm tra trắc nghiệm theo khối kiến thức · *đo **CLO2+CLO3*** · trọng số học phần **50%** · tuần 12 — theo lịch thi của Trường

| Tiêu chí | TS | CLO | Kém (0%) | Yếu (25%) | Trung bình (50%) | Khá (75%) | Giỏi/Xuất sắc (100%) |
|:--|:--:|:--:|:--|:--|:--|:--|:--|
| **A.** Khối khái niệm nền — dữ liệu và metadata, CSDL – DBMS – hệ CSDL, kiến trúc ba mức, mô hình ER/EER, mô hình quan hệ và tám đặc trưng, đại số quan hệ, khái niệm ràng buộc toàn vẹn, phụ thuộc hàm và các dạng chuẩn | 60 | CLO2 | Đúng ≤ 30% số câu của khối | Đúng 31–54% số câu của khối | Đúng 55–69% số câu của khối | Đúng 70–84% số câu của khối | Đúng 85–100% số câu của khối |
| **B1.** Khối tình huống — ràng buộc toàn vẹn: đọc bảng tầm ảnh hưởng, chọn hành động khi vi phạm, phát hiện ràng buộc bị vi phạm trên bộ dữ liệu mẫu | 15 | CLO3 | Đúng ≤ 30% số câu của khối | Đúng 31–54% số câu của khối | Đúng 55–69% số câu của khối | Đúng 70–84% số câu của khối | Đúng 85–100% số câu của khối |
| **B2.** Khối tình huống — chuẩn hóa: tính bao đóng, tìm khóa, xác định dạng chuẩn cao nhất, xác định phép tách có bảo toàn thông tin hay không | 25 | CLO3 | Đúng ≤ 30% số câu của khối | Đúng 31–54% số câu của khối | Đúng 55–69% số câu của khối | Đúng 70–84% số câu của khối | Đúng 85–100% số câu của khối |

> **Cảnh báo về tính giá trị — điều quan trọng nhất khi ra đề này.** Chương 4 (Ràng buộc toàn vẹn, 8 tiết) và Chương 5 (Chuẩn hóa, 12 tiết) chiếm 20/45 tiết — 44% thời lượng học phần — và **chỉ được đo bằng đề trắc nghiệm này**. Vì vậy hai khối B1 và B2 phải chiếm **ít nhất 40% tổng số câu của đề**, tương ứng với 40% trọng số của rubric.

> **Ma trận đề bắt buộc.** Khối A: 60% số câu, mức Nhớ – Hiểu, phải có câu phân biệt các cặp khái niệm dễ nhầm (CSDL ↔ DBMS; khóa chính ↔ khóa dự tuyển; thực thể ↔ kiểu thực thể; toàn vẹn thực thể ↔ toàn vẹn tham chiếu). Khối B1 và B2: 40% số câu, **mỗi câu BẮT BUỘC kèm dữ kiện** — lược đồ quan hệ, tập phụ thuộc hàm, bảng tầm ảnh hưởng, bộ dữ liệu mẫu, hoặc một phép tách cho sẵn — để sinh viên phải chạy thuật toán rồi mới chọn được đáp án.

> Ví dụ câu đúng chuẩn cho khối B2: *Cho R(A, B, C, D) với F = {A → B, B → C} và khóa chính là A. Lược đồ R đạt dạng chuẩn cao nhất là: A. 1NF · B. 2NF · C. 3NF · D. BCNF.* Sinh viên buộc phải tìm khóa và phát hiện phụ thuộc bắc cầu A → B → C mới trả lời được. Câu KHÔNG được dùng ở khối B: *"Dạng chuẩn 3NF là gì?"* — đó là câu tái hiện định nghĩa, thuộc khối A.

> CLO3 tuyên bố ở mức Nhận thức 5/6 và nhận 20/50 điểm từ đề trắc nghiệm này. Nếu khối B ra theo lối tái hiện định nghĩa thì đề cương khai đo Tổng hợp – đánh giá nhưng thực tế chỉ đo Ghi nhớ — đây là lỗi constructive alignment mà đoàn kiểm định soi trước tiên.

> **Lưu ý kỹ thuật khi nhập điểm:** phải tách riêng điểm khối A và tổng điểm khối B1 + B2, vì mục Ngưỡng đạt CLO cần hai con số này để tính mức đạt CLO2 và CLO3. Nếu chỉ lưu tổng điểm trắc nghiệm thì không báo cáo được mức đạt CLO.

### 7.4. Cách tính điểm học phần

```
Điểm học phần = 15% × Rubric 1 + 15% × Rubric 2 + 20% × Rubric 3 + 50% × Rubric 4
```

### 7.5. Ngưỡng đạt CLO và báo cáo mức đạt chuẩn đầu ra

| CLO | Thành phần đo | Công thức điểm CLO |
|:--:|:--|:--|
| CLO1 | Nhận thức, thái độ học tập (chuyên cần · nội quy · hồ sơ tự học · hợp tác nhóm) | (Nhận thức, thái độ học tập (chuyên cần · nội quy · hồ sơ tự học · hợp tác nhóm) × 15) ÷ 15 |
| CLO3 | Bài kiểm tra viết — chuyển quy tắc nghiệp vụ thành mô hình ER + Bài kiểm tra viết — ánh xạ mô hình ER sang lược đồ quan hệ và đại số quan hệ + Bài kiểm tra trắc nghiệm theo khối kiến thức | (Bài kiểm tra viết — chuyển quy tắc nghiệp vụ thành mô hình ER × 15 + Bài kiểm tra viết — ánh xạ mô hình ER sang lược đồ quan hệ và đại số quan hệ × 20 + Bài kiểm tra trắc nghiệm theo khối kiến thức × 20) ÷ 55 |
| CLO2 | Bài kiểm tra trắc nghiệm theo khối kiến thức | (Bài kiểm tra trắc nghiệm theo khối kiến thức × 30) ÷ 30 |

| Cấp | Ngưỡng | Ý nghĩa |
|:--|:--|:--|
| Cá nhân | Sinh viên đạt một CLO khi điểm CLO đó ≥ 5,0/10 — dưới ngưỡng thì ghi nhận để tư vấn học tập, dù điểm tổng học phần vẫn có thể đạt | Dưới ngưỡng ⇒ ghi nhận để tư vấn học tập |
| Lớp học phần | CLO của lớp học phần được xem là đạt khi ≥ 70% sinh viên đạt CLO đó; dưới ngưỡng thì giảng viên rà lại nội dung, phương pháp dạy và đề thi của phần tương ứng, ghi vào báo cáo cải tiến PDCA của Bộ môn | Dưới ngưỡng ⇒ rà lại nội dung, phương pháp dạy và đề thi; ghi vào báo cáo cải tiến |

## 8. Kế hoạch và nội dung giảng dạy học phần *(Course Schedule)*

**Bảng 7: Kế hoạch giảng dạy**

| Tuần | Nội dung giảng dạy | LT | TH | ∑ | CLOs | Hoạt động giảng dạy | Hoạt động của người học | Hoạt động kiểm tra – đánh giá |
|:--:|:--|:--:|:--:|:--:|:--:|:--|:--|:--|
| 1 | **Chương 1: Tổng quan về cơ sở dữ liệu** | 4 | 0 | 4 | CLO1, CLO2 | Thuyết giảng; đặt vấn đề bằng tình huống Trung tâm Anh ngữ ABC; tổ chức thảo luận "Excel có phải cơ sở dữ liệu không?"; demo hệ quản trị CSDL của giảng viên trên máy chiếu — tạo CSDL mẫu, xem từ điển dữ liệu; công bố toàn bộ rubric của học phần | Nghe, ghi chép, tham gia thảo luận, làm bài tập nhanh; quan sát demo (không phải tự cài đặt phần mềm) | Quan sát chuyên cần và nội quy (Rubric 1); chấm sản phẩm tự học tuần 1; nội dung chương này thuộc khối A của đề trắc nghiệm cuối kỳ (Rubric 4) |
|  | 1.1. Dữ liệu và thông tin · Tháp DIKW · Khái niệm CSDL và metadata | 1 | 0 | 1 |  |  |  |  |
|  | 1.2. Hệ quản trị CSDL (DBMS) · Phân biệt CSDL – DBMS – hệ CSDL | 0,5 | 0 | 0,5 |  |  |  |  |
|  | 1.3. Vì sao cần CSDL — bốn hạn chế của hệ thống tệp và chuỗi nhân quả (dư thừa → dị thường → quyết định sai) | 1 | 0 | 1 |  |  |  |  |
|  | 1.4. Mô hình dữ liệu · Lược đồ (schema) và thể hiện (instance) | 0,5 | 0 | 0,5 |  |  |  |  |
|  | 1.5. Kiến trúc ba mức ANSI/SPARC và tính độc lập dữ liệu (logic · vật lý) | 0,5 | 0 | 0,5 |  |  |  |  |
|  | 1.6. Các ngôn ngữ CSDL (DDL/DML/DQL/DCL) · Giao dịch và ACID (mức nhận biết) · Chức năng, thành phần của DBMS · Từ điển dữ liệu trong DBMS thực tế (`INFORMATION_SCHEMA`) — giảng viên demo trên lớp [3, Ch.1] | 0,5 | 0 | 0,5 |  |  |  |  |
| 2-3 | **Chương 2: Mô hình thực thể–liên kết (ER) và ER mở rộng** | 8 | 0 | 8 | CLO1, CLO2, CLO3 | Thuyết giảng; làm mẫu kỹ thuật hỏi hai chiều trên bảng; tổ chức "phòng thiết kế" — nhóm vẽ ERD rồi gallery walk phản biện chéo; chữa lỗi thiết kế điển hình ngay tại lớp | Vẽ ERD theo nhóm; phản biện chéo bài của nhóm khác; làm bài tập cá nhân; luyện quy trình quy tắc nghiệp vụ → bảng hỏi hai chiều → ERD trong giờ tự học | Quan sát chuyên cần và hoạt động nhóm (Rubric 1); chấm bài tập ERD và sản phẩm tự học tuần 2–3; **chương này là toàn bộ phạm vi của Bài kiểm tra viết 15% (Rubric 2) tổ chức ở tuần 5** |
|  | 2.1. Quá trình thiết kế CSDL · Quy tắc nghiệp vụ và tiêu chí "đếm được" | 1 | 0 | 1 |  |  |  |  |
|  | 2.2. Thực thể · Bốn loại thuộc tính · Xử lý thuộc tính đa trị | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 2.3. Khóa / định danh · Hai tiêu chí bắt buộc của khóa · Khóa tự nhiên và khóa thay thế (surrogate) — cách chọn [3, Ch.5] | 0,5 | 0 | 0,5 |  |  |  |  |
|  | 2.4. Liên kết · **Kỹ thuật hỏi hai chiều** xác định 1:1 / 1:M / M:N | 1 | 0 | 1 |  |  |  |  |
|  | 2.5. Kết nối · Lực lượng · Sự tham gia (tùy chọn / bắt buộc) | 1 | 0 | 1 |  |  |  |  |
|  | 2.6. Bậc liên kết · Liên kết đệ quy · Thực thể mạnh / yếu · Thực thể kết hợp (tách M:N) | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 2.7. Mô hình ER mở rộng (EER): thực thể cha/con (supertype/subtype) · phân cấp chuyên biệt hóa · kế thừa · ràng buộc rời nhau/chồng lấn, đầy đủ/không đầy đủ | 1 | 0 | 1 |  |  |  |  |
|  | 2.8. Quy trình 5 bước vẽ ERD · Ký pháp Chen / Crow's Foot · Sơ lược UML class diagram | 0,5 | 0 | 0,5 |  |  |  |  |
| 4-5 | **Chương 3: Mô hình dữ liệu quan hệ và các phép toán** | 8 | 0 | 8 | CLO2, CLO3 | Thuyết giảng; kỹ thuật "làm sai để thấy vì sao" — đặt khóa ngoại nhầm bên rồi cho lớp phát hiện hệ quả; giải mẫu biểu thức đại số quan hệ từng bước; coi bài kiểm tra viết cuối tuần 5 | Đổi ERD giữa các nhóm để ánh xạ chéo; luyện viết đại số quan hệ; làm bài kiểm tra viết; ánh xạ ERD thư viện sang lược đồ quan hệ trong giờ tự học | **Bài kiểm tra viết 15% (Rubric 2) tổ chức ở tuần 5, phạm vi Chương 2**; quan sát chuyên cần (Rubric 1); chấm sản phẩm tự học tuần 4–5; **chương này là mốc cuối của phạm vi Bài kiểm tra giữa học phần (Rubric 3) tổ chức ở tuần 6** |
|  | 3.1. Quan hệ, bộ, thuộc tính, miền giá trị · Tám đặc trưng của bảng quan hệ | 1 | 0 | 1 |  |  |  |  |
|  | 3.2. Phụ thuộc hàm (X → Y) và tính có chiều · Siêu khóa – khóa dự tuyển – khóa chính – khóa ngoại | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 3.3. Toàn vẹn thực thể và toàn vẹn tham chiếu · Vì sao khóa chính cấm null còn khóa ngoại cho phép | 1 | 0 | 1 |  |  |  |  |
|  | 3.4. **Bốn quy tắc ánh xạ ER → quan hệ** (QT1–QT4) · Xử lý thực thể yếu và liên kết M:N | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 3.5. Đại số quan hệ — phép chọn σ, phép chiếu π | 1 | 0 | 1 |  |  |  |  |
|  | 3.6. Phép toán tập hợp ∪, ∩, −, × · Điều kiện khả hợp | 1 | 0 | 1 |  |  |  |  |
|  | 3.7. Phép kết ⋈ (tự nhiên, bằng, trong/ngoài) · Ứng dụng kết ngoài để dò lỗi toàn vẹn tham chiếu [3, Ch.3] · Phép chia ÷ | 1 | 0 | 1 |  |  |  |  |
| 6-7 | **Chương 4: Ràng buộc toàn vẹn** | 8 | 0 | 8 | CLO2, CLO3 | Thuyết giảng; suy luận từng ô của bảng tầm ảnh hưởng cùng cả lớp; thảo luận "đặt ràng buộc ở CSDL hay ở ứng dụng?"; giảng viên minh họa cú pháp khai báo ràng buộc (`CHECK`, `NOT NULL`, `UNIQUE`, `FOREIGN KEY … ON DELETE`) — **không yêu cầu sinh viên viết SQL**; coi bài kiểm tra giữa học phần đầu tuần 6 | Làm bài kiểm tra giữa học phần; đóng vai "đội thanh tra dữ liệu" — săn ràng buộc toàn vẹn trên lược đồ của nhóm khác; lập bảng tầm ảnh hưởng trong giờ tự học | **Bài kiểm tra giữa học phần 20% (Rubric 3) tổ chức đầu tuần 6, phạm vi Chương 2–3**; chấm bảng tầm ảnh hưởng và sản phẩm tự học tuần 6–7; nội dung chương này được đo ở **khối B1** của đề trắc nghiệm cuối kỳ (Rubric 4) |
|  | 4.1. Khái niệm ràng buộc toàn vẹn · Vì sao đặt ràng buộc ở tầng CSDL thay vì chỉ ở ứng dụng | 1 | 0 | 1 |  |  |  |  |
|  | 4.2. Ba yếu tố của một ràng buộc toàn vẹn: điều kiện · bối cảnh · bảng tầm ảnh hưởng | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 4.3. **Lập bảng tầm ảnh hưởng** — quy tắc "ĐÚNG thành SAI" · Câu thần chú "Thêm ở CON, Xóa ở CHA" | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 4.4. Hành động khi vi phạm: từ chối · CASCADE · SET NULL — chọn theo nghiệp vụ · Đọc hiểu cú pháp khai báo ràng buộc, giảng viên minh họa [3, Ch.3] | 1 | 0 | 1 |  |  |  |  |
|  | 4.5. Ràng buộc bối cảnh một quan hệ: miền giá trị · liên thuộc tính · liên bộ | 1 | 0 | 1 |  |  |  |  |
|  | 4.6. Ràng buộc bối cảnh nhiều quan hệ: khóa ngoại · liên thuộc tính liên quan hệ · liên bộ liên quan hệ · Giới thiệu trigger | 1 | 0 | 1 |  |  |  |  |
|  | 4.7. Thực hành phát hiện ràng buộc toàn vẹn trên bài toán thực tế — bộ 6 loại đầy đủ · "cờ đỏ thiết kế" (ràng buộc khó ⇒ thiết kế cần cải thiện) | 1 | 0 | 1 |  |  |  |  |
| 8-10 | **Chương 5: Lý thuyết thiết kế CSDL quan hệ (chuẩn hóa)** | 12 | 0 | 12 | CLO2, CLO3 | Thuyết giảng; giải mẫu từng thuật toán trên bảng; tổ chức "bệnh viện lược đồ" — nhóm chẩn đoán, điều trị, tái khám một lược đồ có bệnh; luyện đọc đề dạng câu hỏi tình huống để chuẩn bị cho khối B2 của đề trắc nghiệm | Luyện bao đóng, tìm khóa, phủ tối thiểu; chuẩn hóa lược đồ theo nhóm; phản biện chéo; xác định phép tách bảo toàn thông tin trong giờ tự học | Chấm bài tập chuẩn hóa (thường xuyên, không tính điểm thành phần); chấm sản phẩm tự học tuần 8–10; **nội dung chương này được đo chính thức ở khối B2 của đề trắc nghiệm cuối kỳ (Rubric 4) — chiếm 25% trọng số đề** |
|  | 5.1. Thế nào là một CSDL "tốt" — định nghĩa đo được · Vị trí của chuẩn hóa trong quy trình thiết kế | 0,5 | 0 | 0,5 |  |  |  |  |
|  | 5.2. Ba loại phụ thuộc hàm: đầy đủ · bộ phận · bắc cầu | 1 | 0 | 1 |  |  |  |  |
|  | 5.3. Hệ luật dẫn Armstrong (3 luật gốc + 3 luật dẫn xuất) | 1 | 0 | 1 |  |  |  |  |
|  | 5.4. **Bao đóng X⁺** — thuật toán · hai công dụng · phân biệt với F⁺ | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 5.5. **Thuật toán tìm khóa** (TN – TG) · Tìm tất cả khóa | 2 | 0 | 2 |  |  |  |  |
|  | 5.6. Phủ tối thiểu — ba điều kiện · thuật toán ba bước | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 5.7. Các dạng chuẩn 1NF · 2NF · 3NF · Câu thần chú "the key, the whole key, and nothing but the key" | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 5.8. Phép tách lược đồ — bảo toàn thông tin (lossless join) và bộ giả · bảo toàn phụ thuộc hàm | 1,5 | 0 | 1,5 |  |  |  |  |
|  | 5.9. Quy trình chuẩn hóa hoàn chỉnh — ví dụ tổng hợp từ bảng phẳng về 3NF | 1 | 0 | 1 |  |  |  |  |
|  | 5.10. Dạng chuẩn mức cao: BCNF (so sánh với 3NF) · giới thiệu 4NF · Phi chuẩn hóa (denormalization) — khi nào hợp lý [3, Ch.6] | 0,5 | 0 | 0,5 |  |  |  |  |
| 11 | **Ôn tập – Tổng hợp – Bài tập nhóm** | 5 | 0 | 5 | CLO1, CLO2, CLO3 | Hệ thống hóa bằng sơ đồ một trang (quy tắc nghiệp vụ → ERD → lược đồ quan hệ → ràng buộc toàn vẹn → 3NF); tổ chức trình bày và phản biện chéo sản phẩm nhóm; giải đáp và định hướng ôn thi cuối kỳ | Hoàn thiện sản phẩm nhóm; trình bày và phản biện; nộp phiếu đánh giá đồng đẳng; ôn tập tổng hợp | **Chốt điểm Nhận thức thái độ 15% (Rubric 1)** — trong đó tiêu chí 1.4 chấm hợp tác nhóm dựa trên sản phẩm nhóm tuần này và phiếu đánh giá đồng đẳng |
|  | Hệ thống hóa toàn bộ quy trình thiết kế: quy tắc nghiệp vụ → ERD → ánh xạ → ràng buộc toàn vẹn → chuẩn hóa | 1,5 | 0 | 1,5 |  |  |  |  |
|  | **Bài tập nhóm tổng hợp** — thiết kế trọn vẹn một CSDL từ đề bài thực tế · trình bày · phản biện chéo (chấm ở tiêu chí 1.4 của Rubric 1) | 2,5 | 0 | 2,5 |  |  |  |  |
|  | Giải đáp – định hướng ôn thi cuối kỳ · hướng dẫn đọc dạng câu hỏi tình huống của khối B1, B2 | 1 | 0 | 1 |  |  |  |  |
|  | **TỔNG** | **45** | **0** | **45** |  |  |  |  |

## 9. Kế hoạch tự học *(Self-study Plan)*

> Tỷ lệ chuẩn: 1 tiết lên lớp ⇒ 2 tiết tự học. Quỹ tự học khai ở mục 2.5 là 90 tiết — đây là mức TRẦN. Đề cương định giao 78 tiết và **chừa lại 12 tiết (13,3%) làm khoản dư**, dành để hấp thụ phần phát sinh khi biên soạn tập bài giảng và độ chậm thực tế của người học. Khi phải dùng tới khoản dư, ghi rõ tuần nào vượt và vượt bao nhiêu vào chính chương đó của tập bài giảng, đồng thời cập nhật lại bảng này.

**Nguyên tắc thiết kế nhiệm vụ:** mọi nhiệm vụ chỉ cần **giấy bút** và **công cụ vẽ sơ đồ miễn phí** (draw.io) — **KHÔNG yêu cầu cài đặt hay sử dụng hệ quản trị CSDL / SQL**, vì các kỹ năng đó thuộc học phần Hệ quản trị CSDL kế tiếp mà sinh viên chưa học. Phần thao tác trên DBMS do giảng viên demo trên lớp để minh họa.

Sản phẩm nộp được tính điểm qua tiêu chí 1.3 của Rubric 1. Ba nhiệm vụ là **bài dượt trực tiếp** cho ba bài đánh giá: tuần 3 dượt cho bài kiểm tra viết tuần 5, tuần 5 dượt cho bài giữa học phần tuần 6, và tuần 10 dượt cho khối B2 của đề trắc nghiệm cuối kỳ.

| Tuần | Nhiệm vụ tự học | Sản phẩm nộp | Tiết |
|:--:|:--|:--|:--:|
| 1 | Đọc [1] chương mở đầu; [3] Ch.1. Chọn một bảng dữ liệu quen thuộc (danh bạ, bảng điểm…), lập bảng metadata trên giấy: tên cột · kiểu · bắt buộc? · ràng buộc. Phân tích một bảng phẳng cho trước: chỉ ra dư thừa và 3 dị thường (thêm, xóa, sửa). | Bảng metadata + bài phân tích dị thường | 7 |
| 2 | Đọc [3] Ch.4 (mục 4.1). Vẽ lại ERD Trung tâm Anh ngữ ABC bằng draw.io theo ký pháp đã học trên lớp, đánh dấu đầy đủ khóa và lực lượng. | File PNG sơ đồ ERD | 7 |
| 3 | Đọc [3] Ch.5 (EER). Làm bài tập ERD thư viện theo đúng quy trình: phát biểu quy tắc nghiệp vụ → lập bảng hỏi hai chiều → vẽ ERD → viết thuyết minh. **Bài dượt trực tiếp cho bài kiểm tra viết tuần 5.** | Danh mục quy tắc nghiệp vụ + bảng hỏi hai chiều + ERD + thuyết minh | 7 |
| 4 | Đọc [1] chương mô hình quan hệ; [3] Ch.3 (3.1–3.4). Ánh xạ ERD thư viện của tuần 3 sang lược đồ quan hệ theo bốn quy tắc, đánh dấu đầy đủ khóa chính và khóa ngoại, nêu rõ đã dùng quy tắc nào cho liên kết nào. | Lược đồ quan hệ có PK/FK + bảng đối chiếu quy tắc ánh xạ | 7 |
| 5 | Luyện đại số quan hệ — 10 biểu thức trên lược đồ đã ánh xạ ở tuần 4. Kiểm tra toàn vẹn trên giấy: với bộ dữ liệu mẫu cho trước của 7 bảng ABC, chỉ ra thao tác nào vi phạm toàn vẹn tham chiếu và giải thích. **Bài dượt trực tiếp cho bài kiểm tra giữa học phần tuần 6.** | Bài tập 10 biểu thức đại số quan hệ + bài kiểm tra toàn vẹn | 7 |
| 6 | Đọc [1] chương ràng buộc toàn vẹn; [2] phần toàn vẹn. Phát hiện ≥ 8 ràng buộc toàn vẹn trên lược đồ thư viện, phân đủ 6 loại đã học, mỗi ràng buộc ghi rõ điều kiện và bối cảnh. | Bảng 8 ràng buộc toàn vẹn đủ 6 loại | 7 |
| 7 | Lập bảng tầm ảnh hưởng cho 3 ràng buộc đã phát hiện ở tuần 6; với mọi khóa ngoại của lược đồ, đề xuất hành động khi vi phạm (từ chối / CASCADE / SET NULL) kèm lý do nghiệp vụ cho từng lựa chọn. | Bảng tầm ảnh hưởng + bảng hành động kèm lý do nghiệp vụ | 7 |
| 8 | Đọc [3] Ch.6 (6.1–6.3); [2] phần phụ thuộc hàm. Luyện bao đóng X⁺ và thuật toán tìm khóa — 5 bài tập, mỗi bài ghi rõ từng bước chạy thuật toán. | Bài tập 5 câu có trình bày từng bước | 7 |
| 9 | Luyện phủ tối thiểu và xác định dạng chuẩn cao nhất — 5 bài tập. Với mỗi bài, ghi rõ vì sao lược đồ dừng ở dạng chuẩn đó, chỉ ra phụ thuộc hàm nào là nguyên nhân. | Bài tập 5 câu có phần giải thích nguyên nhân | 7 |
| 10 | Chuẩn hóa lược đồ thư viện về 3NF theo quy trình hoàn chỉnh. Với 3 phép tách cho trước, **xác định phép tách nào bảo toàn thông tin** và giải thích căn cứ. **Bài dượt trực tiếp cho khối B2 của đề trắc nghiệm cuối kỳ.** | Bài tổng hợp chuẩn hóa + phần xác định phép tách bảo toàn thông tin | 9 |
| 11 | Hoàn thiện sản phẩm bài tập nhóm tổng hợp và chuẩn bị phần trình bày; nộp phiếu đánh giá đồng đẳng. Ôn tập toàn học phần theo sơ đồ một trang; tự làm một đề trắc nghiệm mẫu để làm quen dạng câu hỏi tình huống của khối B1, B2. | Sản phẩm nhóm + phiếu đánh giá đồng đẳng + bài làm đề trắc nghiệm mẫu | 6 |
|  | **TỔNG** |  | **78** |

## 10. Tài liệu học tập *(Learning Resources)*

**Sách, giáo trình chính *(Textbooks)***

- [1] Tô Văn Nam (2005). Giáo trình cơ sở dữ liệu. NXB Giáo dục.

**Tài liệu tham khảo *(References)***

- [2] Vũ Đức Thi (1997). Cơ sở dữ liệu — kiến thức và thực hành. NXB Thống kê.
- [3] Coronel, C. & Morris, S. Database Systems: Design, Implementation & Management. Cengage Learning. — nguồn cho các nội dung nâng cao đã tích hợp: Ch.1 (khái niệm, từ điển dữ liệu), Ch.3 (mô hình quan hệ, ràng buộc), Ch.4 (ER), Ch.5 (EER, chọn khóa thay thế), Ch.6 (chuẩn hóa, BCNF, 4NF, phi chuẩn hóa).

**Các loại học liệu khác *(Other Learning Resources)***

- Tập bài giảng học phần (5 chương, có hình vẽ minh họa) và bộ slide bài giảng do Bộ môn Công nghệ thông tin biên soạn.
- **Bộ đề tình huống nghiệp vụ** dùng cho Rubric 2 và Rubric 3, kèm đáp án liệt kê sẵn số quy tắc nghiệp vụ, số thực thể, số liên kết, số quan hệ và số câu truy vấn — điều kiện bắt buộc để chấm được hai rubric này. Mỗi học kỳ thay đề để tránh lưu truyền lời giải.
- **Ngân hàng câu hỏi trắc nghiệm phân theo ba khối A, B1, B2**, trong đó mọi câu của khối B1 và B2 đều kèm dữ kiện (lược đồ, tập phụ thuộc hàm, bảng tầm ảnh hưởng, bộ dữ liệu mẫu hoặc phép tách cho sẵn).
- Công cụ: **draw.io** — vẽ ERD, miễn phí, sinh viên sử dụng. MySQL Workbench / SSMS chỉ dùng cho **demo của giảng viên** trên lớp; sinh viên **không bắt buộc** cài đặt.

## 11. Chính sách học phần *(Course Policies)*

- Liêm chính học thuật: bài tập thiết kế nộp về nhà phải là sản phẩm của cá nhân hoặc của chính nhóm. Hai bài nộp có sơ đồ và thuyết minh trùng khớp bị điểm 0 ở đầu điểm tương ứng. Mọi tư liệu, sơ đồ, số liệu dẫn từ nguồn khác đều phải ghi nguồn.
- Sử dụng công cụ AI: được phép dùng để tra cứu khái niệm và kiểm tra lại lời giải của mình; không được dùng để tạo ra sơ đồ ER, lược đồ quan hệ hay bài chuẩn hóa thay cho sinh viên. Ghi rõ ở cuối sản phẩm phần nào có sử dụng công cụ hỗ trợ và dùng vào việc gì. Ba bài đánh giá của học phần đều làm trên lớp, không mang tài liệu điện tử — khoảng cách giữa bài nộp ở nhà và bài làm tại lớp sẽ lộ ra ngay.
- Nộp bài: sản phẩm tự học nộp đầu buổi học của tuần kế tiếp; nộp muộn trừ điểm theo quy định. Phiếu đánh giá đồng đẳng nộp riêng, không công khai giữa các thành viên nhóm.
- Vắng học, thi lại, phúc khảo và khiếu nại điểm: thực hiện theo quy chế đào tạo hiện hành của Trường.

---

*Đà Nẵng, ngày … tháng … năm 2026*

| Trưởng khoa *(Dean)* | Trưởng bộ môn *(Head of the Program)* | Người biên soạn *(Compiled by)* |
|:--:|:--:|:--:|
|  |  |  |
