# 2.4. Liên kết và kỹ thuật hỏi hai chiều

*(1,0 tiết)*

## 2.4.1. Liên kết

!!! note "Định nghĩa 2.7"

    **Liên kết** *(relationship)* là một **mối liên hệ có ý nghĩa nghiệp vụ** giữa các thực thể.

    Trong ký pháp Chen, liên kết được vẽ bằng một **hình thoi** đặt giữa hai thực thể, bên trong ghi **động từ** mô tả mối liên hệ.

Trong quy tắc nghiệp vụ, liên kết thường xuất hiện dưới dạng **động từ** nối hai danh từ: giáo viên **phụ trách** lớp, học viên **ghi danh** lớp, khóa học **là tiên quyết của** khóa học khác.

Việc dành hẳn một ký hiệu riêng cho liên kết là một lựa chọn có chủ ý của Chen, và nó có giá trị thực tế. Vì liên kết là một hình độc lập chứ không phải chỉ là một đường kẻ, **nó có chỗ để mang thuộc tính riêng** — điều sẽ trở nên thiết yếu ở mục 2.6.4 khi ta gặp liên kết nhiều–nhiều có thuộc tính. Ký pháp Crow's Foot vẽ liên kết chỉ bằng một đường nối, nên khi liên kết có thuộc tính thì buộc phải tạo thêm một ô chữ nhật — tức là phải quyết định sớm hơn.

Việc phát hiện ra có một liên kết thường không khó. Cái khó nằm ở bước tiếp theo: **xác định cho đúng loại liên kết ấy là 1:1, 1:M hay M:N**. Xác định sai ở đây kéo theo sai toàn bộ thiết kế các bước sau, và đây là lỗi phổ biến nhất của người mới học.

## 2.4.2. Kỹ thuật hỏi hai chiều

Có một kỹ thuật đơn giản loại bỏ gần như hoàn toàn khả năng nhầm lẫn: **luôn đặt hai câu hỏi, mỗi câu cho một chiều**, rồi ghép hai câu trả lời lại.

**Hình 2.5. Kỹ thuật hỏi hai chiều — quy trình xác định loại liên kết**

```mermaid
flowchart TB
    Q1["<b>CÂU HỎI 1</b><br/>Một <b>[A]</b> liên quan tới<br/><b>BAO NHIÊU [B]</b>?"]
    Q2["<b>CÂU HỎI 2</b><br/>Một <b>[B]</b> liên quan tới<br/><b>BAO NHIÊU [A]</b>?"]
    Q1 --> G{"Ghép hai<br/>câu trả lời"}
    Q2 --> G
    G -->|"Một + Một"| R1["<b>1:1</b>"]
    G -->|"Nhiều + Một"| R2["<b>1:M</b>"]
    G -->|"Một + Nhiều"| R3["<b>1:M</b><br/><i>đảo chiều</i>"]
    G -->|"Nhiều + Nhiều"| R4["<b>M:N</b><br/><i>bắt buộc phải tách</i>"]
    style Q1 fill:#1F4E79,color:#fff,stroke:#1F4E79
    style Q2 fill:#1F4E79,color:#fff,stroke:#1F4E79
    style R4 fill:#FFD9D9,stroke:#C00000,stroke-width:2px
    style G fill:#FFF2CC,stroke:#C00000
```

Sức mạnh của kỹ thuật này nằm ở chỗ nó **buộc người thiết kế phải hỏi cả chiều ngược lại** — mà chiều ngược lại chính là chiều người ta hay quên. Khi nghe *"một giáo viên phụ trách nhiều lớp"*, phản xạ tự nhiên là kết luận ngay 1:M. Nhưng nếu không hỏi tiếp *"một lớp do bao nhiêu giáo viên phụ trách?"*, ta có thể bỏ sót trường hợp trung tâm cho phép hai giáo viên đồng phụ trách một lớp — và khi ấy liên kết thật sự là M:N.

## 2.4.3. Áp dụng cho Trung tâm Anh ngữ ABC

**Bảng 2.7. Bảng hỏi hai chiều cho Trung tâm ABC**

| Cặp thực thể | Câu hỏi chiều thứ nhất | Câu hỏi chiều thứ hai | Kết luận |
|---|---|---|:--:|
| `GIAOVIEN` – `LOP` | Một giáo viên phụ trách bao nhiêu lớp? → **Nhiều** *(hoặc chưa lớp nào)* | Một lớp do bao nhiêu giáo viên phụ trách? → **Một** | **1:M** |
| `KHOAHOC` – `LOP` | Một khóa học mở bao nhiêu lớp? → **Nhiều** | Một lớp thuộc bao nhiêu khóa học? → **Một** | **1:M** |
| `HOCVIEN` – `DIENTHOAI` | Một học viên có bao nhiêu số? → **Nhiều** | Một số thuộc bao nhiêu học viên? → **Một** | **1:M** |
| `HOCVIEN` – `LOP` | Một học viên ghi danh bao nhiêu lớp? → **Nhiều** | Một lớp có bao nhiêu học viên? → **Nhiều** | **M:N** |
| `KHOAHOC` – `KHOAHOC` | Một khóa là tiên quyết của bao nhiêu khóa? → **Nhiều** | Một khóa có bao nhiêu khóa tiên quyết? → **Nhiều** | **M:N đệ quy** |

Hai dòng cuối cần lưu ý đặc biệt vì chúng là **liên kết nhiều–nhiều**, và như mục 2.6.4 sẽ chỉ ra, loại liên kết này **bắt buộc phải tách** trước khi chuyển sang thiết kế bảng.

---


---

[← Trang trước](2-3-thuoc-tinh-khoa-va-dinh-danh.md) · [Trang sau →](2-5-ket-noi-luc-luong-va-su-tham-gia.md)
