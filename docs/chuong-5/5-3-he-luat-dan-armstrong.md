# 5.3. Hệ luật dẫn Armstrong

*(1,0 tiết)*

Tập `F` mà người thiết kế thu thập được từ nghiệp vụ thường chỉ là **một phần** các phụ thuộc hàm thật sự tồn tại. Nhiều phụ thuộc khác **suy ra được** từ `F`. Hệ luật Armstrong *(1974)* cho biết cách suy diễn chính xác mà không cần nhìn lại dữ liệu.

## 5.3.1. Ba luật gốc

!!! note "Định nghĩa 5.5 (Hệ tiên đề Armstrong)"

    Cho `X`, `Y`, `Z` là các tập thuộc tính của quan hệ `R` *(ký hiệu `XZ` viết tắt cho `X ∪ Z`)*:

    - **Luật phản xạ** *(reflexivity)*: nếu `Y ⊆ X` thì `X → Y`.
    - **Luật tăng trưởng** *(augmentation)*: nếu `X → Y` thì `XZ → YZ`.
    - **Luật bắc cầu** *(transitivity)*: nếu `X → Y` và `Y → Z` thì `X → Z`.

Ba luật này là **đúng đắn** *(sound — mọi phụ thuộc suy ra được đều đúng trên mọi thể hiện thỏa `F`)* và **đầy đủ** *(complete — mọi phụ thuộc đúng theo `F` đều suy ra được bằng hữu hạn bước)* — đó là kết quả do W. W. Armstrong chứng minh năm 1974, và cũng là lý do chỉ cần ba luật này là đủ cho toàn bộ lý thuyết chuẩn hóa.

Trong ba luật, hai luật đầu thoạt nhìn có vẻ ít tác dụng:

- **Luật phản xạ** nói rằng *biết `(MAHV, MALOP)` thì biết `MAHV`* — hiển nhiên. Nhưng chính nhờ nó sinh ra các **phụ thuộc tầm thường** *(trivial)* kiểu `YZ → Y`, ta mới có "cầu nối" để rút bớt thuộc tính ở vế phải.
- **Luật tăng trưởng** cho phép *đắp thêm cùng một tập thuộc tính `Z` vào cả hai vế*. Khi có `A → B` mà phụ thuộc kế tiếp lại đòi vế trái là `BC` *(như `BC → D`)*, hai đầu chưa khớp nhau để bắc cầu ngay; nhờ tăng trưởng `A → B` với `C` thành `AC → BC`, cầu nối lập tức hình thành.

## 5.3.2. Ba luật dẫn xuất và chứng minh từ ba luật gốc

Từ ba luật gốc, ta chứng minh được ba luật dẫn xuất giúp rút ngắn đáng kể các bước biến đổi khi làm bài.

**Bảng 5.6. Ba luật gốc và ba luật dẫn xuất**

| Ký hiệu | Luật | Phát biểu | Loại |
|:--:|---|---|---|
| **IR1** | **Phản xạ** *(reflexivity)* | `Y ⊆ X` ⟹ `X → Y` | Gốc |
| **IR2** | **Tăng trưởng** *(augmentation)* | `X → Y` ⟹ `XZ → YZ` | Gốc |
| **IR3** | **Bắc cầu** *(transitivity)* | `X → Y`, `Y → Z` ⟹ `X → Z` | Gốc |
| **IR4** | **Hợp** *(union)* | `X → Y`, `X → Z` ⟹ `X → YZ` | Dẫn xuất |
| **IR5** | **Tách** *(decomposition)* | `X → YZ` ⟹ `X → Y` và `X → Z` | Dẫn xuất |
| **IR6** | **Bắc cầu giả** *(pseudotransitivity)* | `X → Y`, `WY → Z` ⟹ `WX → Z` | Dẫn xuất |

Vì sao gọi IR4, IR5, IR6 là luật **dẫn xuất**? Vì không cần thêm tiên đề mới nào — cả ba đều được suy ra thuần túy từ IR1, IR2, IR3. Bảng dưới đây trình bày trọn vẹn ba chứng minh ấy; người học nên đọc kỹ vì đây chính là **ba bài mẫu chuẩn mực nhất** về cách phối hợp phản xạ, tăng trưởng và bắc cầu.

**Bảng 5.7. Chứng minh ba luật dẫn xuất từ ba luật gốc của Armstrong**

| Luật cần chứng minh | Bước | Phụ thuộc suy ra | Căn cứ *(chỉ dùng IR1, IR2, IR3)* | Ý tưởng của bước |
|---|:--:|---|---|---|
| **Luật hợp (IR4)**<br/>Cho `X → Y` và `X → Z`,<br/>chứng minh `X → YZ` | 1<br/>2<br/>3<br/>4<br/>5 | `X → Y`<br/>`X → XY`<br/>`X → Z`<br/>`XY → YZ`<br/>`X → YZ` | giả thiết<br/>tăng trưởng (1) với `X` *(vì `XX = X`)*<br/>giả thiết<br/>tăng trưởng (3) với `Y`<br/>bắc cầu (2) và (4) | —<br/>tạo trung gian `XY`<br/>—<br/>đưa `XY` sang `YZ`<br/>nối `X → XY → YZ` |
| **Luật tách (IR5)**<br/>Cho `X → YZ`,<br/>chứng minh `X → Y` và `X → Z` | 1<br/>2<br/>3<br/>4<br/>5 | `X → YZ`<br/>`YZ → Y`<br/>`X → Y`<br/>`YZ → Z`<br/>`X → Z` | giả thiết<br/>phản xạ *(vì `Y ⊆ YZ`)*<br/>bắc cầu (1) và (2)<br/>phản xạ *(vì `Z ⊆ YZ`)*<br/>bắc cầu (1) và (4) | —<br/>dùng phản xạ để giữ lại `Y`<br/>nối `X → YZ → Y`<br/>dùng phản xạ để giữ lại `Z`<br/>nối `X → YZ → Z` |
| **Luật bắc cầu giả (IR6)**<br/>Cho `X → Y` và `WY → Z`,<br/>chứng minh `WX → Z` | 1<br/>2<br/>3<br/>4 | `X → Y`<br/>`WX → WY`<br/>`WY → Z`<br/>`WX → Z` | giả thiết<br/>tăng trưởng (1) với `W`<br/>giả thiết<br/>bắc cầu (2) và (3) | —<br/>bù `W` vào hai vế để khớp `WY`<br/>—<br/>nối `WX → WY → Z` |

Nhìn vào Bảng 5.7, vai trò của hai luật gốc đầu tiên hiện ra rất rõ: ở **luật tách**, nếu không có bước phản xạ `YZ → Y` thì không có cách nào "gọt" bớt `Z` khỏi vế phải; ở **luật hợp** và **luật bắc cầu giả**, nếu không có bước tăng trưởng để tạo tập trung gian `XY` hay `WX → WY` thì hai giả thiết đứng rời nhau, không nối thành chuỗi bắc cầu được.

Hai luật **hợp** và **tách** đi thành một cặp ngược chiều nhau: chúng cho phép **gộp** hoặc **tách** vế phải tùy tiện. Nhờ đó ta luôn viết lại được mọi tập `F` về dạng chuẩn **mỗi phụ thuộc chỉ có đúng một thuộc tính ở vế phải** — điều kiện đầu tiên của phủ tối thiểu ở mục 5.6.

Sáu luật viết bằng `X`, `Y`, `Z` trông khô khan, nhưng thay bằng các thuộc tính của Trung tâm Anh ngữ ABC thì luật nào cũng chỉ là một câu nói hiển nhiên trong nghiệp vụ.

**Bảng 5.8. Sáu luật, mỗi luật một ví dụ tại ABC**

| Luật | Ví dụ | Đọc thành lời |
|---|---|---|
| Phản xạ | `(MAHV, MALOP) → MAHV` | biết cả cặp thì đương nhiên biết mã học viên |
| Tăng trưởng | `MAGV → HOTEN_GV` ⟹ `(MAGV, MALOP) → (HOTEN_GV, MALOP)` | thêm cùng một thứ vào hai vế, phụ thuộc vẫn đúng |
| Bắc cầu | `MALOP → MAGV`, `MAGV → HOTEN_GV` ⟹ `MALOP → HOTEN_GV` | biết lớp thì biết giáo viên, biết giáo viên thì biết tên — vậy biết lớp là biết tên |
| Hợp | `MALOP → TENLOP`, `MALOP → MAGV` ⟹ `MALOP → (TENLOP, MAGV)` | hai điều cùng suy từ lớp thì gộp lại vẫn suy từ lớp |
| Tách | `MALOP → (TENLOP, MAGV)` ⟹ `MALOP → TENLOP` và `MALOP → MAGV` | suy được cả cụm thì suy được từng phần |
| Bắc cầu giả | `MALOP → MAGV`, `(NGAY, MAGV) → PHONG` ⟹ `(NGAY, MALOP) → PHONG` | nếu mỗi giáo viên mỗi ngày dạy ở một phòng, thì biết lớp và ngày là biết phòng |

Dòng **bắc cầu** đáng chú ý nhất: hai phụ thuộc đầu vào đều "vô hại", nhưng kết quả `MALOP → HOTEN_GV` chính là phụ thuộc bắc cầu ở Bảng 5.5 — luật Armstrong làm lộ ra thủ phạm mà mắt thường dễ bỏ qua.

## 5.3.3. Bốn ví dụ suy diễn từ cơ bản đến nâng cao

Khi đứng trước bài toán *"Cho tập `F`, hãy chứng minh `X → Y` bằng hệ luật Armstrong"*, người mới học thường lúng túng không biết áp luật nào trước. Bí quyết nằm ở **tư duy hai đầu**: nhìn **vế trái `X`** xem từ `X` đang có những mũi tên nào đi ra, đồng thời nhìn **vế phải `Y`** xem trong `F` có những mũi tên nào bắn trúng `Y`, rồi tìm cách bắc cầu giữa hai đầu ấy. Bốn ví dụ dưới đây minh họa bốn tình huống điển hình nhất.

!!! example "Ví dụ 5.2 — Ghép vế phải bằng Bắc cầu và Hợp"

    Cho `F = {A → B, B → C}`. Chứng minh `A → BC`.

    *Hướng suy nghĩ:* Đích cần chứng minh có vế phải gồm hai thuộc tính `B` và `C`. Ta tìm cách suy ra từng thuộc tính từ `A` (`A → B` đã có sẵn; `A → C` suy qua trung gian `B`), rồi dùng **luật hợp** gộp chúng lại.

    | Bước | Suy luận | Luật dùng | Giải thích |
    |:--:|---|---|---|
    | 1 | `A → B` | giả thiết | đã có phần thứ nhất của vế phải (`B`) |
    | 2 | `B → C` | giả thiết | cầu nối từ `B` sang `C` |
    | 3 | `A → C` | bắc cầu (1, 2) | nối `A → B → C` để có phần thứ hai (`C`) |
    | 4 | `A → BC` | hợp (1, 3) | gộp hai vế phải `B` và `C` có cùng vế trái `A` |

!!! example "Ví dụ 5.3 — Tách vế phải để làm bàn đạp bắc cầu"

    Cho `R(A, B, C, D, E)` và `F = {A → BC, B → D, CD → E}`. Chứng minh `A → E`.

    *Hướng suy nghĩ (lần ngược từ đích):* Trong `F`, chỉ có `CD → E` sinh ra được `E`. Vậy muốn có `A → E`, ta cần chứng minh `A → CD`. Muốn có `A → CD`, ta cần `A → C` và `A → D`. Nhìn lại giả thiết `A → BC`: dùng **luật tách** sẽ lấy ra được `A → B` và `A → C`; từ `A → B` kết hợp với `B → D` sẽ cho `A → D`. Mạch suy diễn đã thông suốt.

    | Bước | Suy luận | Luật dùng | Vì sao thực hiện bước này |
    |:--:|---|---|---|
    | 1 | `A → BC` | giả thiết | xuất phát từ vế trái `A` |
    | 2 | `A → B` | tách (1) | tách riêng `B` để chuẩn bị nối với `B → D` |
    | 3 | `A → C` | tách (1) | tách riêng `C` để lát nữa ghép thành `CD` |
    | 4 | `B → D` | giả thiết | đưa phụ thuộc chứa `D` vào |
    | 5 | `A → D` | bắc cầu (2, 4) | nối `A → B → D` |
    | 6 | `A → CD` | hợp (3, 5) | gộp `C` và `D` để khớp đúng vế trái của `CD → E` |
    | 7 | `CD → E` | giả thiết | đưa phụ thuộc đích vào |
    | 8 | `A → E` | bắc cầu (6, 7) | nối `A → CD → E`, hoàn tất chứng minh |

!!! example "Ví dụ 5.4 — Khi vế trái thiếu thuộc tính: so sánh Bắc cầu giả và Tăng trưởng"

    Cho `R(A, B, C, D)` và `F = {A → B, BC → D}`. Chứng minh `AC → D` bằng **hai cách**: *(a)* dùng sáu luật; *(b)* chỉ dùng ba luật gốc.

    *Hướng suy nghĩ:* Từ `A` ta suy được `B`, nhưng phụ thuộc thứ hai lại đòi cả cụm `BC` mới suy ra `D`. Vế trái đang thiếu `C` — đây chính là dấu hiệu dùng **luật bắc cầu giả** (hoặc **luật tăng trưởng** với `C` nếu chỉ được dùng ba luật gốc).

    | Cách (a) — Dùng sáu luật *(nhanh gọn)* | | | | Cách (b) — Chỉ dùng ba luật gốc *(khi đề bắt buộc)* | | |
    |:--:|---|---|:--:|:--:|---|---|
    | **Bước** | **Suy luận** | **Luật dùng** | | **Bước** | **Suy luận** | **Luật dùng** |
    | 1 | `A → B` | giả thiết | | 1 | `A → B` | giả thiết |
    | 2 | `BC → D` | giả thiết | | 2 | `AC → BC` | tăng trưởng (1) với `C` |
    | 3 | `AC → D` | bắc cầu giả (1, 2) với `W = C` | | 3 | `BC → D` | giả thiết |
    | | | | | 4 | `AC → D` | bắc cầu (2, 3) |

    *Kinh nghiệm làm bài:* Mọi chỗ dùng **bắc cầu giả** đều có thể thay bằng một bước **tăng trưởng** cộng một bước **bắc cầu**. Tương tự, mọi chỗ dùng **luật tách** đều thay được bằng **phản xạ** cộng **bắc cầu**. Nhớ quy tắc quy đổi này, người học không bao giờ sợ câu hỏi yêu cầu *"chỉ dùng ba tiên đề gốc"*.

!!! example "Ví dụ 5.5 — Suy diễn trên bài toán nghiệp vụ Trung tâm Anh ngữ ABC"

    Phòng Đào tạo của Trung tâm ABC quản lý lịch học theo ba quy tắc nghiệp vụ sau trên quan hệ `LICHHOC(MALOP, MAGV, MAKH, CAHOC, PHONG, DAYNHA)`:

    - `f₁: MALOP → MAGV, MAKH` *(mỗi lớp do một giáo viên phụ trách và thuộc một khóa học)*
    - `f₂: (MAGV, CAHOC) → PHONG` *(trong một ca học, mỗi giáo viên chỉ dạy tại một phòng)*
    - `f₃: PHONG → DAYNHA` *(mỗi phòng học nằm ở một dãy nhà cố định)*

    Hãy dùng hệ luật Armstrong để chứng minh `(MALOP, CAHOC) → DAYNHA` và giải thích ý nghĩa nghiệp vụ của kết quả.

    | Bước | Suy luận | Luật dùng | Diễn giải theo nghiệp vụ |
    |:--:|---|---|---|
    | 1 | `MALOP → MAGV, MAKH` | giả thiết `f₁` | biết mã lớp thì biết giáo viên và khóa học |
    | 2 | `MALOP → MAGV` | tách (1) | giữ lại thông tin giáo viên phụ trách lớp |
    | 3 | `(MAGV, CAHOC) → PHONG` | giả thiết `f₂` | biết giáo viên và ca học thì biết phòng học |
    | 4 | `(MALOP, CAHOC) → PHONG` | bắc cầu giả (2, 3) với `W = CAHOC` | suy ra: biết lớp và ca học thì xác định được phòng học |
    | 5 | `PHONG → DAYNHA` | giả thiết `f₃` | biết phòng học thì biết dãy nhà |
    | 6 | `(MALOP, CAHOC) → DAYNHA` | bắc cầu (4, 5) | kết luận: biết lớp và ca học thì biết chắc lớp học ở dãy nhà nào |

    *Ý nghĩa thiết kế:* Dù quy tắc ban đầu không hề nhắc tới mối liên hệ giữa lớp học và dãy nhà, hệ luật Armstrong chỉ ra rằng `DAYNHA` phụ thuộc bắc cầu vào `(MALOP, CAHOC)` qua trung gian `PHONG`. Nếu lưu `DAYNHA` trực tiếp trong bảng lịch học theo ca, mỗi lần phòng P201 được lặp lại ở nhiều ca học thì tên dãy nhà sẽ bị chép lặp bấy nhiêu lần.

## 5.3.4. Ba ngụy biện thường gặp khi áp luật Armstrong

Khi làm bài tập suy diễn, người học rất hay "tự chế" ra những quy tắc trông có vẻ hợp lý trên mặt chữ nhưng **hoàn toàn sai về mặt toán học**. Có ba ngụy biện phổ biến nhất cần gạch đỏ ngay từ đầu.

**Bảng 5.9. Ba ngụy biện thường gặp khi suy diễn bằng luật Armstrong**

| Ngụy biện *(luật SAI)* | Vì sao người học hay nhầm | Quy tắc ĐÚNG tương ứng | Cách nhớ để không bao giờ sai |
|---|---|---|---|
| **1. Tách vế trái (SAI)**<br/>`XY → Z` ⟹ `X → Z` và `Y → Z` | Nhầm với **luật tách (IR5)** `X → YZ ⟹ X → Y, X → Z` | Chỉ được **tách vế phải**, tuyệt đối **không được tách vế trái**. Ngược lại, vế trái chỉ có thể **mở rộng thêm** (`X → Z ⟹ XY → Z`, do tăng trưởng với `Y` rồi tách) | Ổ khóa hai chìa `(X, Y)` mới mở được két `Z` — cầm một chìa `X` không mở được! |
| **2. Đảo chiều (SAI)**<br/>`X → Y` ⟹ `Y → X` | Nhầm mũi tên phụ thuộc hàm `→` với dấu bằng `=` trong đại số | Phụ thuộc hàm **có chiều** *(mục 3.2.2)*. `X → Y` và `Y → X` là hai khẳng định độc lập; chỉ khi cả hai cùng được nghiệp vụ cho phép mới có hai chiều | Biết mã lớp biết giáo viên (`MALOP → MAGV`), nhưng biết giáo viên GV1 không suy ra được lớp nào vì cô dạy ba lớp |
| **3. Khử hai vế (SAI)**<br/>`XZ → YZ` ⟹ `X → Y` | Làm ngược **luật tăng trưởng (IR2)**, tưởng "rút gọn" được `Z` ở hai bên như phương trình số học | Tăng trưởng chỉ đi **một chiều**: từ `X → Y` thêm `Z` vào hai vế thành `XZ → YZ`, **không có chiều bớt `Z` đi** | Có thêm `Z` giúp xác định được `Y` không có nghĩa bỏ `Z` đi một mình `X` vẫn xác định được `Y` |

Để thấy rõ vì sao ba ngụy biện trên đều sai, không gì thuyết phục hơn nhìn thẳng vào bảng dữ liệu thực tế của Trung tâm ABC. Bảng dưới đây dùng chính bốn dòng dữ liệu quen thuộc của `GHIDANH_MORONG` để bác bỏ cả ba.

**Bảng 5.10. Dữ liệu `GHIDANH_MORONG` bác bỏ cả ba ngụy biện suy diễn**

| MAHV | MALOP | HOTEN | MAGV | HOCPHI |
|---|---|---|---|---|
| **HV01** | **A1** | Trần An | **GV1** | **2.000.000** |
| **HV01** | **A2** | Trần An | GV2 | **2.500.000** |
| HV02 | **A3** | Lê Bình | **GV1** | 2.200.000 |
| HV03 | A1 | **Trần An** | GV1 | 2.000.000 |

| Ngụy biện bị kiểm nghiệm | Giả thiết ĐÚNG trên bảng | Kết luận SAI nếu áp ngụy biện | Dòng dữ liệu vạch trần chỗ sai *(phản ví dụ)* |
|---|---|---|---|
| **Tách vế trái** | `(MAHV, MALOP) → HOCPHI` *(mỗi cặp học viên – lớp có một mức học phí)* | Tưởng suy ra được `MAHV → HOCPHI` | Hai dòng đầu có cùng **`MAHV = HV01`** nhưng `HOCPHI` lại là **`2.000.000`** *(lớp A1)* và **`2.500.000`** *(lớp A2)* — một mình `MAHV` không xác định được học phí |
| **Đảo chiều** | `MAHV → HOTEN` và `MALOP → MAGV` | Tưởng suy ra được `HOTEN → MAHV` hoặc `MAGV → MALOP` | Dòng 1 và dòng 4 cùng **`HOTEN = Trần An`** nhưng là hai học viên `HV01` và `HV03`; dòng 1 và dòng 3 cùng **`MAGV = GV1`** nhưng dạy hai lớp **`A1`** và **`A3`** |
| **Khử hai vế** | `(MAHV, MALOP) → (MAGV, MALOP)` *(suy từ `MALOP → MAGV` bằng luật tăng trưởng với `MAHV`, rồi hợp)* | Tưởng bỏ `MALOP` ở hai vế thì được `MAHV → MAGV` | Dòng 1 và dòng 2 có cùng **`MAHV = HV01`** nhưng học với hai giáo viên khác nhau là **`GV1`** và **`GV2`** — bỏ `MALOP` đi là mất ngay sự thật |

!!! warning "Chú ý — quy tắc mở rộng vế trái (luật tích lũy vế trái)"

    Tuy **không được bớt** thuộc tính ở vế trái (`XY → Z` không suy ra `X → Z`), ta lại **luôn được phép thêm** thuộc tính bất kỳ vào vế trái:

    Nếu `X → Z` thì `XY → Z` *(với mọi tập thuộc tính `Y`)*.

    *Chứng minh trong hai bước:* Từ `X → Z`, áp luật tăng trưởng với `Y` được `XY → YZ`; áp tiếp luật tách cho vế phải `YZ` được `XY → Z`. Quy tắc này rất dễ hiểu: nếu một chìa `X` đã mở được ổ khóa `Z`, thì cầm chùm chìa `XY` *(có sẵn chìa `X` trong đó)* đương nhiên vẫn mở được `Z`.

## 5.3.5. Bài tập mẫu có lời giải từng bước

Năm bài tập dưới đây bao quát các dạng câu hỏi thường gặp nhất về hệ luật dẫn Armstrong trong bài kiểm tra và đề thi kết thúc học phần: từ suy diễn cơ bản, rút gọn thuộc tính thừa, chứng minh chỉ bằng ba luật gốc, phát hiện lỗi ngụy biện, cho tới vận dụng trên bài toán nghiệp vụ. Người học nên tự giải ra nháp trước khi đọc bảng lời giải.

---

### Bài tập mẫu 5.1 — Suy diễn nhiều chặng và rút gọn thuộc tính thừa ở vế trái

**Đề bài.** Cho lược đồ quan hệ `R(A, B, C, D, E)` và tập phụ thuộc hàm `F = {A → B, AB → C, C → D, BD → E}`. Bằng hệ luật dẫn Armstrong, hãy chứng minh:

a) `A → C`
b) `A → E`

**Phân tích hướng giải.**

- Ở câu (a), giả thiết cho `AB → C` *(cần cả `A` và `B` mới suy ra `C`)*, nhưng đồng thời lại cho `A → B` *(bản thân `A` đã suy ra `B`)*. Vậy thực chất chỉ cần một mình `A` là đủ suy ra `C`. Để nối `A → B` vào `AB → C`, ta dùng **luật bắc cầu giả** với `W = A` *(vì `AA = A`)*, hoặc tăng trưởng `A → B` với `A` thành `A → AB` rồi bắc cầu.
- Ở câu (b), muốn có `A → E` thì nhìn vào `BD → E`: ta cần chứng minh `A → BD`, tức cần `A → B` *(đã có)* và `A → D`. Mà `A → D` nối được từ kết quả câu (a) `A → C` và giả thiết `C → D`.

**Lời giải chi tiết.**

*Câu a) Chứng minh `A → C`:*

| Bước | Suy luận | Luật dùng | Ghi chú |
|:--:|---|---|---|
| 1 | `A → B` | giả thiết | xuất phát từ `A` |
| 2 | `A → AB` | tăng trưởng (1) với `A` *(hoặc hợp `A → A` và `A → B`)* | vì `A ∪ A = A`, ghép thêm `A` vào vế phải để khớp `AB` |
| 3 | `AB → C` | giả thiết | phụ thuộc có vế trái `AB` |
| 4 | `A → C` | bắc cầu (2, 3) | nối `A → AB → C` *(hoặc áp thẳng bắc cầu giả cho 1 và 3 với `W = A`)* |

*Câu b) Chứng minh `A → E`:*

| Bước | Suy luận | Luật dùng | Ghi chú |
|:--:|---|---|---|
| 5 | `C → D` | giả thiết | cầu nối từ `C` sang `D` |
| 6 | `A → D` | bắc cầu (4, 5) | nối kết quả câu (a) `A → C` với `C → D` |
| 7 | `A → BD` | hợp (1, 6) | gộp `A → B` và `A → D` để tạo đúng vế trái `BD` |
| 8 | `BD → E` | giả thiết | đưa phụ thuộc đích vào |
| 9 | `A → E` | bắc cầu (7, 8) | nối `A → BD → E`, hoàn tất chứng minh |

> **Nhận xét nối sang mục 5.6.** Câu (a) cho thấy một ý rất quan trọng: khi trong `F` có `A → B`, thì thuộc tính `B` ở vế trái của `AB → C` là **thuộc tính thừa** — ta có thể thay `AB → C` bằng `A → C` gọn hơn mà không làm thay đổi những gì suy ra được. Đây chính là bản chất của **Bước 2 (loại thuộc tính thừa ở vế trái)** trong thuật toán tìm phủ tối thiểu ở mục 5.6.3.

---

### Bài tập mẫu 5.2 — Chứng minh bằng sáu luật so với chỉ dùng ba luật gốc

**Đề bài.** Cho lược đồ `R(A, B, C, D, E, F)` và tập phụ thuộc hàm `F = {AB → C, BC → AD, D → E, CF → B}`.

a) Chứng minh `AB → D` bằng **hai cách**: *(Cách 1)* được dùng cả sáu luật; *(Cách 2)* **chỉ được dùng ba luật gốc** *(phản xạ, tăng trưởng, bắc cầu)*.
b) Chứng minh `AB → E` và `ACF → D`.

**Phân tích hướng giải.**

- Ở câu (a), từ `AB → C` và `BC → AD`, ta thấy `C` ở vế phải của phụ thuộc đầu nằm trong vế trái `BC` của phụ thuộc sau (thiếu `B`, mà `B` đã có sẵn trong `AB`). Khi dùng sáu luật, ta áp **bắc cầu giả** rồi **tách** vế phải `AD` lấy `D`. Khi chỉ được dùng ba luật gốc, ta thay bắc cầu giả bằng **tăng trưởng** với `B` (`AB → C ⟹ ABB → BC`, mà `ABB = AB`), và thay luật tách bằng **phản xạ** (`AD → D`) cộng **bắc cầu**.
- Ở câu (b), `AB → E` suy ngay từ `AB → D` và `D → E`. Còn với `ACF → D`: trong `ACF` có `CF`, mà `CF → B` cho phép suy ra `B`; ghép với `A` sẵn có sẽ quay về bài toán của `AB → D`!

**Lời giải chi tiết.**

*Câu a) Chứng minh `AB → D` bằng hai cách:*

| Bước | **Cách 1 — Dùng cả sáu luật** | Luật dùng | | Bước | **Cách 2 — Chỉ dùng ba luật gốc (IR1, IR2, IR3)** | Luật dùng |
|:--:|---|---|:--:|:--:|---|---|
| 1 | `AB → C` | giả thiết | | 1 | `AB → C` | giả thiết |
| 2 | `BC → AD` | giả thiết | | 2 | `AB → BC` | tăng trưởng (1) với `B` *(vì `ABB = AB`)* |
| 3 | `AB → AD` | bắc cầu giả (1, 2) với `W = B` *(vì `BB = B`)* | | 3 | `BC → AD` | giả thiết |
| 4 | `AB → D` | tách (3) | | 4 | `AB → AD` | bắc cầu (2, 3) |
| | | | | 5 | `AD → D` | phản xạ *(vì `D ⊆ AD`)* |
| | | | | 6 | `AB → D` | bắc cầu (4, 5) |

*Câu b) Chứng minh `AB → E` và `ACF → D`:*

| Bước | Suy luận | Luật dùng | Giải thích |
|:--:|---|---|---|
| 1 | `AB → D` | chứng minh ở câu (a) | điểm xuất phát cho nhánh thứ nhất |
| 2 | `D → E` | giả thiết | — |
| 3 | `AB → E` | bắc cầu (1, 2) | **xong ý thứ nhất** (`AB → E`) |
| 4 | `CF → B` | giả thiết | bắt đầu nhánh thứ hai để chứng minh `ACF → D` |
| 5 | `ACF → D` | bắc cầu giả (4, 1) với `W = A` | thay `B` trong vế trái của `AB → D` *(bước 1)* bằng `CF` → được `ACF → D` **(xong ý thứ hai)** |

---

### Bài tập mẫu 5.3 — Suy diễn trên tập phụ thuộc có chu trình và gộp nhiều nhánh

**Đề bài.** Cho lược đồ `R(A, B, C, D, E, H)` và tập phụ thuộc hàm `F = {A → B, BC → D, D → E, E → A, AH → C}`. Hãy chứng minh bằng hệ luật Armstrong:

a) `D → B`
b) `CE → D`
c) `EH → D`

**Phân tích hướng giải.**

Nhìn vào `F`, ta phát hiện một chuỗi đi vòng: `D → E → A → B`, rồi `B` ghép với `C` lại quay về `D` (`BC → D`).

- Câu (a) đi dọc theo chuỗi đơn: `D → E → A → B` (hai lần bắc cầu).
- Câu (b) có vế trái `CE`: từ `E` đi qua `A` sẽ lấy được `B` (`E → A → B`), ghép với `C` sẵn có ở vế trái sẽ đủ bộ `BC` để kích hoạt `BC → D`.
- Câu (c) có vế trái `EH`: từ `E → A` và `AH → C`, áp bắc cầu giả được `EH → C`. Khi đã có cả `EH → C` và `E → B`, ta gộp lại để đi vào `BC → D` (hoặc nối vào kết quả `CE → D` của câu b)!

**Lời giải chi tiết.**

| Phần | Bước | Suy luận | Luật dùng | Giải thích |
|---|:--:|---|---|---|
| **Câu a)**<br/>`D → B` | 1<br/>2<br/>3<br/>4<br/>5 | `D → E`<br/>`E → A`<br/>`D → A`<br/>`A → B`<br/>`D → B` | giả thiết<br/>giả thiết<br/>bắc cầu (1, 2)<br/>giả thiết<br/>bắc cầu (3, 4) | —<br/>—<br/>nối `D → E → A`<br/>—<br/>nối `D → A → B` **(xong câu a)** |
| **Câu b)**<br/>`CE → D` | 6<br/>7<br/>8<br/>9 | `E → B`<br/>`BC → D`<br/>`CE → D`<br/>— | bắc cầu (2, 4)<br/>giả thiết<br/>bắc cầu giả (6, 7) với `W = C`<br/>— | nối `E → A → B`<br/>cần `BC` ở vế trái<br/>thay `B` trong `BC` bằng `E` → `CE → D` **(xong câu b)**<br/>— |
| **Câu c)**<br/>`EH → D` | 10<br/>11<br/>12 | `AH → C`<br/>`EH → C`<br/>`EH → D` | giả thiết<br/>bắc cầu giả (2, 10) với `W = H`<br/>bắc cầu giả (11, 8) với `W = E` | —<br/>từ `E → A` và `AH → C` suy ra `EH → C`<br/>từ `EH → C` và `CE → D` *(bước 8)* suy ra `EEH → D`, tức `EH → D` **(xong câu c)** |

---

### Bài tập mẫu 5.4 — Bắt lỗi lời giải sai và dựng bảng dữ liệu phản ví dụ

**Đề bài.** Cho lược đồ `R(A, B, C, D)` và tập phụ thuộc hàm `F = {AB → C, C → D, D → B}`.

a) Chứng minh `AB → D`.
b) Một bạn sinh viên khẳng định rằng từ `F` cũng suy ra được `A → D` và trình bày lời giải 4 bước sau:
   - Bước 1: `AB → C` *(giả thiết)*
   - Bước 2: `A → C` *(áp luật tách cho bước 1)*
   - Bước 3: `C → D` *(giả thiết)*
   - Bước 4: `A → D` *(áp luật bắc cầu cho bước 2 và bước 3)*

   Hỏi: Lời giải của bạn ấy **sai ở bước nào** và mắc ngụy biện gì? Hãy dựng một bảng dữ liệu gồm **2 dòng** cho `R(A, B, C, D)` sao cho thỏa mãn cả ba phụ thuộc trong `F` nhưng vi phạm `A → D` *(để chứng minh rằng không thể nào suy ra `A → D` từ `F`)*.

**Lời giải chi tiết.**

*Câu a) Chứng minh `AB → D`:*

| Bước | Suy luận | Luật dùng |
|:--:|---|---|
| 1 | `AB → C` | giả thiết |
| 2 | `C → D` | giả thiết |
| 3 | `AB → D` | bắc cầu (1, 2) |

*Câu b) Chỉ ra lỗi sai và lập bảng phản ví dụ:*

- **Chỗ sai:** Lời giải sai ngay ở **Bước 2** (`AB → C ⟹ A → C`). Bạn sinh viên đã mắc **ngụy biện tách vế trái** *(mục 5.3.4)*: luật tách của Armstrong chỉ cho phép tách **vế phải** (`X → YZ ⟹ X → Y`), không bao giờ cho phép bỏ bớt thuộc tính `B` khỏi vế trái `AB`.
- **Dựng bảng phản ví dụ 2 dòng:** Muốn bác bỏ `A → D`, ta cần hai dòng có **cùng giá trị `A`** nhưng **khác giá trị `D`**, đồng thời vẫn tuân thủ nghiêm ngặt `AB → C`, `C → D` và `D → B` *(nghĩa là nếu hai dòng khác `D` thì chúng phải khác `B` và khác `C`)*.

| Dòng | A | B | C | D | Kiểm tra tập `F = {AB → C, C → D, D → B}` |
|:--:|:--:|:--:|:--:|:--:|---|
| 1 | **`a₁`** | `b₁` | `c₁` | **`d₁`** | Hai dòng có cặp `(A, B)` khác nhau (`(a₁, b₁) ≠ (a₁, b₂)`), giá trị `C` khác nhau (`c₁ ≠ c₂`), giá trị `D` khác nhau (`d₁ ≠ d₂`) → **không có bất kỳ hai dòng nào trùng vế trái**, nên cả ba phụ thuộc `AB → C`, `C → D`, `D → B` đều **thỏa mãn tuyệt đối** |
| 2 | **`a₁`** | `b₂` | `c₂` | **`d₂`** | Tuy nhiên, hai dòng có **cùng `A = a₁`** mà lại nhận **hai giá trị `D` khác nhau (`d₁ ≠ d₂`)** → phụ thuộc **`A → D` bị vi phạm** |

Bảng 2 dòng trên là bằng chứng không thể chối cãi: tồn tại một thể hiện hợp lệ của `R` thỏa mãn toàn bộ `F` nhưng không thỏa `A → D`. Do hệ luật Armstrong là đúng đắn, không một chuỗi suy diễn hợp lệ nào có thể dẫn tới `A → D`.

---

### Bài tập mẫu 5.5 — Bài toán nghiệp vụ thực tế: Phân công giảng dạy và phòng học

**Đề bài.** Một trường đại học quản lý lịch giảng dạy bằng lược đồ `LICHDAY(MALOP, MAMH, TENMH, SOTC, MAGV, CAHOC, PHONG)` với tập phụ thuộc hàm `F` rút từ bốn quy tắc nghiệp vụ:

- `f₁: MAMH → TENMH, SOTC` *(mỗi mã môn học có một tên môn và một số tín chỉ)*
- `f₂: MALOP → MAMH, MAGV` *(mỗi lớp học phần thuộc một môn học và do một giảng viên phụ trách)*
- `f₃: (MAGV, CAHOC) → PHONG` *(tại một ca học, một giảng viên chỉ dạy ở một phòng)*
- `f₄: (PHONG, CAHOC) → MALOP` *(tại một ca học, một phòng chỉ bố trí cho một lớp học phần)*

Dùng hệ luật dẫn Armstrong để chứng minh các phụ thuộc hàm sau và nêu ý nghĩa nghiệp vụ của từng kết quả:

a) `MALOP → TENMH, SOTC`
b) `(MALOP, CAHOC) → PHONG`
c) `(PHONG, CAHOC) → MAGV`

**Lời giải chi tiết.**

| Câu | Bước | Suy luận | Luật dùng | Ý nghĩa nghiệp vụ |
|---|:--:|---|---|---|
| **a)** | 1<br/>2<br/>3<br/>4 | `MALOP → MAMH, MAGV`<br/>`MALOP → MAMH`<br/>`MAMH → TENMH, SOTC`<br/>`MALOP → TENMH, SOTC` | giả thiết `f₂`<br/>tách (1)<br/>giả thiết `f₁`<br/>bắc cầu (2, 3) | Biết mã lớp học phần thì biết môn học của lớp đó, suy ra biết luôn tên môn và số tín chỉ *(đây là phụ thuộc bắc cầu qua `MAMH`, báo hiệu phải tách bảng `MONHOC`)* |
| **b)** | 5<br/>6<br/>7 | `MALOP → MAGV`<br/>`(MAGV, CAHOC) → PHONG`<br/>`(MALOP, CAHOC) → PHONG` | tách (1)<br/>giả thiết `f₃`<br/>bắc cầu giả (5, 6) với `W = CAHOC` | Biết lớp học phần thì biết giảng viên dạy lớp đó; kết hợp với ca học sẽ xác định duy nhất phòng học của lớp trong ca ấy |
| **c)** | 8<br/>9 | `(PHONG, CAHOC) → MALOP`<br/>`(PHONG, CAHOC) → MAGV` | giả thiết `f₄`<br/>bắc cầu (8, 5) | Tại một phòng trong một ca học chỉ có một lớp học phần, mà mỗi lớp do một giảng viên dạy, nên nhìn vào phòng và ca học là biết ngay giảng viên nào đang đứng lớp |

---

## 5.3.6. Vì sao cần hệ luật này — và khi nào chuyển sang bao đóng

Có hai lý do thực dụng khiến người thiết kế phải nắm vững hệ luật Armstrong.

Thứ nhất, nó cho phép **phát hiện các phụ thuộc bắc cầu và dư thừa ẩn**. Nhìn vào `F = {MALOP → MAGV, MAGV → HOTEN_GV}` hay `{MALOP → MAMH, MAMH → TENMH}` ở Bài tập mẫu 5.5, từng phụ thuộc riêng lẻ trông hoàn toàn tự nhiên, nhưng luật bắc cầu chỉ ra `MALOP → HOTEN_GV` và `MALOP → TENMH` — chính là các vi phạm 3NF. Không có hệ luật này, người thiết kế phải dò tìm bằng mắt, tức lại quay về trực giác.

Thứ hai, hệ luật Armstrong là **nền tảng toán học của thuật toán bao đóng** ở mục 5.4 ngay sau đây. Khi làm năm bài tập mẫu ở trên, người học có thể nhận thấy:

- Để chứng minh một phụ thuộc **suy ra được** (`X → Y`), ta nối từng bước bằng luật Armstrong rất tường minh.
- Nhưng nếu đề hỏi *"Cho `F`, phụ thuộc `A → D` có suy ra được không?"* (như câu b Bài tập mẫu 5.4), việc tìm mãi không ra cách nối chưa phải là chứng minh — biết đâu có cách nối mà ta chưa nghĩ ra? Muốn trả lời dứt khoát cả câu hỏi *"có"* lẫn câu hỏi *"không"* một cách tự động, ta cần gom toàn bộ những gì `X` suy ra được bằng luật Armstrong vào một tập hợp duy nhất. Tập hợp ấy chính là **bao đóng `X⁺`** ở mục 5.4.

!!! question "Tự kiểm tra 5.3"

    *(tự trả lời trước, rồi mở đáp án bên dưới)*

    1. Cho `F = {A → B, BC → D, D → E}`. Để chứng minh `AC → E`, một bạn lập bảng suy diễn: *(1)* `A → B` (giả thiết); *(2)* `AC → BC` (…); *(3)* `BC → D` (giả thiết); *(4)* `AC → D` (…); *(5)* `D → E` (giả thiết); *(6)* `AC → E` (…). Hãy điền tên luật gốc Armstrong đã dùng ở các bước (2), (4), (6), và cho biết có thể gộp bước (1)–(4) bằng một luật dẫn xuất nào.
    2. Cho `R(A, B, C, D, E)` và `F = {A → BC, CD → E, B → D}`. Hãy lập bảng suy diễn từng bước bằng hệ luật Armstrong để chứng minh `A → E`.
    3. Vì sao từ `X → YZ` ta tách được `X → Y` và `X → Z`, nhưng từ `XY → Z` lại **không bao giờ** tách được `X → Z`? Giải thích bằng cả luật Armstrong lẫn ví dụ thực tế trên bảng `GHIDANH(MAHV, MALOP, HOCPHI)`.

??? success "Đáp án tự kiểm tra 5.3"

    *(1)* Bước (2): **luật tăng trưởng** *(áp cho bước 1 với `C`)*; bước (4): **luật bắc cầu** *(giữa bước 2 và bước 3)*; bước (6): **luật bắc cầu** *(giữa bước 4 và bước 5)*. Các bước (1)–(4) có thể gộp ngay thành một bước bằng **luật bắc cầu giả** *(từ `A → B` và `BC → D` suy ra `AC → D` với `W = C`)*. *(2)* Bảng 8 bước: *(1)* `A → BC` (giả thiết); *(2)* `A → B` (tách 1); *(3)* `A → C` (tách 1); *(4)* `B → D` (giả thiết); *(5)* `A → D` (bắc cầu 2, 4); *(6)* `A → CD` (hợp 3, 5); *(7)* `CD → E` (giả thiết); *(8)* `A → E` (bắc cầu 6, 7). *(3)* Với `X → YZ`, ta có `YZ → Y` theo **luật phản xạ** *(vì `Y ⊆ YZ`)*, nên bắc cầu `X → YZ → Y` cho `X → Y`. Ngược lại, với `XY → Z`, muốn bắc cầu từ `X` sang `XY` thì phải có `X → XY`, mà `XY` không phải tập con của `X` nên luật phản xạ không áp dụng được. Trên `GHIDANH(MAHV, MALOP, HOCPHI)`, cả cặp `(MAHV, MALOP) → HOCPHI` là đúng, nhưng một mình `MAHV → HOCPHI` là sai vì một học viên `HV01` đăng ký hai lớp `A1`, `A2` có hai mức học phí khác nhau.

---


---

[← Trang trước](5-2-ba-loai-phu-thuoc-ham.md) · [Trang sau →](5-4-bao-dong-cua-tap-thuoc-tinh.md)
