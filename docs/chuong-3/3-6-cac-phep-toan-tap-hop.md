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

Điều kiện này không phải là hình thức. Nếu hợp hai bảng khác cấu trúc, kết quả sẽ là một bảng mà các dòng có **số cột khác nhau** hoặc **ý nghĩa cột lệch nhau** — không còn là một quan hệ hợp lệ, vi phạm Đặc trưng 3 và 5 ở mục 3.1.3.

## 3.6.2. Hợp, giao và hiệu

!!! note "Định nghĩa 3.10"

    Cho hai quan hệ **khả hợp** `R` và `S`:

    - **Hợp** `R ∪ S`: mọi bộ thuộc `R` **hoặc** thuộc `S` *(bộ trùng chỉ lấy một lần)*.
    - **Giao** `R ∩ S`: các bộ thuộc **cả** `R` **và** `S`.
    - **Hiệu** `R − S`: các bộ thuộc `R` **nhưng không** thuộc `S`.

    **Ví dụ 3.11.** Trung tâm ABC có hai cơ sở. Gọi `A` là tập học viên cơ sở 1, `B` là tập học viên cơ sở 2, cả hai cùng cấu trúc `(MAHV, HOTEN)`.

    | Yêu cầu nghiệp vụ | Biểu thức |
    |---|---|
    | Danh sách **toàn bộ** học viên của trung tâm | `A ∪ B` |
    | Học viên **học ở cả hai** cơ sở | `A ∩ B` |
    | Học viên **chỉ học ở cơ sở 1** | `A − B` |

Cần lưu ý rằng **phép hiệu không giao hoán**: `A − B` khác `B − A`. `A − B` cho học viên chỉ ở cơ sở 1, còn `B − A` cho học viên chỉ ở cơ sở 2. Trong khi đó `∪` và `∩` đều giao hoán.

## 3.6.3. Tích Descartes — phép duy nhất không đòi hỏi khả hợp

!!! note "Định nghĩa 3.11"

    **Tích Descartes** *(Cartesian product)* `R × S` ghép **mỗi bộ của `R` với mọi bộ của `S`**. Nếu `R` có bậc `m` và lực lượng `p`, còn `S` có bậc `n` và lực lượng `q`, thì `R × S` có **bậc `m + n`** và **lực lượng `p × q`**.

Tích Descartes được xếp vào **nhóm phép toán tập hợp** vì nó kế thừa trực tiếp từ lý thuyết tập hợp, giống ba phép trên. Nhưng nó **khác ba phép kia ở một điểm căn bản**, và đây là chỗ người học hay nhầm.

**Ba phép `∪`, `∩`, `−` đòi hỏi khả hợp; tích Descartes thì không.** Lý do nằm ở bản chất phép toán. Ba phép đầu **so sánh các bộ với nhau** để quyết định giữ hay bỏ, nên hai bộ phải có cùng cấu trúc mới so sánh được. Tích Descartes **không so sánh gì cả** — nó chỉ nối hai bộ lại thành một bộ dài hơn, nên hai quan hệ đầu vào có cấu trúc thế nào cũng được.

**Bảng 3.7. Bốn phép toán tập hợp — đối chiếu**

| Phép toán | Đòi hỏi khả hợp? | Bậc kết quả | Lực lượng kết quả |
|---|:--:|---|---|
| Hợp `∪` | **Có** | Bằng bậc đầu vào | ≤ `p + q` *(bỏ trùng)* |
| Giao `∩` | **Có** | Bằng bậc đầu vào | ≤ min(`p`, `q`) |
| Hiệu `−` | **Có** | Bằng bậc đầu vào | ≤ `p` |
| **Tích Descartes `×`** | **Không** | **`m + n`** | **`p × q`** |

!!! example "Ví dụ 3.12"

    `HOCVIEN` có 3 bộ và bậc 4; `LOP` có 2 bộ và bậc 3. Khi ấy `HOCVIEN × LOP` có **bậc 7** và **lực lượng 6**. Trong 6 bộ ấy, chỉ một số ít là có ý nghĩa — những cặp mà học viên thật sự thuộc lớp đó. Phần còn lại là ghép cơ học vô nghĩa.

Nhận xét trên dẫn thẳng tới phép toán quan trọng nhất của chương, trình bày ở mục sau: **phép kết chính là tích Descartes có lọc**.

!!! warning "Chú ý"

    Tích Descartes hiếm khi được dùng một mình vì kết quả **phình rất nhanh**. Hai bảng mỗi bảng 1.000 dòng cho ra một triệu dòng. Trong thực tế, khi một truy vấn vô tình sinh ra tích Descartes — thường do quên điều kiện kết — người ta gọi đó là *"tích Descartes ngoài ý muốn"*, và đây là một trong những lỗi gây treo hệ thống phổ biến nhất.

---


---

[← Trang trước](3-5-dai-so-quan-he-phep-chon-va-phep-chieu.md) · [Trang sau →](3-7-phep-ket-va-phep-chia.md)
