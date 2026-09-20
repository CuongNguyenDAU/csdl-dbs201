# 5.3. Hệ luật dẫn Armstrong

*(1,0 tiết)*

Tập `F` mà người thiết kế thu thập được từ nghiệp vụ thường chỉ là **một phần** các phụ thuộc hàm thật sự tồn tại. Nhiều phụ thuộc khác **suy ra được** từ `F`. Hệ luật Armstrong *(1974)* cho biết cách suy.

## 5.3.1. Ba luật gốc

!!! note "Định nghĩa 5.5 (Hệ tiên đề Armstrong)"

    Cho `X`, `Y`, `Z` là các tập thuộc tính của quan hệ `R`:

    - **Luật phản xạ** *(reflexivity)*: nếu `Y ⊆ X` thì `X → Y`.
    - **Luật tăng trưởng** *(augmentation)*: nếu `X → Y` thì `XZ → YZ`.
    - **Luật bắc cầu** *(transitivity)*: nếu `X → Y` và `Y → Z` thì `X → Z`.

Ba luật này là **đúng đắn** *(mọi thứ suy ra được đều đúng)* và **đầy đủ** *(mọi thứ đúng đều suy ra được)* — đó là kết quả do Armstrong chứng minh, và cũng là lý do chỉ cần ba luật này là đủ.

Trong ba luật, **luật phản xạ** thoạt nhìn có vẻ vô nghĩa: *biết `(MAHV, MALOP)` thì biết `MAHV`* — hiển nhiên. Nhưng chính vì hiển nhiên mà nó cần thiết: nó cho phép sinh ra các **phụ thuộc tầm thường** *(trivial)*, làm điểm khởi đầu cho các phép suy diễn khác.

## 5.3.2. Ba luật dẫn xuất

Từ ba luật gốc suy ra được ba luật tiện dụng hơn khi làm bài.

**Bảng 5.6. Ba luật gốc và ba luật dẫn xuất**

| Luật | Phát biểu | Loại |
|---|---|---|
| **Phản xạ** | `Y ⊆ X` ⟹ `X → Y` | Gốc |
| **Tăng trưởng** | `X → Y` ⟹ `XZ → YZ` | Gốc |
| **Bắc cầu** | `X → Y`, `Y → Z` ⟹ `X → Z` | Gốc |
| **Hợp** *(union)* | `X → Y`, `X → Z` ⟹ `X → YZ` | Dẫn xuất |
| **Tách** *(decomposition)* | `X → YZ` ⟹ `X → Y` và `X → Z` | Dẫn xuất |
| **Bắc cầu giả** *(pseudotransitivity)* | `X → Y`, `WY → Z` ⟹ `WX → Z` | Dẫn xuất |

Hai luật **hợp** và **tách** dùng nhiều nhất trong thực hành, vì chúng cho phép **gộp** hoặc **tách** vế phải tùy tiện. Nhờ đó ta luôn có thể viết `F` ở dạng **mỗi phụ thuộc chỉ có một thuộc tính ở vế phải** — điều kiện đầu tiên của phủ tối thiểu ở mục 5.6.

Sáu luật viết bằng `X`, `Y`, `Z` trông khô, nhưng thay bằng thuộc tính của Trung tâm ABC thì luật nào cũng chỉ là một câu nói hiển nhiên.

**Bảng 5.7. Sáu luật, mỗi luật một ví dụ tại ABC**

| Luật | Ví dụ | Đọc thành lời |
|---|---|---|
| Phản xạ | `(MAHV, MALOP) → MAHV` | biết cả cặp thì đương nhiên biết mã học viên |
| Tăng trưởng | `MAGV → HOTEN_GV` ⟹ `(MAGV, MALOP) → (HOTEN_GV, MALOP)` | thêm cùng một thứ vào hai vế, phụ thuộc vẫn đúng |
| Bắc cầu | `MALOP → MAGV`, `MAGV → HOTEN_GV` ⟹ `MALOP → HOTEN_GV` | biết lớp thì biết giáo viên, biết giáo viên thì biết tên — vậy biết lớp là biết tên |
| Hợp | `MALOP → TENLOP`, `MALOP → MAGV` ⟹ `MALOP → (TENLOP, MAGV)` | hai điều cùng suy từ lớp thì gộp lại vẫn suy từ lớp |
| Tách | `MALOP → (TENLOP, MAGV)` ⟹ `MALOP → TENLOP` và `MALOP → MAGV` | suy được cả cụm thì suy được từng phần |
| Bắc cầu giả | `MALOP → MAGV`, `(NGAY, MAGV) → PHONG` ⟹ `(NGAY, MALOP) → PHONG` | nếu mỗi giáo viên mỗi ngày dạy ở một phòng, thì biết lớp và ngày là biết phòng |

Dòng **bắc cầu** đáng chú ý nhất: hai phụ thuộc đầu vào đều "vô hại", nhưng kết quả `MALOP → HOTEN_GV` chính là phụ thuộc bắc cầu ở Bảng 5.5 — luật Armstrong làm lộ ra thủ phạm mà mắt thường dễ bỏ qua.

!!! example "Ví dụ 5.2"

    Cho `F = {A → B, B → C}`. Chứng minh `A → BC`.

    | Bước | Suy luận | Luật dùng |
    |:--:|---|---|
    | 1 | `A → B` | giả thiết |
    | 2 | `B → C` | giả thiết |
    | 3 | `A → C` | bắc cầu (1, 2) |
    | 4 | `A → BC` | hợp (1, 3) |

## 5.3.3. Vì sao cần hệ luật này

Có hai lý do thực dụng.

Thứ nhất, hệ luật Armstrong là **nền tảng của thuật toán bao đóng** ở mục 5.4 — thuật toán ấy chính là việc áp luật bắc cầu lặp đi lặp lại một cách có hệ thống.

Thứ hai, nó cho phép **phát hiện phụ thuộc bắc cầu ẩn**. Nhìn vào `F = {MALOP → MAGV, MAGV → HOTEN_GV}` thì hai phụ thuộc trông vô hại, nhưng luật bắc cầu cho ra `MALOP → HOTEN_GV` — và đó chính là vi phạm 3NF. Không có luật này, người thiết kế phải nhìn ra bằng mắt, tức lại quay về trực giác.

---


---

[← Trang trước](5-2-ba-loai-phu-thuoc-ham.md) · [Trang sau →](5-4-bao-dong-cua-tap-thuoc-tinh.md)
