# 3.6. Các phép toán tập hợp

*(1,0 tiết)*

## 3.6.1. Điều kiện khả hợp

Ba phép toán `∪`, `∩`, `−` chỉ áp dụng được khi hai quan hệ **tương thích với nhau về cấu trúc**.

!!! note "Định nghĩa 3.9"

    Hai quan hệ `R` và `S` gọi là **khả hợp** *(union-compatible)* nếu thỏa mãn **đồng thời hai điều kiện**:

    1. Chúng có **cùng bậc** — tức cùng số thuộc tính.
    2. Các thuộc tính **tương ứng theo thứ tự** có **cùng miền giá trị**.

Điều kiện thứ hai nói *"cùng miền giá trị"* chứ không nói *"cùng tên"*. Tên thuộc tính có thể khác nhau; điều quan trọng là chúng chứa **cùng loại dữ liệu**.

!!! example "Ví dụ 3.10"

    Hai quan hệ `HOCVIEN_CS1(MAHV, HOTEN)` và `HOCVIEN_CS2(MA, TEN)` là **khả hợp**: cùng bậc 2, và cặp thuộc tính tương ứng cùng miền giá trị *(mã học viên và họ tên)*. Ngược lại, `HOCVIEN(MAHV, HOTEN, NGAYSINH)` và `LOP(MALOP, TENLOP)` **không khả hợp** vì khác bậc.

Đặt các bảng cạnh nhau, **cột nào thẳng hàng với cột nào** là thấy ngay câu trả lời.

**Bảng 3.18. Kiểm tra khả hợp bằng cách xếp cột thẳng hàng**

| | Cột 1 | Cột 2 | Cột 3 | Khả hợp với `HOCVIEN_CS1`? |
|---|---|---|---|:--:|
| `HOCVIEN_CS1` | `MAHV` *(mã học viên)* | `HOTEN` *(họ tên)* | — | — |
| `HOCVIEN_CS2` | `MA` *(mã học viên)* | `TEN` *(họ tên)* | — | ✓ cùng bậc, cột tương ứng cùng miền — **tên khác không sao** |
| `LOP` | `MALOP` *(mã lớp)* | `TENLOP` *(tên lớp)* | — | ✗ cùng bậc nhưng cột 1 là mã **lớp**, không phải mã học viên — **khác miền** |
| `HOCVIEN` | `MAHV` | `HOTEN` | `NGAYSINH` | ✗ **khác bậc** — thừa một cột |

Điều kiện này không phải là hình thức. Nếu hợp hai bảng khác cấu trúc, kết quả sẽ là một bảng mà các dòng có **số cột khác nhau** hoặc **ý nghĩa cột lệch nhau** — không còn là một quan hệ hợp lệ, vi phạm Đặc trưng 3 và 5 ở mục 3.1.3.

## 3.6.2. Hợp, giao và hiệu

!!! note "Định nghĩa 3.10"

    Cho hai quan hệ **khả hợp** `R` và `S`:

    - **Hợp** `R ∪ S`: mọi bộ thuộc `R` **hoặc** thuộc `S` *(bộ trùng chỉ lấy một lần)*.
    - **Giao** `R ∩ S`: các bộ thuộc **cả** `R` **và** `S`.
    - **Hiệu** `R − S`: các bộ thuộc `R` **nhưng không** thuộc `S`.

    Viết bằng công thức: `R ∪ S = { t | t ∈ R hoặc t ∈ S }`; `R ∩ S = { t | t ∈ R và t ∈ S }`; `R − S = { t | t ∈ R và t ∉ S }`. Chữ **"hoặc / và / và không"** trong ba công thức chính là chữ cần bắt lấy khi đọc một yêu cầu bằng lời.

!!! example "Ví dụ 3.11"

    Trung tâm ABC có hai cơ sở. Gọi `A` là tập học viên cơ sở 1, `B` là tập học viên cơ sở 2, cả hai cùng cấu trúc `(MAHV, HOTEN)`.

    | Yêu cầu nghiệp vụ | Biểu thức |
    |---|---|
    | Danh sách **toàn bộ** học viên của trung tâm | `A ∪ B` |
    | Học viên **học ở cả hai** cơ sở | `A ∩ B` |
    | Học viên **chỉ học ở cơ sở 1** | `A − B` |

Tính thử trên dữ liệu — mỗi cơ sở ba học viên, trong đó Lê Bình học ở cả hai.

**Bảng 3.19. Bốn phép toán tập hợp tính trên hai bảng khả hợp `A` và `B`**

*Đầu vào:*

| `A` — cơ sở 1 | MAHV | HOTEN |
|---|---|---|
| | HV01 | Trần An |
| | HV02 | Lê Bình |
| | HV03 | Phạm Cường |

| `B` — cơ sở 2 | MAHV | HOTEN |
|---|---|---|
| | HV02 | Lê Bình |
| | HV04 | Ngô Dung |
| | HV05 | Vũ Em |

*Kết quả:*

| `A ∪ B` *(5 bộ — Lê Bình chỉ một lần)* | `A ∩ B` *(1 bộ)* | `A − B` *(2 bộ)* | `B − A` *(2 bộ)* |
|---|---|---|---|
| HV01 Trần An | HV02 Lê Bình | HV01 Trần An | HV04 Ngô Dung |
| HV02 Lê Bình | | HV03 Phạm Cường | HV05 Vũ Em |
| HV03 Phạm Cường | | | |
| HV04 Ngô Dung | | | |
| HV05 Vũ Em | | | |

Cần lưu ý rằng **phép hiệu không giao hoán**: `A − B` khác `B − A` — hai cột cuối của bảng trên cho hai danh sách hoàn toàn khác nhau. `A − B` cho học viên chỉ ở cơ sở 1, còn `B − A` cho học viên chỉ ở cơ sở 2. Trong khi đó `∪` và `∩` đều giao hoán. Cũng nên để ý `A ∪ B` có **5** bộ chứ không phải 3 + 3 = 6: Lê Bình có mặt ở cả hai bảng nhưng chỉ được lấy **một lần**, đúng tinh thần tập hợp.

## 3.6.3. Tích Descartes — phép duy nhất không đòi hỏi khả hợp

!!! note "Định nghĩa 3.11"

    **Tích Descartes** *(Cartesian product)* `R × S` ghép **mỗi bộ của `R` với mọi bộ của `S`**. Nếu `R` có bậc `m` và lực lượng `p`, còn `S` có bậc `n` và lực lượng `q`, thì `R × S` có **bậc `m + n`** và **lực lượng `p × q`**.

![](../hinh-ve/slide/internet/thuc_don_combo.jpg){width=60%}

*Ảnh minh họa: bảng thực đơn đồ ăn nhanh. Ba món chính và hai đồ uống cho sáu combo khả dĩ, kể cả combo chẳng ai gọi — tích Descartes ghép cơ học mọi cặp đúng như thế — Nguồn: Wikimedia Commons · Dave O · CC BY-SA 2.0.*

Tích Descartes được xếp vào **nhóm phép toán tập hợp** vì nó kế thừa trực tiếp từ lý thuyết tập hợp, giống ba phép trên. Nhưng nó **khác ba phép kia ở một điểm căn bản**, và đây là chỗ người học hay nhầm.

**Ba phép `∪`, `∩`, `−` đòi hỏi khả hợp; tích Descartes thì không.** Lý do nằm ở bản chất phép toán. Ba phép đầu **so sánh các bộ với nhau** để quyết định giữ hay bỏ, nên hai bộ phải có cùng cấu trúc mới so sánh được. Tích Descartes **không so sánh gì cả** — nó chỉ nối hai bộ lại thành một bộ dài hơn, nên hai quan hệ đầu vào có cấu trúc thế nào cũng được.

**Bảng 3.20. Bốn phép toán tập hợp — đối chiếu**

| Phép toán | Đòi hỏi khả hợp? | Bậc kết quả | Lực lượng kết quả |
|---|:--:|---|---|
| Hợp `∪` | **Có** | Bằng bậc đầu vào | ≤ `p + q` *(bỏ trùng)* |
| Giao `∩` | **Có** | Bằng bậc đầu vào | ≤ min(`p`, `q`) |
| Hiệu `−` | **Có** | Bằng bậc đầu vào | ≤ `p` |
| **Tích Descartes `×`** | **Không** | **`m + n`** | **`p × q`** |

!!! example "Ví dụ 3.12"

    Lấy `LOP` gồm 2 bộ, bậc 3 và `GIAOVIEN` gồm 2 bộ, bậc 2. Khi ấy `LOP × GIAOVIEN` có **bậc 3 + 2 = 5** và **lực lượng 2 × 2 = 4**. Với bảng lớn hơn — `HOCVIEN` 3 bộ bậc 4 nhân `LOP` 2 bộ bậc 3 — kết quả có bậc 7 và 6 bộ; quy luật vẫn thế.

**Bảng 3.21. Tích Descartes `LOP × GIAOVIEN` — mọi cặp, kể cả cặp vô nghĩa**

*Đầu vào:*

| `LOP` | MALOP | TENLOP | MAGV |
|---|---|---|---|
| | A1 | Anh cơ bản 1 | GV1 |
| | A2 | Anh giao tiếp | GV2 |

| `GIAOVIEN` | MAGV | HOTEN_GV |
|---|---|---|
| | GV1 | Lê Hoa |
| | GV2 | Trần Mai |

*Kết quả `LOP × GIAOVIEN` — 4 bộ, 5 cột; cột `MAGV` xuất hiện hai lần nên phải ghi rõ bảng gốc:*

| # | MALOP | TENLOP | LOP.MAGV | GIAOVIEN.MAGV | HOTEN_GV | Có nghĩa? |
|:--:|---|---|---|---|---|---|
| 1 | A1 | Anh cơ bản 1 | GV1 | GV1 | Lê Hoa | ✓ đúng giáo viên của lớp |
| 2 | A1 | Anh cơ bản 1 | GV1 | GV2 | Trần Mai | ✗ ghép cơ học |
| 3 | A2 | Anh giao tiếp | GV2 | GV1 | Lê Hoa | ✗ ghép cơ học |
| 4 | A2 | Anh giao tiếp | GV2 | GV2 | Trần Mai | ✓ đúng giáo viên của lớp |

Trong 4 bộ ấy chỉ **hai** bộ có ý nghĩa — những dòng mà `LOP.MAGV` và `GIAOVIEN.MAGV` **bằng nhau**. Hai bộ còn lại ghép lớp với một giáo viên không hề dạy lớp ấy. Hãy nhớ bảng này: mục 3.7.1 sẽ dùng lại nó nguyên vẹn.

Nhận xét trên dẫn thẳng tới phép toán quan trọng nhất của chương, trình bày ở mục sau: **phép kết chính là tích Descartes có lọc**.

!!! warning "Chú ý"

    Tích Descartes hiếm khi được dùng một mình vì kết quả **phình rất nhanh**. Hai bảng mỗi bảng 1.000 dòng cho ra một triệu dòng. Trong thực tế, khi một truy vấn vô tình sinh ra tích Descartes — thường do quên điều kiện kết — người ta gọi đó là *"tích Descartes ngoài ý muốn"*, và đây là một trong những lỗi gây treo hệ thống phổ biến nhất.

!!! question "Tự kiểm tra 3.5–3.6"

    *(tự trả lời trước, rồi mở đáp án bên dưới)*

    1. Trên bảng `HOCVIEN` của Ví dụ 3.8, `π_NGAYSINH(HOCVIEN)` có mấy dòng? Nếu thêm một học viên `HV04` sinh ngày `2005-04-12` thì kết quả có mấy dòng?
    2. `A(MAHV, HOTEN)` và `D(MAHV, NGAYSINH)` có khả hợp không? Vì sao?
    3. `R` có 5 bộ, bậc 2; `S` có 4 bộ, bậc 3. Cho biết bậc và lực lượng của `R × S`, của `R ∪ S` *(nếu tính được)*.

??? success "Đáp án tự kiểm tra 3.5–3.6"

    *(1)* Ba dòng *(ba ngày sinh khác nhau)*. Thêm `HV04` trùng ngày sinh với `HV01` thì kết quả **vẫn ba dòng**, vì phép chiếu gộp bộ trùng. *(2)* **Không** khả hợp: cùng bậc 2 nhưng cột thứ hai một bên là họ tên, một bên là ngày sinh — khác miền giá trị. *(3)* `R × S` có bậc 2 + 3 = 5 và 5 × 4 = 20 bộ. `R ∪ S` **không tính được** vì hai bảng khác bậc, không khả hợp.

---


---

[← Trang trước](3-5-dai-so-quan-he-phep-chon-va-phep-chieu.md) · [Trang sau →](3-7-phep-ket-va-phep-chia.md)
