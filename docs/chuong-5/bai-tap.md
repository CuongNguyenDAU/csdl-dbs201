# Bài tập Chương 5

## Mức A — Nhận biết và tái hiện

**Bài A1.** Cho `R(A,B,C,D,E)` và `F = {A → B, BC → D, D → E}`. Tính `(AC)⁺` và `(BD)⁺`, ghi rõ từng vòng lặp.


??? success "Lời giải bài A1"

    `R(A,B,C,D,E)` với `F = {A → B, BC → D, D → E}`.

    ### Tính `(AC)⁺`

    | Vòng | Tập hiện có | Phụ thuộc áp được | Kết quả |
    |:--:|---|---|---|
    | 0 | `{A, C}` | — | khởi tạo |
    | 1 | `{A, C}` | `A → B` vì `A ⊆ X` | `{A, B, C}` |
    | 2 | `{A, B, C}` | `BC → D` vì `{B,C} ⊆ X` | `{A, B, C, D}` |
    | 3 | `{A, B, C, D}` | `D → E` vì `D ⊆ X` | `{A, B, C, D, E}` |
    | 4 | `{A, B, C, D, E}` | không còn gì áp thêm | **dừng** |

    **`(AC)⁺ = {A, B, C, D, E}`** — bằng toàn bộ thuộc tính của `R`, nên `AC` là **siêu khóa**.

    ### Tính `(BD)⁺`

    | Vòng | Tập hiện có | Phụ thuộc áp được | Kết quả |
    |:--:|---|---|---|
    | 0 | `{B, D}` | — | khởi tạo |
    | 1 | `{B, D}` | `D → E` vì `D ⊆ X` | `{B, D, E}` |
    | 2 | `{B, D, E}` | `A → B` không áp được (`A ⊄ X`)<br>`BC → D` không áp được (`C ⊄ X`) | **dừng** |

    **`(BD)⁺ = {B, D, E}`** — thiếu `A` và `C`, nên `BD` **không** phải siêu khóa.

    Hai kết quả trên minh họa đúng hai công dụng của bao đóng: kiểm tra một tập có phải siêu khóa hay không, và kiểm tra một phụ thuộc có suy ra được hay không — chẳng hạn `BD → E` suy ra được vì `E ∈ (BD)⁺`, còn `BD → A` thì không.

**Bài A2.** Với mỗi phát biểu, cho biết đúng hay sai và giải thích: (a) mọi quan hệ đạt 3NF đều đạt 2NF; (b) mọi quan hệ đạt BCNF đều đạt 3NF; (c) nếu khóa chỉ gồm một thuộc tính thì quan hệ luôn đạt 2NF; (d) nếu mọi thuộc tính đều là thuộc tính khóa thì quan hệ luôn đạt 3NF; (e) mọi quan hệ đạt BCNF đều đạt 4NF.


??? success "Lời giải bài A2"

    | Phát biểu | Đúng/Sai | Giải thích |
    |---|:--:|---|
    | (a) Mọi quan hệ đạt 3NF đều đạt 2NF | **Đúng** | Định nghĩa 3NF **bao hàm** 2NF: *"đạt 2NF và không có phụ thuộc bắc cầu"*. Các dạng chuẩn lồng nhau như những vòng tròn đồng tâm |
    | (b) Mọi quan hệ đạt BCNF đều đạt 3NF | **Đúng** | BCNF chặt hơn: nó bỏ đi ngoại lệ mà 3NF cho phép *(vế phải là thuộc tính khóa)*. Chiều ngược lại **sai** — xem bài C1 |
    | (c) Khóa chỉ gồm một thuộc tính thì luôn đạt 2NF | **Đúng** | Phụ thuộc bộ phận đòi hỏi *một phần thực sự của khóa* xác định được thuộc tính không khóa. Khóa một thuộc tính thì không có phần thực sự nào khác rỗng ⇒ không thể có phụ thuộc bộ phận. **Lưu ý:** vẫn phải đạt 1NF trước |
    | (d) Mọi thuộc tính đều là thuộc tính khóa thì luôn đạt 3NF | **Đúng** | 3NF cấm *thuộc tính **không khóa*** phụ thuộc bắc cầu vào khóa. Không có thuộc tính không khóa nào thì điều kiện thỏa mãn hiển nhiên. Nhưng quan hệ ấy vẫn **có thể không đạt BCNF** — đúng trường hợp bài C1 |
    | (e) Mọi quan hệ đạt BCNF đều đạt 4NF | **Sai** | 4NF đòi thêm điều kiện về **phụ thuộc đa trị**. Bảng `NV_KYNANG_NGOAINGU` ở bài C2 đạt BCNF *(mọi thuộc tính đều là thuộc tính khóa)* nhưng **không** đạt 4NF |

    Phát biểu (d) và (e) đi cặp với nhau và đáng ghi nhớ: chúng cho thấy vì sao chuỗi dạng chuẩn không dừng ở 3NF.

**Bài A3.** Cho `F = {AB → C, A → D, D → B}`. Xác định `TN`, `TG`, `TĐ` cho `R(A,B,C,D)`.


??? success "Lời giải bài A3"

    `R(A,B,C,D)` với `F = {AB → C, A → D, D → B}`.

    Lập bảng đối chiếu vị trí xuất hiện của từng thuộc tính:

    | Thuộc tính | Xuất hiện vế trái | Xuất hiện vế phải | Nhóm |
    |:--:|:--:|:--:|:--:|
    | `A` | `AB → C`, `A → D` | — | **TN** |
    | `B` | `AB → C` | `D → B` | **TG** |
    | `C` | — | `AB → C` | **TĐ** |
    | `D` | `D → B` | `A → D` | **TG** |

    **`TN = {A}` · `TG = {B, D}` · `TĐ = {C}`**

    Ý nghĩa thực hành: `A` **luôn** thuộc mọi khóa, `C` **không bao giờ** thuộc khóa nào. Thay vì duyệt cả 16 tập con của `{A,B,C,D}`, chỉ cần thử `A` ghép với 4 tập con của `TG` — giảm từ 16 xuống 4 lần kiểm tra.

    Kiểm nhanh: `A⁺ = {A, D, B, C}` — đủ mọi thuộc tính ⇒ **`A` là khóa duy nhất**, và không cần thử thêm tập nào nữa vì mọi tập chứa `A` đều là siêu khóa nhưng không tối thiểu.

## Mức B — Vận dụng

**Bài B1.** Cho `R(A,B,C,D,E)` và `F = {AB → C, C → D, D → A, B → E}`.
a) Xác định `TN`, `TG`, `TĐ`.
b) Tìm **tất cả** khóa, trình bày bảng duyệt đầy đủ và chỉ rõ chỗ áp **mẹo rút gọn**.
c) Xác định thuộc tính khóa và thuộc tính không khóa.
d) Xác định **dạng chuẩn cao nhất** mà `R` đạt được, có chứng minh.


??? success "Lời giải bài B1"

    `R(A,B,C,D,E)` với `F = {AB → C, C → D, D → A, B → E}`.

    ### (a) Xác định `TN`, `TG`, `TĐ`

    | Thuộc tính | Vế trái | Vế phải | Nhóm |
    |:--:|:--:|:--:|:--:|
    | `A` | `AB → C` | `D → A` | **TG** |
    | `B` | `AB → C`, `B → E` | — | **TN** |
    | `C` | `C → D` | `AB → C` | **TG** |
    | `D` | `D → A` | `C → D` | **TG** |
    | `E` | — | `B → E` | **TĐ** |

    **`TN = {B}` · `TG = {A, C, D}` · `TĐ = {E}`**

    ### (b) Tìm tất cả khóa

    `B` luôn thuộc mọi khóa. Duyệt các tập con của `TG = {A, C, D}`, ghép với `B`.

    | # | Tập thử `X` | `X⁺` | Siêu khóa? | Tối thiểu? |
    |:--:|---|---|:--:|:--:|
    | 1 | `B` | `{B, E}` | không | — |
    | 2 | `AB` | `{A,B,C,D,E}` | **có** | **khóa** |
    | 3 | `BC` | `{B,C,D,A,E}` | **có** | **khóa** |
    | 4 | `BD` | `{B,D,A,C,E}` | **có** | **khóa** |
    | 5 | `ABC` | đủ | có | *bỏ* — chứa khóa `AB` |
    | 6 | `ABD` | đủ | có | *bỏ* — chứa khóa `AB` |
    | 7 | `BCD` | đủ | có | *bỏ* — chứa khóa `BC` |
    | 8 | `ABCD` | đủ | có | *bỏ* — chứa khóa `AB` |

    **Chỗ áp mẹo rút gọn:** từ dòng 5 trở đi **không cần tính bao đóng nữa**. Đã biết `AB`, `BC`, `BD` là khóa, mà mọi tập ở dòng 5–8 đều **chứa trọn** một trong ba tập ấy, nên chắc chắn là siêu khóa nhưng **không tối thiểu**. Mẹo này cắt được một nửa khối lượng tính toán.

    Chi tiết bao đóng dòng 2: `AB → C` cho `C`; `C → D` cho `D`; `B → E` cho `E` ⇒ đủ năm thuộc tính.

    **Ba khóa: `AB`, `BC`, `BD`.**

    ### (c) Thuộc tính khóa và không khóa

    Hợp ba khóa: `{A, B} ∪ {B, C} ∪ {B, D} = {A, B, C, D}`.

    - **Thuộc tính khóa:** `A`, `B`, `C`, `D`
    - **Thuộc tính không khóa:** `E`

    ### (d) Dạng chuẩn cao nhất

    **Kiểm 2NF.** Chỉ cần xét thuộc tính không khóa `E`. Có `B → E`, mà `B` là **tập con thực sự** của cả ba khóa `AB`, `BC`, `BD` ⇒ `E` phụ thuộc **bộ phận** vào khóa ⇒ **`R` không đạt 2NF**.

    **Dạng chuẩn cao nhất: 1NF.**

    *(Giả định `R` đạt 1NF, tức mọi ô đều chứa giá trị đơn — điều luôn đúng với lược đồ quan hệ.)*

    **Cách chữa.** Tách `E` ra theo phụ thuộc bộ phận gây lỗi:

    ```text
    R1(B, E)              -- khóa B
    R2(A, B, C, D)        -- khóa AB, BC, BD
    ```

    `R1` đạt BCNF. `R2` cần kiểm tiếp: `C → D` với `C` là siêu khóa của `R2`? `C⁺` trong `R2` = `{C, D, A}`, thiếu `B` ⇒ `C` **không** là siêu khóa ⇒ `R2` **không đạt BCNF**. Nhưng `D` là thuộc tính khóa nên `R2` **đạt 3NF**. Đây lại là tình huống của bài C1.

**Bài B2.** Cho `F = {A → BC, CD → E, B → D, E → A}`. Tìm **phủ tối thiểu**, trình bày đủ ba bước.


??? success "Lời giải bài B2"

    `F = {A → BC, CD → E, B → D}`.

    ### Bước 1 — Tách vế phải

    ```text
    F1 = { A → B,  A → C,  CD → E,  B → D }
    ```

    Chỉ `A → BC` cần tách. Bốn phụ thuộc, mỗi cái một thuộc tính bên phải.

    ### Bước 2 — Loại thuộc tính thừa ở vế trái

    Chỉ `CD → E` có vế trái nhiều hơn một thuộc tính. Thử bỏ từng cái:

    - **Bỏ `C`, còn `D → E`?** Tính `D⁺` theo `F1` = `{D}`. Không chứa `E` ⇒ **không suy ra được** ⇒ `C` **không thừa**.
    - **Bỏ `D`, còn `C → E`?** Tính `C⁺` theo `F1` = `{C}`. Không chứa `E` ⇒ `D` **không thừa**.

    Vế trái giữ nguyên: `F2 = F1`.

    ### Bước 3 — Loại phụ thuộc thừa

    Bỏ từng phụ thuộc rồi kiểm xem có suy lại được không.

    | Bỏ | Tập còn lại | Kiểm tra | Kết luận |
    |---|---|---|---|
    | `A → B` | `{A → C, CD → E, B → D}` | `A⁺ = {A, C}`, không chứa `B` | **giữ** |
    | `A → C` | `{A → B, CD → E, B → D}` | `A⁺ = {A, B, D}`, không chứa `C` | **giữ** |
    | `CD → E` | `{A → B, A → C, B → D}` | `(CD)⁺ = {C, D}`, không chứa `E` | **giữ** |
    | `B → D` | `{A → B, A → C, CD → E}` | `B⁺ = {B}`, không chứa `D` | **giữ** |

    Không phụ thuộc nào thừa.

    ### Kết quả

    ```text
    F_min = { A → B,  A → C,  CD → E,  B → D }
    ```

    Nhận xét: `F` ban đầu trông đã gọn nhưng vẫn phải chạy đủ ba bước mới khẳng định được. Bước 1 là bước duy nhất thực sự thay đổi tập, và nó phải làm **trước** — nếu loại phụ thuộc thừa trước khi tách vế phải thì có thể bỏ sót cơ hội rút gọn.

**Bài B3.** Cho bảng phẳng của một **hiệu sách**:

`DONHANG(MADH, NGAYDAT, MAKH, TENKH, SDT_KH, MASP, TENSP, DONGIA, SOLUONG)`

với các quy tắc nghiệp vụ: mỗi đơn hàng có một ngày đặt và một khách hàng; mỗi khách hàng có một tên và một số điện thoại; mỗi sản phẩm có một tên và một đơn giá; mỗi dòng đơn hàng ghi số lượng của một sản phẩm trong một đơn.

a) Viết tập phụ thuộc hàm `F`.
b) Tìm tất cả khóa.
c) Chẩn đoán dạng chuẩn, chỉ đích danh các phụ thuộc **bộ phận** và **bắc cầu**.
d) Chuẩn hóa về **3NF**, trình bày từng bước.
e) **Chứng minh** mọi phép tách đều bảo toàn thông tin.


??? success "Lời giải bài B3"

    `DONHANG(MADH, NGAYDAT, MAKH, TENKH, SDT_KH, MASP, TENSP, DONGIA, SOLUONG)`

    ### (a) Tập phụ thuộc hàm

    Đọc từng quy tắc nghiệp vụ:

    ```text
    f1: MADH → NGAYDAT, MAKH        (mỗi đơn có một ngày đặt và một khách)
    f2: MAKH → TENKH, SDT_KH        (mỗi khách có một tên và một số điện thoại)
    f3: MASP → TENSP, DONGIA        (mỗi sản phẩm có một tên và một đơn giá)
    f4: MADH, MASP → SOLUONG        (mỗi dòng đơn ghi số lượng)
    ```

    ### (b) Tìm tất cả khóa

    | Thuộc tính | Vế trái | Vế phải | Nhóm |
    |:--:|:--:|:--:|:--:|
    | `MADH` | f1, f4 | — | **TN** |
    | `MASP` | f3, f4 | — | **TN** |
    | `MAKH` | f2 | f1 | TG |
    | các thuộc tính còn lại | — | có | **TĐ** |

    `TN = {MADH, MASP}`. Kiểm ngay: `(MADH, MASP)⁺` = `{MADH, MASP}` → thêm `NGAYDAT, MAKH` (f1) → thêm `TENKH, SDT_KH` (f2) → thêm `TENSP, DONGIA` (f3) → thêm `SOLUONG` (f4) = **toàn bộ**.

    `TN` đã là siêu khóa ⇒ **khóa duy nhất là `(MADH, MASP)`**, không cần duyệt `TG`.

    **Thuộc tính khóa:** `MADH`, `MASP`. **Không khóa:** bảy thuộc tính còn lại.

    ### (c) Chẩn đoán dạng chuẩn

    **Phụ thuộc bộ phận** — thuộc tính không khóa chỉ cần **một phần** khóa:

    - `MADH → NGAYDAT` — chỉ cần nửa khóa `MADH`
    - `MADH → MAKH` — chỉ cần `MADH`
    - `MASP → TENSP` — chỉ cần nửa kia `MASP`
    - `MASP → DONGIA` — chỉ cần `MASP`

    ⇒ **Không đạt 2NF.**

    **Phụ thuộc bắc cầu** — qua trung gian không phải khóa:

    - `MADH → MAKH → TENKH`
    - `MADH → MAKH → SDT_KH`

    `MAKH` không phải khóa và không phải tập con của khóa ⇒ đúng định nghĩa bắc cầu.

    **Dạng chuẩn cao nhất: 1NF.**

    Hậu quả thực tế của hai loại lỗi: tên và số điện thoại khách lặp ở **mọi dòng của mọi đơn** người đó đặt; tên và đơn giá sản phẩm lặp ở **mọi dòng có sản phẩm** ấy. Đổi số điện thoại khách phải sửa hàng chục dòng, sót một dòng là mâu thuẫn — đúng chuỗi *dư thừa → không nhất quán* của Chương 1.

    ### (d) Chuẩn hóa về 3NF

    **Bước 1 — Từ 1NF lên 2NF: tách phụ thuộc bộ phận.**

    ```text
    DONHANG(MADH, NGAYDAT, MAKH, TENKH, SDT_KH)     -- theo MADH
    SANPHAM(MASP, TENSP, DONGIA)                     -- theo MASP
    CHITIET(MADH, MASP, SOLUONG)                     -- phần phụ thuộc đầy đủ
    ```

    Ba bảng đều đạt 2NF: `SANPHAM` và `CHITIET` có mọi thuộc tính không khóa phụ thuộc đầy đủ vào khóa; `DONHANG` có khóa một thuộc tính nên không thể có bộ phận.

    **Bước 2 — Từ 2NF lên 3NF: tách phụ thuộc bắc cầu.**

    `DONHANG` còn `MADH → MAKH → TENKH, SDT_KH`. Tách phần phụ thuộc vào `MAKH`:

    ```text
    DONHANG(MADH, NGAYDAT, MAKH)
    KHACHHANG(MAKH, TENKH, SDT_KH)
    SANPHAM(MASP, TENSP, DONGIA)
    CHITIET(MADH, MASP, SOLUONG)
    ```

    **Kiểm tra lần cuối:**

    | Bảng | Khóa | 2NF | 3NF |
    |---|---|:--:|:--:|
    | `DONHANG` | `MADH` | ✔ khóa đơn | ✔ `NGAYDAT`, `MAKH` phụ thuộc trực tiếp |
    | `KHACHHANG` | `MAKH` | ✔ | ✔ |
    | `SANPHAM` | `MASP` | ✔ | ✔ |
    | `CHITIET` | `(MADH, MASP)` | ✔ `SOLUONG` phụ thuộc đầy đủ | ✔ không có trung gian |

    Cả bốn bảng **đạt 3NF**. Thực ra cả bốn đều đạt BCNF, vì mọi vế trái đều là khóa.

    ### (e) Chứng minh mọi phép tách bảo toàn thông tin

    Điều kiện: phần giao phải là **siêu khóa của ít nhất một** bảng con.

    **Phép tách 1** — `DONHANG_1NF` thành `{MADH, NGAYDAT, MAKH, TENKH, SDT_KH}` và `{MADH, MASP, SOLUONG}`:

    - Phần giao = `{MADH}`
    - `MADH⁺` = `{MADH, NGAYDAT, MAKH, TENKH, SDT_KH}` — **chứa trọn** bảng thứ nhất
    - ⇒ `MADH` là siêu khóa của bảng thứ nhất ⇒ **bảo toàn thông tin** ✔

    **Phép tách 2** — tách tiếp `SANPHAM` khỏi `CHITIET`:

    - Phần giao = `{MASP}`
    - `MASP⁺` = `{MASP, TENSP, DONGIA}` — **chứa trọn** `SANPHAM`
    - ⇒ **bảo toàn thông tin** ✔

    **Phép tách 3** — `DONHANG` thành `{MADH, NGAYDAT, MAKH}` và `KHACHHANG{MAKH, TENKH, SDT_KH}`:

    - Phần giao = `{MAKH}`
    - `MAKH⁺` = `{MAKH, TENKH, SDT_KH}` — **chứa trọn** `KHACHHANG`
    - ⇒ **bảo toàn thông tin** ✔

    Cả ba phép tách đều bảo toàn thông tin, nên ghép bốn bảng cuối lại luôn cho đúng dữ liệu ban đầu, **không sinh bộ giả**.

    Điểm chung đáng rút ra: mọi phép tách trên đều tách **theo đúng một phụ thuộc hàm**, lấy vế trái làm phần giao. Cách tách ấy **tự động** bảo toàn thông tin, vì vế trái của một phụ thuộc luôn là siêu khóa của bảng chứa vế phải của nó.

**Bài B4.** Dùng lược đồ **thư viện** đã làm ở các chương trước:
a) Viết tập phụ thuộc hàm `F` từ các quy tắc nghiệp vụ.
b) Kiểm tra từng bảng xem đã đạt 3NF chưa.
c) Nếu có bảng chưa đạt, chuẩn hóa và giải thích.


??? success "Lời giải bài B4"

    Lược đồ thư viện từ Chương 3:

    ```text
    THELOAI(MATL, TENTL)
    DAUSACH(MADS, TENSACH, NAMXB, MATL)
    TACGIA(MATG, HOTEN_TG)
    VIET(MADS, MATG)
    BANSAO(MABS, TINHTRANG, MADS)
    DOCGIA(MADG, HOTEN, NGAYSINH, NGAYCAPTHE)
    MUON(MADG, MABS, NGAYMUON, NGAYHENTRA, NGAYTRA)
    ```

    ### (a) Tập phụ thuộc hàm

    ```text
    MATL → TENTL
    MADS → TENSACH, NAMXB, MATL
    MATG → HOTEN_TG
    MABS → TINHTRANG, MADS
    MADG → HOTEN, NGAYSINH, NGAYCAPTHE
    MADG, MABS → NGAYMUON, NGAYHENTRA, NGAYTRA
    ```

    Bảng `VIET` không có phụ thuộc hàm nào ngoài phụ thuộc tầm thường — nó chỉ ghi nhận sự kết hợp.

    ### (b) Kiểm tra từng bảng

    | Bảng | Khóa | Phụ thuộc bộ phận? | Phụ thuộc bắc cầu? | Kết luận |
    |---|---|:--:|:--:|:--:|
    | `THELOAI` | `MATL` | không — khóa đơn | không | **3NF** ✔ |
    | `DAUSACH` | `MADS` | không — khóa đơn | không — `MATL` phụ thuộc trực tiếp | **3NF** ✔ |
    | `TACGIA` | `MATG` | không | không | **3NF** ✔ |
    | `VIET` | `(MADS, MATG)` | không — không có thuộc tính không khóa | không | **3NF** ✔ |
    | `BANSAO` | `MABS` | không | không | **3NF** ✔ |
    | `DOCGIA` | `MADG` | không | không | **3NF** ✔ |
    | `MUON` | `(MADG, MABS)` | không — ba thuộc tính đều cần **cả cặp** | không | **3NF** ✔ |

    **Cả bảy bảng đều đạt 3NF.** Thực tế còn đạt BCNF, vì mọi vế trái của mọi phụ thuộc không tầm thường đều là khóa.

    ### (c) Vì sao không bảng nào phải chuẩn hóa lại

    Đây không phải may mắn. Lược đồ này ra đời từ quy trình **ER → ánh xạ** của Chương 2 và 3, và quy trình ấy đã loại sẵn hai nguyên nhân gây lỗi:

    - **Phụ thuộc bộ phận** sinh ra khi gộp nhiều loại sự vật vào một bảng có khóa phức hợp. Bước 1 của quy trình năm bước — *mỗi loại sự vật một thực thể* — đã ngăn điều đó từ mức quan niệm.
    - **Phụ thuộc bắc cầu** sinh ra khi để thuộc tính của sự vật A nằm trong bảng của sự vật B. Việc tách thực thể ở Chương 2 cũng đã ngăn.

    Đây là kết luận đáng nhớ nhất của bài: **thiết kế ER đúng thì lược đồ ánh xạ ra thường đã đạt 3NF**. Chuẩn hóa khi ấy đóng vai trò **kiểm chứng** chứ không phải sửa chữa. Chuẩn hóa chỉ thật sự phải làm việc nặng khi ta xuất phát từ một **bảng phẳng có sẵn** — như bài B3 — chứ không phải từ một lược đồ ER.

    Nếu muốn thấy chuẩn hóa phát huy tác dụng trên bài thư viện, hãy thử thêm cột `TENTL` vào `DAUSACH` cho tiện tra cứu: lập tức sinh phụ thuộc bắc cầu `MADS → MATL → TENTL` và bảng rơi xuống 2NF.

## Mức C — Nâng cao

**Bài C1.** Cho `R(A,B,C)` và `F = {AB → C, C → B}`.
a) Tìm tất cả khóa.
b) Chứng minh `R` đạt **3NF** nhưng **không đạt BCNF**.
c) Tách về BCNF và chỉ ra **phụ thuộc hàm nào bị mất**.
d) Liên hệ với Định lý 5.2 và giải thích vì sao trường hợp này nên **dừng ở 3NF**.


??? success "Lời giải bài C1"

    `R(A,B,C)` với `F = {AB → C, C → B}`.

    ### (a) Tìm tất cả khóa

    | Thuộc tính | Vế trái | Vế phải | Nhóm |
    |:--:|:--:|:--:|:--:|
    | `A` | `AB → C` | — | **TN** |
    | `B` | `AB → C` | `C → B` | **TG** |
    | `C` | `C → B` | `AB → C` | **TG** |

    `A` thuộc mọi khóa. Duyệt tập con của `TG = {B, C}`:

    | Tập thử | Bao đóng | Siêu khóa? | Tối thiểu? |
    |---|---|:--:|:--:|
    | `A` | `{A}` | không | — |
    | `AB` | `{A,B,C}` | **có** | **khóa** |
    | `AC` | `{A,C,B}` | **có** | **khóa** |
    | `ABC` | đủ | có | *bỏ* — chứa `AB` |

    **Hai khóa: `AB` và `AC`.**

    **Thuộc tính khóa:** `A`, `B`, `C` — **toàn bộ**. Không có thuộc tính không khóa nào.

    ### (b) Chứng minh `R` đạt 3NF nhưng không đạt BCNF

    **Đạt 3NF.** Định nghĩa 3NF cấm *thuộc tính **không khóa*** phụ thuộc bắc cầu vào khóa. Ở đây **không tồn tại thuộc tính không khóa nào**, nên điều kiện thỏa mãn hiển nhiên — không có gì để vi phạm. ⇒ `R` đạt 3NF. ∎

    *(Cách phát biểu tương đương: với mọi `X → A` không tầm thường, hoặc `X` là siêu khóa, hoặc `A` là thuộc tính khóa. Xét `C → B`: `C` không là siêu khóa, nhưng `B` **là** thuộc tính khóa ⇒ vẫn thỏa 3NF.)*

    **Không đạt BCNF.** Định nghĩa 5.17 đòi: với **mọi** phụ thuộc không tầm thường `X → A`, `X` phải là **siêu khóa**.

    Xét `C → B`:

    - Đây là phụ thuộc không tầm thường vì `B ⊄ C`.
    - `C⁺ = {C, B}` — **không chứa `A`** ⇒ `C` **không** là siêu khóa.

    ⇒ `R` **vi phạm BCNF**. ∎

    ### (c) Tách về BCNF và phụ thuộc bị mất

    Tách theo phụ thuộc vi phạm `C → B`:

    ```text
    R1(C, B)     -- khóa C
    R2(A, C)     -- khóa AC
    ```

    **Kiểm bảo toàn thông tin:** phần giao = `{C}`; `C⁺ = {C, B}` chứa trọn `R1` ⇒ `C` là siêu khóa của `R1` ⇒ **bảo toàn thông tin** ✔

    **Kiểm bảo toàn phụ thuộc:**

    | Phụ thuộc | Kiểm được trên bảng con nào? |
    |---|---|
    | `C → B` | ✔ `R1` chứa cả `C` và `B` |
    | `AB → C` | ✘ **không bảng nào** chứa đủ `A`, `B`, `C` |

    **Phụ thuộc bị mất: `AB → C`.**

    Hậu quả cụ thể: muốn kiểm tra ràng buộc *"cặp `(A, B)` xác định duy nhất một `C`"*, hệ quản trị phải **ghép `R1` và `R2` lại** rồi mới kiểm. Không thể đặt một ràng buộc cục bộ trên `R1` hay `R2` để bảo đảm điều đó. Mỗi lần thêm dữ liệu vào một trong hai bảng đều phải chạy một phép kết — chi phí y hệt ràng buộc *liên bộ liên quan hệ* của Chương 4.

    ### (d) Liên hệ Định lý 5.2 và vì sao nên dừng ở 3NF

    **Định lý 5.2** phát biểu: luôn tồn tại phép tách về **3NF** vừa **bảo toàn thông tin** vừa **bảo toàn phụ thuộc hàm**; nhưng với **BCNF** thì chỉ bảo đảm được **bảo toàn thông tin**, còn bảo toàn phụ thuộc **có thể không đạt được**.

    Trường hợp này là ví dụ mẫu: muốn lên BCNF thì buộc phải hy sinh `AB → C`.

    **Ba lý do nên dừng ở 3NF ở đây:**

    1. **Cái được rất nhỏ.** Vi phạm BCNF duy nhất là `C → B`, gây dư thừa ở chỗ giá trị `B` lặp lại theo `C`. Nhưng `B` là thuộc tính khóa, số bộ phân biệt bị giới hạn, nên mức dư thừa thực tế thường không đáng kể.

    2. **Cái mất rất đắt.** Mất `AB → C` nghĩa là mất khả năng **thực thi ràng buộc tại chỗ**. Từ một ràng buộc mà hệ quản trị tự lo, nó trở thành ràng buộc phải viết trigger và chạy phép kết mỗi lần ghi. Đây đúng là **cờ đỏ thiết kế** của Chương 4, chỉ khác là lần này ta tự tạo ra nó.

    3. **3NF đã đủ cho mục tiêu chính.** Mục tiêu của chuẩn hóa là loại **dị thường** do dư thừa gây ra. 3NF đã loại hết dị thường liên quan tới thuộc tính không khóa — phần chiếm đa số dữ liệu. Phần BCNF xử lý thêm là các ca hiếm, liên quan tới thuộc tính khóa.

    **Nguyên tắc thực hành:** chuẩn hóa tới **3NF là bắt buộc**; lên BCNF chỉ khi **vừa đạt được** cả bảo toàn phụ thuộc. Không đạt được thì dừng ở 3NF và ghi rõ lý do vào tài liệu thiết kế, để người sau không tưởng là mình quên chuẩn hóa.

**Bài C2.** Cho quan hệ `NHANVIEN_KYNANG_NGOAINGU(MANV, KYNANG, NGOAINGU)` trong đó kỹ năng và ngoại ngữ của một nhân viên **độc lập với nhau**.
a) Với một nhân viên có 4 kỹ năng và 3 ngoại ngữ, bảng phải chứa bao nhiêu dòng?
b) Bảng này có đạt BCNF không? Giải thích.
c) Chỉ ra các phụ thuộc đa trị và **tách về 4NF**.
d) Sau khi tách, cần bao nhiêu dòng? Tính tỷ lệ tiết kiệm.


??? success "Lời giải bài C2"

    `NHANVIEN_KYNANG_NGOAINGU(MANV, KYNANG, NGOAINGU)`, kỹ năng và ngoại ngữ **độc lập** nhau.

    ### (a) Số dòng cần thiết

    Vì hai thuộc tính độc lập, bảng phải chứa **mọi tổ hợp** để không ngầm khẳng định một mối liên hệ không có thật.

    Nhân viên có 4 kỹ năng và 3 ngoại ngữ ⇒ **4 × 3 = 12 dòng**.

    Minh họa với `NV01` biết Java, Python, SQL, C# và tiếng Anh, Nhật, Pháp:

    | MANV | KYNANG | NGOAINGU |
    |---|---|---|
    | NV01 | Java | Anh |
    | NV01 | Java | Nhật |
    | NV01 | Java | Pháp |
    | NV01 | Python | Anh |
    | … | … | … |
    | NV01 | C# | Pháp |

    Nếu chỉ ghi 4 dòng cho kỹ năng và bỏ trống ngoại ngữ ở phần còn lại, dữ liệu sẽ ngầm nói *"NV01 biết Java **kèm** tiếng Anh"* — một mối liên hệ không hề tồn tại.

    ### (b) Có đạt BCNF không

    **Có, bảng này đạt BCNF.**

    Khóa của bảng là **toàn bộ ba thuộc tính** `(MANV, KYNANG, NGOAINGU)`, vì không tổ hợp nhỏ hơn nào xác định được phần còn lại.

    Không có phụ thuộc hàm **không tầm thường** nào: `MANV` không xác định được `KYNANG` *(một người nhiều kỹ năng)*, cũng không xác định được `NGOAINGU`. Không có phụ thuộc nào để vi phạm ⇒ mọi điều kiện của BCNF thỏa mãn hiển nhiên.

    Đây chính là điểm mấu chốt: **bảng đạt BCNF mà vẫn dư thừa nặng.** Đó là lý do phải có thêm 4NF — công cụ của các dạng chuẩn dựa trên phụ thuộc hàm đã hết tác dụng ở đây.

    ### (c) Phụ thuộc đa trị và tách về 4NF

    Hai phụ thuộc đa trị **không tầm thường**:

    ```text
    MANV ↠ KYNANG
    MANV ↠ NGOAINGU
    ```

    Đọc là: *tập kỹ năng của một nhân viên được xác định bởi `MANV` và **độc lập** với ngoại ngữ*, và ngược lại.

    `R` vi phạm 4NF vì `MANV` **không** phải siêu khóa của `R`.

    **Tách:**

    ```text
    NV_KYNANG(MANV, KYNANG)
    NV_NGOAINGU(MANV, NGOAINGU)
    ```

    **Kiểm bảo toàn thông tin:** phần giao = `{MANV}`. Theo định lý về phụ thuộc đa trị, phép tách theo `X ↠ Y` với `X` là phần giao luôn bảo toàn thông tin ⇒ ghép hai bảng lại bằng kết tự nhiên cho đúng 12 dòng ban đầu, không bộ giả.

    Cả hai bảng con đều đạt **4NF**: mỗi bảng chỉ còn một phụ thuộc đa trị, và nó đã tầm thường.

    ### (d) Số dòng sau khi tách và tỷ lệ tiết kiệm

    | | Trước | Sau |
    |---|:--:|:--:|
    | `NV_KYNANG` | — | 4 dòng |
    | `NV_NGOAINGU` | — | 3 dòng |
    | **Tổng** | **12** | **7** |

    **Tiết kiệm = (12 − 7) / 12 ≈ 42%.**

    Tỷ lệ này tăng rất nhanh theo quy mô. Với `m` kỹ năng và `n` ngoại ngữ:

    | `m` × `n` | Trước | Sau | Tiết kiệm |
    |---|:--:|:--:|:--:|
    | 4 × 3 | 12 | 7 | 42% |
    | 10 × 5 | 50 | 15 | 70% |
    | 20 × 10 | 200 | 30 | **85%** |

    Ngoài dung lượng, cái được lớn hơn là **hết dị thường**: trước khi tách, thêm một ngoại ngữ cho `NV01` phải thêm **4 dòng** — đúng bằng số kỹ năng; sót một dòng là dữ liệu ngầm khẳng định người này biết ngoại ngữ mới nhưng *chỉ khi* dùng ba kỹ năng nhất định. Sau khi tách, thêm ngoại ngữ chỉ là thêm **một dòng**.

**Bài C3.** Một hệ thống thương mại điện tử lưu bảng `DONHANG` đã chuẩn hóa 3NF. Bộ phận báo cáo phàn nàn rằng truy vấn *"doanh thu theo tháng theo danh mục sản phẩm"* phải ghép 5 bảng và chạy mất 40 giây.
a) Đề xuất một phương án **phi chuẩn hóa** cụ thể.
b) Chỉ ra **dư thừa** mà phương án ấy tạo ra và **dị thường** có thể phát sinh.
c) Đề xuất **cơ chế bảo đảm** dữ liệu dư thừa luôn khớp.
d) Nêu **điều kiện** để phương án này chấp nhận được, đối chiếu Bảng 5.23.


??? success "Lời giải bài C3"

    ### (a) Phương án phi chuẩn hóa

    Truy vấn *"doanh thu theo tháng theo danh mục sản phẩm"* hiện phải ghép 5 bảng: `CHITIET ⋈ DONHANG ⋈ SANPHAM ⋈ DANHMUC` cộng bảng lịch.

    **Phương án: thêm hai cột đã tính sẵn vào `CHITIET`.**

    ```text
    CHITIET(MADH, MASP, SOLUONG, THANHTIEN, MADM, THANG)
    ```

    - `THANHTIEN` = `SOLUONG × DONGIA` — khỏi phải ghép `SANPHAM` để lấy đơn giá
    - `MADM` — mã danh mục, chép từ `SANPHAM`, khỏi phải ghép hai bảng
    - `THANG` — chép từ `DONHANG.NGAYDAT`, khỏi phải ghép `DONHANG`

    Truy vấn báo cáo rút xuống còn **một bảng duy nhất**, nhóm theo `(THANG, MADM)`.

    *(Phương án thay thế mạnh hơn: dựng hẳn một bảng tổng hợp `DOANHTHU_THANG_DANHMUC(THANG, MADM, TONGTIEN)` cập nhật hằng đêm. Chọn phương án nào tùy yêu cầu về độ tươi của số liệu.)*

    ### (b) Dư thừa tạo ra và dị thường có thể phát sinh

    **Ba nguồn dư thừa:**

    | Cột | Dư thừa vì | Nguồn thật |
    |---|---|---|
    | `THANHTIEN` | Suy ra được từ `SOLUONG × DONGIA` | `SANPHAM.DONGIA` |
    | `MADM` | Chép lại từ bảng sản phẩm | `SANPHAM.MADM` |
    | `THANG` | Suy ra được từ ngày đặt | `DONHANG.NGAYDAT` |

    Lược đồ rơi từ 3NF xuống **2NF** — thậm chí thấp hơn, vì `MASP → MADM` là phụ thuộc bộ phận vào khóa `(MADH, MASP)`.

    **Dị thường có thể phát sinh:**

    - **Dị thường sửa, loại nguy hiểm nhất.** Sản phẩm được chuyển sang danh mục khác. Cột `MADM` trong `SANPHAM` đổi, nhưng hàng triệu dòng `CHITIET` cũ vẫn giữ danh mục cũ ⇒ báo cáo doanh thu theo danh mục cho **hai kết quả khác nhau** tùy đọc từ bảng nào.
    - **Dị thường sửa với `THANHTIEN`.** Sửa đơn giá sản phẩm mà không cập nhật `THANHTIEN` ⇒ tổng doanh thu lệch với tích số lượng nhân đơn giá.
    - **Dị thường sửa với `THANG`.** Sửa ngày đặt của một đơn mà quên `THANG` ⇒ đơn hàng nằm sai tháng trong báo cáo.

    !!! warning "Một chi tiết nghiệp vụ quan trọng"

        `THANHTIEN` **không hoàn toàn** là dư thừa. Nếu đơn giá sản phẩm thay đổi theo thời gian thì `THANHTIEN` phải giữ **giá tại thời điểm bán**, và khi ấy nó là **dữ liệu lịch sử thật sự**, không suy lại được từ đơn giá hiện hành. Trong trường hợp đó, lưu `THANHTIEN` là **thiết kế đúng** chứ không phải phi chuẩn hóa. Phải làm rõ điều này với nghiệp vụ trước khi quyết định.

    ### (c) Cơ chế bảo đảm dữ liệu dư thừa luôn khớp

    Ba lớp, dùng phối hợp:

    **Lớp 1 — Chặn tại nguồn bằng trigger.** Trên `CHITIET`, khi thêm hoặc sửa thì tự lấy `MADM` từ `SANPHAM` và `THANG` từ `DONHANG` thay vì để người nhập tự điền. Trên `SANPHAM`, khi `MADM` đổi thì lan truyền cập nhật xuống `CHITIET`.

    **Lớp 2 — Đối soát định kỳ.** Một tác vụ chạy hằng đêm so cột chép với nguồn thật, ghi ra bảng nhật ký các dòng lệch:

    ```text
    σ (CHITIET.MADM ≠ SANPHAM.MADM) ( CHITIET ⋈ SANPHAM )
    ```

    Đây là lưới an toàn cho những đường ghi lọt qua lớp 1 — nhập hàng loạt, khôi phục sao lưu.

    **Lớp 3 — Ghi rõ vào tài liệu thiết kế.** Nêu đích danh ba cột này là **cố ý phi chuẩn hóa**, kèm lý do và cơ chế đồng bộ. Không có dòng này thì người bảo trì sau sẽ tưởng là lỗi thiết kế và hoặc xóa đi, hoặc thêm một cột dư thừa nữa.

    Chi phí của cả ba lớp phải được tính vào bài toán đánh đổi. Nếu tổng chi phí ấy lớn hơn 40 giây tiết kiệm được thì phương án không đáng làm.

    ### (d) Điều kiện để phương án chấp nhận được

    Đối chiếu Bảng 5.11:

    | Điều kiện | Tình huống này | Đạt? |
    |---|---|:--:|
    | **Đọc nhiều, ghi ít** | Đơn hàng đã chốt hầu như không sửa; báo cáo chạy liên tục | ✔ |
    | **Đã thử mọi cách khác trước** | Phải kiểm: đã thêm chỉ mục chưa, đã viết lại truy vấn chưa, đã xem lại thiết kế chưa | **cần kiểm** |
    | **Lợi ích đo được** | 40 giây → dưới 1 giây là con số cụ thể, kiểm chứng được | ✔ |
    | **Có cơ chế bảo đảm nhất quán** | Ba lớp ở câu (c) | ✔ nếu làm đủ |
    | **Ghi rõ vào tài liệu** | Bắt buộc | ✔ nếu làm |
    | **Phạm vi hẹp, có kiểm soát** | Chỉ ba cột, chỉ phục vụ báo cáo | ✔ |

    **Điều kiện chưa chắc đạt là dòng thứ hai**, và nó phải kiểm **trước tiên**. 40 giây cho một truy vấn tổng hợp thường là dấu hiệu **thiếu chỉ mục** trên `NGAYDAT` và `MASP`, hoặc truy vấn viết chưa tốt. Thêm chỉ mục là thao tác **thuần túy ở mức trong**, không đụng tới lược đồ logic, không sinh dư thừa nào — nếu nó đưa được 40 giây xuống 2 giây thì bài toán đã xong mà không phải trả giá gì.

    **Kết luận:** phi chuẩn hóa là **phương án cuối cùng**, không phải phản xạ đầu tiên khi gặp truy vấn chậm. Đúng như mục 5.10 nhấn mạnh, nó là một quyết định **có cân nhắc và ghi chép**, khác hẳn với việc thiết kế cẩu thả rồi gọi tên cho sang.

**Bài C4** *(tự chọn).* Tìm hiểu về **dạng chuẩn 5 (5NF)** hay *dạng chuẩn nối*. Cho một ví dụ về quan hệ phải tách thành **ba bảng** mới bảo toàn thông tin, và giải thích vì sao tách thành hai bảng là không đủ.

---


??? success "Lời giải bài C4"

    Bài tự chọn. Dưới đây là mức trả lời được coi là đạt.

    **Dạng chuẩn 5 là gì.** 5NF, còn gọi là **dạng chuẩn nối** *(Project–Join Normal Form)*, xử lý trường hợp một quan hệ **không tách được thành hai** bảng mà bảo toàn thông tin, nhưng **tách được thành ba**. Quan hệ `R` đạt 5NF nếu mọi phép tách nối bảo toàn thông tin của nó đều suy ra được từ các **khóa** của `R`.

    **Ví dụ ba bảng.** Xét quan hệ mô tả việc *đại lý phân phối sản phẩm của hãng*:

    `CUNGCAP(DAILY, HANG, SANPHAM)`

    với quy tắc nghiệp vụ đặc biệt:

    > Nếu đại lý `D` có bán hàng của hãng `H`, **và** đại lý `D` có phân phối sản phẩm `S`, **và** hãng `H` có sản xuất sản phẩm `S`, thì chắc chắn `D` phân phối sản phẩm `S` **của** hãng `H`.

    Dữ liệu:

    | DAILY | HANG | SANPHAM |
    |---|---|---|
    | D1 | Samsung | Tivi |
    | D1 | Samsung | Tủ lạnh |
    | D1 | LG | Tivi |
    | D2 | Samsung | Tivi |

    **Tách thành hai bảng là không đủ.** Thử cả ba cách:

    - `(DAILY, HANG)` + `(DAILY, SANPHAM)`: ghép lại sinh dòng giả `(D1, LG, Tủ lạnh)` — vì D1 có bán LG và D1 có bán tủ lạnh, phép kết ghép chéo. Nhưng LG trong dữ liệu gốc không đi kèm tủ lạnh ở D1.
    - `(DAILY, HANG)` + `(HANG, SANPHAM)`: cũng sinh dòng giả tương tự.
    - `(DAILY, SANPHAM)` + `(HANG, SANPHAM)`: cũng vậy.

    **Tách thành ba bảng thì đủ:**

    ```text
    DL_HANG(DAILY, HANG)
    DL_SANPHAM(DAILY, SANPHAM)
    HANG_SANPHAM(HANG, SANPHAM)
    ```

    Ghép cả **ba** bảng lại bằng kết tự nhiên cho đúng bốn dòng ban đầu. Dòng giả `(D1, LG, Tủ lạnh)` bị loại vì bảng thứ ba không có cặp `(LG, Tủ lạnh)` — giả sử LG không sản xuất tủ lạnh trong ngữ cảnh này.

    **Vì sao hai bảng không đủ.** Ràng buộc nghiệp vụ ở trên là một **ràng buộc ba chiều**: nó nói về sự đồng thời của **ba** cặp quan hệ. Mỗi phép tách đôi chỉ giữ được hai trong ba cặp, nên luôn thiếu một điều kiện lọc, và phần thiếu ấy chính là chỗ bộ giả chui vào.

    **Vì sao 5NF ít gặp trong thực tế.** Ba lý do: ràng buộc kiểu *nối ba chiều* rất hiếm trong nghiệp vụ thông thường; nó khó phát hiện vì không lộ ra qua phụ thuộc hàm hay phụ thuộc đa trị; và tách ra ba bảng làm mọi truy vấn phải ghép ba lần. Vì vậy giáo trình dừng ở BCNF và 4NF là hợp lý — biết 5NF tồn tại để nhận ra khi gặp, chứ không phải để áp dụng thường xuyên.
