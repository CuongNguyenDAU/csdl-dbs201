# Lời giải bài tập Chương 3

## A1

`SANPHAM(MASP, TENSP, DONGIA, MANCC)` với 120 dòng.

- **Bậc = 4** — đếm số thuộc tính. Bậc thuộc về **lược đồ** nên rất ít khi đổi.
- **Lực lượng = 120** — đếm số bộ. Lực lượng thuộc về **thể hiện** nên đổi mỗi lần thêm hoặc xóa một sản phẩm.

**Khóa chính: `MASP`.** Nó duy nhất (mỗi sản phẩm một mã) và tối thiểu (chỉ một thuộc tính, không bỏ bớt được). `TENSP` không dùng được vì hai sản phẩm khác nhau có thể trùng tên. Cặp `(MASP, TENSP)` duy nhất nhưng **vi phạm tính tối thiểu**.

**Khóa ngoại: `MANCC`** — trỏ tới khóa chính của `NHACUNGCAP`. Khóa ngoại này **được phép rỗng** nếu nghiệp vụ cho phép nhập sản phẩm khi chưa xác định nhà cung cấp; nếu quy định mọi sản phẩm đều phải có nhà cung cấp thì đặt ràng buộc không rỗng.

Ba con số cần phân biệt cho rõ: bậc 4 là số cột, lực lượng 120 là số dòng, và số ô là 4 × 120 = 480.

## A2

| Cặp | Khả hợp? | Giải thích |
|---|:--:|---|
| (a) `A(MASV, HOTEN)` và `B(MAGV, HOTEN_GV)` | **Có** | Cùng bậc 2. Tên thuộc tính khác nhau **không sao** — điều kiện chỉ đòi các thuộc tính tương ứng theo thứ tự cùng miền giá trị. Mã sinh viên và mã giáo viên cùng miền chuỗi, họ tên và họ tên giáo viên cùng miền chuỗi ⇒ khả hợp |
| (b) `A(MASV, HOTEN)` và `C(MASV, HOTEN, DIEM)` | **Không** | Bậc 2 với bậc 3 — vi phạm điều kiện thứ nhất ngay lập tức. Trùng tên hai thuộc tính đầu không cứu được |
| (c) `A(MASV, HOTEN)` và `D(MASV, NGAYSINH)` | **Không** | Cùng bậc 2 nhưng thuộc tính thứ hai là *họ tên* (chuỗi) với *ngày sinh* (kiểu ngày) — khác miền giá trị |

Cặp (c) là bẫy hay mắc nhất: nhìn qua thấy cùng số cột và trùng tên cột đầu nên tưởng khả hợp. Phải kiểm **từng cặp thuộc tính tương ứng**, không phải chỉ đếm cột.

Khả hợp là điều kiện bắt buộc của ba phép toán tập hợp `∪`, `∩`, `−`. Riêng tích Descartes `×` và phép kết `⋈` **không đòi** khả hợp.

## A3

| Phép toán | Câu hỏi nghiệp vụ tại Trung tâm ABC |
|---|---|
| **Chọn** `σ` | *Những lớp nào khai giảng sau ngày 01/09/2025?* |
| **Chiếu** `π` | *Danh sách các mức học phí khác nhau mà trung tâm đang áp dụng?* |
| **Hợp** `∪` | *Danh sách mọi người có mặt tại trung tâm — gộp học viên và nhân sự?* |
| **Giao** `∩` | *Những học viên vừa ghi danh lớp A1 vừa ghi danh lớp B2?* |
| **Hiệu** `−` | *Những học viên chưa ghi danh lớp nào?* |
| **Tích Descartes** `×` | *Lập bảng mọi cặp (giáo viên, lớp) có thể có, để xếp lịch thử?* |
| **Kết** `⋈` | *Tên học viên kèm tên lớp họ đang học?* |
| **Chia** `÷` | *Học viên nào đã ghi danh tất cả các lớp bắt buộc của chương trình?* |

Ba câu đáng chú ý:

- **Chiếu** có tác dụng phụ là **loại bỏ bộ trùng lặp**, nên câu hỏi *"các mức học phí khác nhau"* đúng là việc của phép chiếu chứ không phải phép chọn.
- **Tích Descartes** hiếm khi dùng một mình vì kết quả rất lớn và phần lớn vô nghĩa; nó thường là bước trung gian của phép kết.
- **Chia** luôn ứng với câu hỏi có chữ **tất cả** hoặc **mọi**.

## B1

### (a) Ánh xạ theo bốn quy tắc

Lược đồ ER thư viện ở Bài B1 Chương 2 có bảy thực thể sau Bước 4.

| Quy tắc | Áp cho | Kết quả |
|:--:|---|---|
| **QT1** — thực thể mạnh thành quan hệ | `THELOAI`, `DAUSACH`, `TACGIA`, `BANSAO`, `DOCGIA` | Mỗi thực thể một bảng, khóa chính giữ nguyên |
| **QT2** — liên kết 1:M đặt khóa ngoại ở bên nhiều | `THELOAI`–`DAUSACH`, `DAUSACH`–`BANSAO` | `MATL` vào `DAUSACH`; `MADS` vào `BANSAO` |
| **QT3** — liên kết M:N sinh quan hệ mới | `DAUSACH`–`TACGIA`, `DOCGIA`–`BANSAO` | Sinh `VIET` và `MUON`, khóa chính là khóa phức hợp |
| **QT4** — thuộc tính đa trị tách thành quan hệ riêng | đã xử lý ở Bước 4 Chương 2 | không phát sinh thêm |

Lược đồ quan hệ đầy đủ:

```text
THELOAI(MATL, TENTL)
DAUSACH(MADS, TENSACH, NAMXB, MATL)
TACGIA(MATG, HOTEN_TG)
VIET(MADS, MATG)
BANSAO(MABS, TINHTRANG, MADS)
DOCGIA(MADG, HOTEN, NGAYSINH)
MUON(MADG, MABS, NGAYMUON, NGAYHENTRA)
```

### (b) Khóa chính và khóa ngoại

| Quan hệ | Khóa chính | Khóa ngoại | Trỏ tới |
|---|---|---|---|
| `THELOAI` | `MATL` | — | — |
| `DAUSACH` | `MADS` | `MATL` | `THELOAI` |
| `TACGIA` | `MATG` | — | — |
| `VIET` | `(MADS, MATG)` | `MADS` · `MATG` | `DAUSACH` · `TACGIA` |
| `BANSAO` | `MABS` | `MADS` | `DAUSACH` |
| `DOCGIA` | `MADG` | — | — |
| `MUON` | `(MADG, MABS)` | `MADG` · `MABS` | `DOCGIA` · `BANSAO` |

Hai bảng sinh từ QT3 có đặc điểm chung: **mọi thành phần của khóa chính đồng thời là khóa ngoại**. Đó là dấu hiệu nhận ra một bảng nối.

### (c) Bảng đối chiếu toàn vẹn

| Khóa ngoại | Ở bảng | Cho phép rỗng? | Vì sao |
|---|---|:--:|---|
| `MATL` | `DAUSACH` | **Không** | Quy tắc 5 nói *mỗi đầu sách thuộc một thể loại* — tham gia bắt buộc |
| `MADS` | `BANSAO` | **Không** | Một bản sao vật lý luôn là bản sao **của** một đầu sách; không có bản sao mồ côi |
| `MADS` | `VIET` | **Không** | Là thành phần khóa chính, mà toàn vẹn thực thể cấm khóa chính rỗng |
| `MATG` | `VIET` | **Không** | Cùng lý do trên |
| `MADG` | `MUON` | **Không** | Cùng lý do trên |
| `MABS` | `MUON` | **Không** | Cùng lý do trên |

!!! note "Quy tắc rút gọn"

    Khóa ngoại nằm **trong** khóa chính thì **luôn** cấm rỗng — không phải vì nghiệp vụ mà vì toàn vẹn thực thể. Chỉ những khóa ngoại **ngoài** khóa chính mới cần xét nghiệp vụ, và câu hỏi để xét chính là **tính tham gia** đã xác định ở Chương 2: tham gia bắt buộc ⇒ cấm rỗng, tham gia tùy chọn ⇒ cho rỗng.

    Ở lược đồ này mọi khóa ngoại đều cấm rỗng. Nếu thư viện cho phép nhập đầu sách chưa xếp thể loại thì `MATL` trong `DAUSACH` chuyển sang cho rỗng.

## B2

### (a) Tên các đầu sách xuất bản sau 2020

```text
π_TENSACH ( σ_(NAMXB > 2020) (DAUSACH) )
```

Thứ tự quan trọng về hiệu năng: **chọn trước, chiếu sau** để giảm số bộ phải xử lý.

### (b) Tên độc giả và tên sách họ đang mượn

```text
π_(HOTEN, TENSACH) ( DOCGIA ⋈ MUON ⋈ BANSAO ⋈ DAUSACH )
```

Phải đi qua đủ bốn bảng vì `MUON` chỉ trỏ tới **bản sao**, mà tên sách nằm ở **đầu sách**. Bỏ qua một bảng trung gian là không nối được.

### (c) Các bản sao **chưa từng** được mượn

```text
π_MABS (BANSAO) − π_MABS (MUON)
```

Chữ **chưa từng** báo hiệu phép **hiệu**. Lấy tập mọi bản sao trừ đi tập bản sao đã từng xuất hiện trong lịch sử mượn. Hai vế đều là quan hệ một cột `MABS` nên khả hợp.

### (d) Liệt kê mọi độc giả, kể cả người chưa mượn cuốn nào

```text
DOCGIA ⟕ MUON
```

Chữ **kể cả** báo hiệu **kết ngoài trái**. Dùng kết tự nhiên `⋈` sẽ loại mất đúng nhóm độc giả cần giữ. Những dòng có giá trị rỗng ở phần `MUON` chính là các độc giả chưa mượn lần nào.

### (e) Độc giả đã mượn **tất cả** đầu sách thuộc thể loại "Tin học"

Chữ **tất cả** báo hiệu phép **chia**. Làm ba bước:

```text
(1) TINHOC  ← π_MADS ( σ_(TENTL = 'Tin học') (THELOAI ⋈ DAUSACH) )
(2) DAMUON  ← π_(MADG, MADS) ( MUON ⋈ BANSAO )
(3) Kết quả ← DAMUON ÷ TINHOC
```

Bước 2 cần phép kết vì `MUON` lưu **bản sao** chứ không lưu **đầu sách**; phải quy về đầu sách rồi mới chia. Kết quả gồm những `MADG` xuất hiện cùng **mọi** giá trị `MADS` có trong `TINHOC`.

## B3

### (a) Ràng buộc bị vi phạm

**Toàn vẹn tham chiếu.** `MAHV` trong `GHIDANH` là khóa ngoại trỏ tới khóa chính của `HOCVIEN`; theo Định nghĩa 3.6 nó phải **hoặc rỗng, hoặc khớp một khóa chính đang tồn tại**. Giá trị `HV99` không rỗng mà cũng không tồn tại bên `HOCVIEN`, nên dòng này là một **bộ mồ côi**.

Lưu ý thêm: ở đây `MAHV` còn là thành phần của khóa chính `(MAHV, MALOP)`, nên nó vốn cũng không được rỗng — vi phạm này không có đường thoát nào.

### (b) Biểu thức phát hiện mọi dòng lỗi tương tự

```text
π_MAHV (GHIDANH) − π_MAHV (HOCVIEN)
```

Kết quả là tập các mã học viên có trong bảng con mà không có trong bảng cha. Muốn lấy trọn dòng lỗi thay vì chỉ lấy mã:

```text
GHIDANH ⋉ ( π_MAHV (GHIDANH) − π_MAHV (HOCVIEN) )
```

hoặc dùng kết ngoài rồi lọc:

```text
σ_(HOCVIEN.MAHV IS NULL) ( GHIDANH ⟕ HOCVIEN )
```

**Không dùng được phép kết tự nhiên** `GHIDANH ⋈ HOCVIEN`: nó âm thầm loại bỏ đúng những dòng ta đang muốn tìm, và cho ra kết quả trông rất sạch.

### (c) Hai nguyên nhân thực tế

**Nguyên nhân 1 — ràng buộc không được khai báo.** Hệ quản trị **hỗ trợ** khóa ngoại không có nghĩa là nó tự động áp dụng. Nếu người tạo bảng chỉ viết `MAHV CHAR(5)` mà quên `FOREIGN KEY`, hệ quản trị không có cơ sở nào để chặn. Đây là nguyên nhân phổ biến nhất, và nó thuộc về quy trình chứ không thuộc về công nghệ.

**Nguyên nhân 2 — dữ liệu vào bằng đường vòng.** Nhập hàng loạt từ tệp CSV, khôi phục từ bản sao lưu cũ, hoặc di trú dữ liệu từ hệ thống trước. Nhiều công cụ nhập liệu cho phép **tạm tắt kiểm tra khóa ngoại** để chạy nhanh, và nếu quên bật lại thì dữ liệu bẩn đã nằm sẵn trong bảng.

Nguyên nhân thứ ba đáng nhắc: học viên `HV99` từng tồn tại rồi bị xóa, mà khóa ngoại khai báo `ON DELETE NO ACTION` nhưng ràng buộc lại đang tắt. Chương 4 sẽ bàn kỹ về việc chọn hành động khi vi phạm.

## B4

Phân cấp `NHANVIENYTE` → `BACSI` / `DIEUDUONG`, thuộc tính chung `(MANV, HOTEN, NGAYSINH, NGAYVAOLAM)`.

### Tổ hợp 1 — Rời nhau + Đầy đủ

```text
BACSI(MANV, HOTEN, NGAYSINH, NGAYVAOLAM, CHUYENKHOA, SOCHUNGCHI)
DIEUDUONG(MANV, HOTEN, NGAYSINH, NGAYVAOLAM, KHOACONGTAC, CATRUC)
```

**Bỏ bảng cha.** Mọi nhân viên thuộc **đúng một** nhóm và **không ai** đứng ngoài, nên hai bảng con đã phủ hết dữ liệu. Được lợi: mọi truy vấn về bác sĩ chỉ đọc một bảng, không cần phép kết.

Cái giá: truy vấn *"danh sách toàn bộ nhân viên y tế"* phải **hợp hai bảng**, và bốn thuộc tính chung bị khai báo hai lần — thêm một cột chung sau này phải sửa hai chỗ.

### Tổ hợp 2 — Rời nhau + Không đầy đủ

```text
NHANVIENYTE(MANV, HOTEN, NGAYSINH, NGAYVAOLAM, LOAINV)
BACSI(MANV, CHUYENKHOA, SOCHUNGCHI)
DIEUDUONG(MANV, KHOACONGTAC, CATRUC)
```

**Giữ cả ba bảng.** Bắt buộc phải có bảng cha, vì có những nhân viên — hành chính, bảo vệ — không thuộc nhóm con nào; bỏ bảng cha là mất hẳn nhóm này.

Cột `LOAINV` là **cột phân loại**, cho biết mỗi bản ghi cha có bản ghi con ở bảng nào. Nhờ tổ hợp là *rời nhau* nên một cột đủ dùng.

### Tổ hợp 3 — Chồng lấn + Đầy đủ

```text
NHANVIENYTE(MANV, HOTEN, NGAYSINH, NGAYVAOLAM)
BACSI(MANV, CHUYENKHOA, SOCHUNGCHI)
DIEUDUONG(MANV, KHOACONGTAC, CATRUC)
```

**Giữ ba bảng, bỏ cột phân loại.** Vì một người có thể thuộc **cả hai** nhóm, một cột phân loại không diễn tả nổi; thay vào đó, sự có mặt của `MANV` trong bảng con nào chính là câu trả lời.

Không thể gộp thành một bảng: người kiêm cả hai vai trò sẽ phải có hai chuyên khoa hay hai ca trực trong cùng một dòng.

### Tổ hợp 4 — Chồng lấn + Không đầy đủ

Lược đồ **giống hệt tổ hợp 3**. Đây là trường hợp tổng quát nhất và ít ràng buộc nhất; ba bảng riêng luôn dùng được.

Khác biệt không nằm ở lược đồ mà ở **ràng buộc cài đặt**: với tổ hợp 3 có thể đặt ràng buộc *mọi `MANV` của bảng cha phải xuất hiện ở ít nhất một bảng con*, còn tổ hợp 4 thì không được phép đặt ràng buộc ấy.

### Tổng kết

| Tổ hợp | Số bảng | Có cột phân loại? | Ghi chú |
|---|:--:|:--:|---|
| Rời nhau + đầy đủ | 2 | không | Bỏ được bảng cha |
| Rời nhau + không đầy đủ | 3 | **có** | Bắt buộc giữ bảng cha |
| Chồng lấn + đầy đủ | 3 | không | Có thêm ràng buộc phủ |
| Chồng lấn + không đầy đủ | 3 | không | Tổng quát nhất |

Bài học: **hai ràng buộc xác định ở Chương 2 quyết định trực tiếp lược đồ ở Chương 3.** Xác định sai ở mức quan niệm thì sai luôn ở mức logic, và đó là lý do không được bỏ qua bước ấy.

## C1

**Cần chứng minh:** `R ∩ S = R − (R − S)` với `R`, `S` khả hợp.

### Chứng minh bằng lập luận trên phần tử

Gọi `t` là một bộ bất kỳ.

**Chiều thuận — nếu `t ∈ R ∩ S` thì `t ∈ R − (R − S)`.**

`t ∈ R ∩ S` nghĩa là `t ∈ R` **và** `t ∈ S`.
Vì `t ∈ S` nên `t ∉ (R − S)`, do `R − S` chỉ chứa các bộ thuộc `R` mà **không** thuộc `S`.
Vậy `t ∈ R` và `t ∉ (R − S)`, tức đúng định nghĩa `t ∈ R − (R − S)`.

**Chiều nghịch — nếu `t ∈ R − (R − S)` thì `t ∈ R ∩ S`.**

`t ∈ R − (R − S)` nghĩa là `t ∈ R` **và** `t ∉ (R − S)`.
Ta có `t ∈ R`. Giả sử phản chứng `t ∉ S`; khi ấy `t ∈ R` và `t ∉ S` nên `t ∈ (R − S)`, mâu thuẫn.
Vậy `t ∈ S`. Kết hợp lại: `t ∈ R` và `t ∈ S`, tức `t ∈ R ∩ S`.

Hai chiều đều đúng ⇒ hai quan hệ bằng nhau. ∎

### Kiểm chứng bằng ví dụ

`R = {a, b, c}`, `S = {b, c, d}`.

| Bước | Kết quả |
|---|---|
| `R − S` | `{a}` |
| `R − (R − S)` | `{a, b, c} − {a}` = `{b, c}` |
| `R ∩ S` | `{b, c}` |

Khớp nhau.

### Ý nghĩa

Phép giao **không nguyên thủy** — có thể loại khỏi tập phép toán cơ sở mà không mất khả năng diễn đạt. Tập nguyên thủy tối thiểu của đại số quan hệ gồm năm phép: **chọn, chiếu, hợp, hiệu, tích Descartes**. Phép giao, phép kết và phép chia đều diễn đạt lại được qua năm phép ấy.

Điều này quan trọng về mặt lý thuyết — chỉ cần cài đặt đúng năm phép là đủ — nhưng trong thực hành ta vẫn dùng phép giao và phép kết vì chúng diễn đạt ý định rõ hơn nhiều và hệ quản trị tối ưu chúng riêng.

## C2

Tính `R ÷ S` với `R = GHIDANH(MAHV, MALOP)` và `S` là tập ba lớp bắt buộc.

### Dữ liệu

`S = {A1, A2, A3}`

| `MAHV` | `MALOP` |
|---|---|
| HV01 | A1 |
| HV01 | A2 |
| HV01 | A3 |
| HV01 | B1 |
| HV02 | A1 |
| HV02 | A2 |
| HV03 | A1 |
| HV03 | A2 |
| HV03 | A3 |
| HV04 | B1 |

Câu hỏi: *học viên nào đã ghi danh **tất cả** ba lớp bắt buộc?*

Nhìn bằng mắt thì đáp án là `{HV01, HV03}`. Dưới đây là năm bước máy móc cho ra đúng kết quả ấy.

### Bước 1 — Chiếu lấy tập ứng viên

```text
T1 ← π_MAHV (R)  =  {HV01, HV02, HV03, HV04}
```

Mọi học viên từng ghi danh ít nhất một lớp.

### Bước 2 — Dựng mọi cặp cần phải có

```text
T2 ← T1 × S
```

12 cặp: mỗi học viên ghép với cả ba lớp bắt buộc. Đây là bảng *lẽ ra phải có* nếu ai cũng học đủ.

| `MAHV` | `MALOP` |
|---|---|
| HV01 | A1, A2, A3 |
| HV02 | A1, A2, A3 |
| HV03 | A1, A2, A3 |
| HV04 | A1, A2, A3 |

### Bước 3 — Tìm các cặp còn thiếu

```text
T3 ← T2 − R
```

| `MAHV` | `MALOP` | Ghi chú |
|---|---|---|
| HV02 | A3 | HV02 chưa học A3 |
| HV04 | A1 | HV04 chưa học A1 |
| HV04 | A2 | |
| HV04 | A3 | |

### Bước 4 — Lấy ra những học viên bị thiếu

```text
T4 ← π_MAHV (T3)  =  {HV02, HV04}
```

Chỉ cần thiếu **một** cặp là học viên đó bị loại.

### Bước 5 — Loại khỏi tập ứng viên

```text
Kết quả ← T1 − T4  =  {HV01, HV03}
```

### Nhận xét

- `HV01` có ghi danh thêm lớp `B1` ngoài ba lớp bắt buộc, và vẫn thuộc kết quả — phép chia đòi **chứa hết** `S` chứ không đòi **bằng** `S`.
- Ý tưởng của thuật toán là **loại trừ**: thay vì tìm ai đủ, ta tìm ai thiếu rồi loại đi. Cách này máy móc hơn nhưng chạy đúng trên mọi dữ liệu.
- Nếu `S` rỗng thì mọi học viên đều thỏa, vì không có cặp nào bị thiếu.

## C3

Ý kiến *"cứ khai báo đủ khóa chính và khóa ngoại là cơ sở dữ liệu an toàn"* nhầm lẫn giữa **toàn vẹn cấu trúc** và **toàn vẹn nghiệp vụ**.

**Hai ràng buộc ấy bảo vệ được gì.** Toàn vẹn thực thể bảo đảm mọi bản ghi đều **định danh được** và không trùng nhau. Toàn vẹn tham chiếu bảo đảm mọi tham chiếu đều **trỏ tới thứ có thật**. Đó là hai bảo đảm rất mạnh và không thể thiếu — nhưng chúng chỉ nói về **hình dạng** của dữ liệu, không nói gì về **ý nghĩa**.

**Ba tình huống tại Trung tâm ABC mà hai ràng buộc ấy không chặn được.**

**Tình huống 1 — giá trị nằm ngoài miền hợp lệ.**
Nhân viên nhập nhầm dấu, `GHIDANH` có dòng với `HOCPHI = -2000000`. Khóa chính `(MAHV, MALOP)` vẫn duy nhất và không rỗng; khóa ngoại vẫn trỏ tới học viên và lớp có thật. Cả hai ràng buộc đều **hài lòng**, trong khi trung tâm vừa ghi nhận một khoản học phí âm. Báo cáo doanh thu cuối tháng sẽ sai mà không ai biết vì sao.

**Tình huống 2 — quan hệ sai giữa hai cột trong cùng một dòng.**
Lớp `A1` có `NGAYKG = '2025-03-01'` còn `NGAYKT = '2025-01-15'` — ngày kết thúc **trước** ngày khai giảng. Mỗi cột xét riêng đều là một ngày hợp lệ, khóa chính vẫn ổn, không có khóa ngoại nào bị đụng tới. Lỗi nằm ở **quan hệ giữa hai cột**, thứ mà hai ràng buộc cấu trúc không hề nhìn tới.

**Tình huống 3 — vi phạm quy định số lượng của nghiệp vụ.**
Trung tâm quy định *mỗi lớp nhiều nhất 25 học viên*. Nhân viên ghi danh học viên thứ 30 vào lớp `A1`. Dòng mới có khóa chính hợp lệ, hai khóa ngoại đều trỏ tới bản ghi có thật. Không ràng buộc cấu trúc nào bị vi phạm, trong khi lớp đã vượt sĩ số và phòng học không đủ chỗ ngồi.

**Ba lỗ hổng ấy thuộc ba loại khác nhau** — miền giá trị, liên thuộc tính, và liên bộ — và chính là bản đồ của Chương 4. Kết luận đúng phải là: khóa chính và khóa ngoại là **điều kiện cần**, không phải điều kiện đủ. Chúng bảo vệ bộ xương của dữ liệu; phần thịt do các ràng buộc toàn vẹn khác lo, và phải phát biểu riêng cho từng nghiệp vụ.

Có một hệ quả thực tiễn đáng nói thêm: vì hai ràng buộc cấu trúc được hệ quản trị hỗ trợ sẵn nên người thiết kế hay dừng lại ở đó. Các ràng buộc nghiệp vụ thì phải tự phát hiện và tự khai báo — không ai nhắc, và không khai thì hệ thống vẫn chạy êm cho tới ngày dữ liệu bẩn lộ ra.

## C4

Bài tự chọn, cùng dạng với bài C3 của Chương 1. Dưới đây là ba quy tắc gắn với nội dung Chương 3, để bài làm bám vào thứ vừa học.

**Quy tắc 2 — Quy tắc truy cập được bảo đảm.** Mọi giá trị nguyên tử trong cơ sở dữ liệu phải truy cập được bằng đúng ba thứ: **tên bảng, giá trị khóa chính, tên cột**. Không cần biết dữ liệu nằm ở đâu trên đĩa, cũng không cần biết nó là dòng thứ mấy.

*Ví dụ:* muốn lấy học phí của học viên `HV01` ở lớp `A1`, ta nói *bảng `GHIDANH`, khóa `(HV01, A1)`, cột `HOCPHI`* — không phải *dòng thứ 47 của tệp*. Đây chính là lý do khóa chính **cấm rỗng**: nếu khóa chính rỗng thì tọa độ này mất một chiều và ô dữ liệu ấy không truy cập được.

**Quy tắc 6 — Quy tắc cập nhật khung nhìn.** Mọi khung nhìn về lý thuyết cập nhật được thì hệ quản trị cũng phải cho cập nhật được.

*Ví dụ:* khung nhìn *danh sách lớp đang mở* dựng bằng `σ_(TRANGTHAI = 'đang mở') (LOP)` — sửa tên lớp qua khung nhìn này là hợp lý và phải làm được. Nhưng khung nhìn *sĩ số từng lớp* dựng bằng phép đếm thì **không** cập nhật được, vì không có cách nào suy ngược từ con số 25 ra việc phải thêm hay bớt học viên nào. Đây là quy tắc mà cho tới nay chưa hệ quản trị nào thỏa mãn hoàn toàn.

**Quy tắc 10 — Độc lập về toàn vẹn.** Các ràng buộc toàn vẹn phải khai báo được **trong chính cơ sở dữ liệu** và lưu ở từ điển dữ liệu, không phải nằm rải rác trong mã ứng dụng.

*Ví dụ:* quy định *học phí phải lớn hơn 0* nên khai bằng `CHECK (HOCPHI > 0)` ngay trên bảng. Nếu chỉ kiểm tra trong phần mềm ghi danh thì khi trung tâm viết thêm một công cụ nhập liệu hàng loạt, quy định ấy biến mất. Quy tắc này chính là lập luận nền của Chương 4 về việc đặt ràng buộc ở tầng cơ sở dữ liệu thay vì ở tầng ứng dụng.

Bài làm đạt yêu cầu cần: chọn đúng ba quy tắc, **diễn giải bằng lời của mình**, và mỗi quy tắc có một ví dụ **cụ thể, kiểm chứng được** — tốt nhất lấy từ lược đồ thư viện hoặc Trung tâm ABC đã làm.
