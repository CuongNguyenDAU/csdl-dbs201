# 2.5. Kết nối, lực lượng và sự tham gia

*(1,0 tiết)*

## 2.5.1. Kết nối và lực lượng

Hai khái niệm này thường bị dùng lẫn, nhưng chúng mô tả hai mức chi tiết khác nhau của cùng một sự việc.

!!! note "Định nghĩa 2.8"

    **Kết nối** *(connectivity)* mô tả **loại** của liên kết ở mức khái quát: một–một *(1:1)*, một–nhiều *(1:M)* hay nhiều–nhiều *(M:N)*.

    **Lực lượng** *(cardinality)* mô tả **con số cụ thể**: số lượng tối thiểu và tối đa các thể hiện tham gia, viết dưới dạng cặp `(min, max)`.

    **Ví dụ 2.4.** Quy tắc *"mỗi lớp có ít nhất 5 và nhiều nhất 25 học viên"* cho biết **kết nối** là nhiều–nhiều nếu xét cả hai chiều, còn **lực lượng** ở phía học viên là `(5, 25)`.

Trong ký pháp Chen, kết nối được ghi bằng các ký tự **`1`, `M`, `N` đặt ngay trên cạnh nối** giữa thực thể và hình thoi liên kết; còn lực lượng chi tiết thì viết dưới dạng cặp `(min, max)` đặt cạnh đó.

**Hình 2.6. Ký pháp Chen — ba loại kết nối, minh họa tại Trung tâm ABC**

```mermaid
flowchart LR
    GV1["GIAOVIEN"] ---|"1"| R1{"phụ trách"}
    R1 ---|"M"| L1["LOP"]
    HV["HOCVIEN"] ---|"M"| R2{"ghi danh"}
    R2 ---|"N"| L2["LOP"]
    NV["NHANVIEN"] ---|"1"| R3{"được cấp"}
    R3 ---|"1"| TK["TAIKHOAN"]
    style GV1 fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style L1 fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style HV fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style L2 fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style NV fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style TK fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style R1 fill:#E2F0D9,stroke:#548235
    style R2 fill:#FFD9D9,stroke:#C00000,stroke-width:2px
    style R3 fill:#E2F0D9,stroke:#548235
```

Cách đọc rất trực tiếp và đây là ưu điểm lớn của ký pháp Chen: **con số ghi ở đầu nào cho biết số lượng thực thể ở đầu đó**. Dòng thứ nhất đọc là *"một giáo viên phụ trách M lớp, một lớp do 1 giáo viên phụ trách"* — tức **1:M**. Dòng thứ hai có `M` và `N` ở hai đầu nên là **M:N**, và liên kết này được tô đỏ vì nó **bắt buộc phải tách** theo mục 2.6.4.

!!! warning "Chú ý"

    Một số tài liệu ghi con số theo quy ước ngược lại — đặt ở đầu **đối diện**. Khi đọc lược đồ của người khác, việc đầu tiên cần làm là **kiểm tra quy ước** bằng một liên kết mà bản thân mình chắc chắn biết loại, rồi mới đọc các liên kết còn lại. Giáo trình này nhất quán dùng quy ước *"con số ở đầu nào mô tả đầu đó"*.

Lực lượng chi tiết hơn kết nối, và nó ghi lại những quy định nghiệp vụ mà kết nối không diễn tả nổi. Tuy vậy phần lớn các con số lực lượng **không được hệ quản trị kiểm tra tự động** — chúng sẽ trở thành các ràng buộc toàn vẹn phải xử lý riêng ở Chương 4.

## 2.5.2. Sự tham gia: tùy chọn hay bắt buộc

!!! note "Định nghĩa 2.9"

    **Sự tham gia** *(participation)* cho biết một thể hiện của thực thể **có buộc phải** tham gia vào liên kết hay không.

    - **Tham gia bắt buộc** *(mandatory)*: mọi thể hiện đều phải tham gia — tương ứng `min = 1`.
    - **Tham gia tùy chọn** *(optional)*: có thể có thể hiện không tham gia — tương ứng `min = 0`.

Điểm dễ nhầm nhất — và đáng nhấn mạnh — là **hai chiều của cùng một liên kết có thể có tính tham gia khác nhau**.

!!! example "Ví dụ 2.5"

    Xét liên kết *"giáo viên phụ trách lớp"* tại Trung tâm ABC.

    - Chiều từ `LOP`: **bắt buộc**. Không thể tồn tại một lớp không có giáo viên nào phụ trách — trung tâm không mở lớp như vậy.
    - Chiều từ `GIAOVIEN`: **tùy chọn**. Một giáo viên mới tuyển, chưa được phân lớp nào, vẫn là giáo viên của trung tâm và vẫn phải có trong hệ thống.

Sự bất đối xứng này có hệ quả rất cụ thể ở Chương 3. Tham gia **bắt buộc** sẽ trở thành ràng buộc *không được rỗng* trên khóa ngoại; tham gia **tùy chọn** thì cho phép rỗng. Xác định sai một trong hai, hệ thống hoặc từ chối những dữ liệu hợp lệ, hoặc chấp nhận những dữ liệu vô nghĩa.

!!! warning "Chú ý"

    Trong đề bài, tính tham gia tùy chọn hầu như luôn được báo hiệu bằng những cụm từ như *"có thể"*, *"chưa có"*, *"không nhất thiết"*. Người học nên tập thói quen **khoanh tròn những cụm từ này ngay khi đọc đề** — chúng là thông tin thiết kế chứ không phải lời văn thừa.

## 2.5.3. Thể hiện sự tham gia trong hai ký pháp

**Trong ký pháp Chen**, tính tham gia được thể hiện bằng **số nét của cạnh nối** giữa thực thể và hình thoi liên kết: cạnh **một nét** nghĩa là tham gia **tùy chọn**, cạnh **hai nét song song** nghĩa là tham gia **bắt buộc**. Cách khác, tường minh hơn và ngày càng phổ biến, là **ghi thẳng cặp `(min, max)`** lên cạnh nối — khi đó `(0, N)` là tùy chọn còn `(1, N)` là bắt buộc. Giáo trình này dùng cách ghi cặp số vì nó không gây nhầm và đọc được ngay.

**Trong ký pháp Crow's Foot**, tính tham gia và kết nối được gộp vào **một ký hiệu duy nhất đặt ở đầu mút** của đường liên kết. Đây là điểm mạnh nhất của ký pháp này.

**Bảng 2.8. Ký hiệu đầu mút Crow's Foot — gộp kết nối và tham gia**

| Ký hiệu đầu mút | Đọc là | Nghĩa `(min, max)` |
|---|---|:--:|
| Hai gạch ngang | Đúng một, bắt buộc | `(1, 1)` |
| Vòng tròn kèm một gạch | Không quá một, tùy chọn | `(0, 1)` |
| Một gạch kèm chân quạ | Một hoặc nhiều, bắt buộc | `(1, N)` |
| Vòng tròn kèm chân quạ | Không hoặc nhiều, tùy chọn | `(0, N)` |

**Hình 2.7. Bốn ký hiệu đầu mút của ký pháp Crow's Foot**

![](../hinh-ve/Chuong-2_Mo-hinh-ER_crowsfoot.png)

Trên hình, **thực thể nằm bên phải** và đường liên kết đi tới từ bên trái. Thứ tự đặt ký hiệu tuân theo đúng quy tắc *đọc từ ngoài vào trong*: ký hiệu **xa thực thể** cho biết `min`, ký hiệu **sát thực thể** cho biết `max`.

Có một mẹo đọc rất dễ nhớ: **vòng tròn đọc là "không", gạch đọc là "một", chân quạ đọc là "nhiều"**. Ký hiệu ở đầu mút gồm hai phần — phần ngoài cùng cho biết `min`, phần trong cho biết `max`. Vậy "vòng tròn kèm chân quạ" đọc là *"không hoặc nhiều"*.

Mục 2.8.3 sẽ trình bày kỹ hơn cách đọc một lược đồ Crow's Foot hoàn chỉnh.

---


---

[← Trang trước](2-4-lien-ket-va-ky-thuat-hoi-hai-chieu.md) · [Trang sau →](2-6-bac-lien-ket-thuc-the-yeu-va-thuc-the-ket-hop.md)
