# 2.6. Bậc liên kết, thực thể yếu và thực thể kết hợp

*(1,5 tiết)*

## 2.6.1. Bậc của liên kết

!!! note "Định nghĩa 2.10"

    **Bậc** *(degree)* của một liên kết là **số thực thể tham gia** vào liên kết đó.

Liên kết **bậc hai** *(binary)* nối hai thực thể khác nhau và chiếm áp đảo trong thực tế. Liên kết **bậc một** *(unary)* nối một thực thể với chính nó — gọi là liên kết đệ quy, trình bày ở mục sau. Liên kết **bậc ba** *(ternary)* nối ba thực thể cùng lúc; loại này hiếm và thường nên tách thành các liên kết bậc hai để dễ xử lý.

## 2.6.2. Liên kết đệ quy

!!! note "Định nghĩa 2.11"

    **Liên kết đệ quy** *(recursive relationship)* là liên kết mà **một thực thể liên hệ với chính nó**.

Loại liên kết này thường gây bối rối lúc đầu, nhưng nó xuất hiện rất nhiều trong đời sống.

**Hình 2.8. Ba ví dụ liên kết đệ quy, vẽ theo ký pháp Chen**

```mermaid
flowchart LR
    NV["NHANVIEN"] ---|"1"| R1{"quản lý"}
    R1 ---|"M"| NV
    KH["KHOAHOC"] ---|"M"| R2{"là tiên quyết của"}
    R2 ---|"N"| KH
    SP["SANPHAM"] ---|"M"| R3{"gồm linh kiện"}
    R3 ---|"N"| SP
    R1 ~~~ KH
    R2 ~~~ SP
    style NV fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style KH fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style SP fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style R1 fill:#E2F0D9,stroke:#548235
    style R2 fill:#FFD9D9,stroke:#C00000,stroke-width:2px
    style R3 fill:#FFD9D9,stroke:#C00000,stroke-width:2px
```

Điểm đáng chú ý về mặt ký pháp: liên kết đệ quy vẽ theo Chen **không có gì đặc biệt** — vẫn là một hình thoi, chỉ khác ở chỗ **cả hai cạnh của nó cùng nối về một hình chữ nhật**. Đây lại là một ưu điểm nữa của Chen: người học không phải nhớ thêm ký hiệu mới nào cho trường hợp này.

Ví dụ thứ nhất là **quan hệ quản lý**: một nhân viên quản lý nhiều nhân viên khác, và mỗi nhân viên có một người quản lý. Đây là đệ quy 1:M.

Ví dụ thứ hai là **khóa học tiên quyết** — chính là quy tắc thứ bảy trong bài toán Trung tâm ABC. Một khóa học có thể là tiên quyết của nhiều khóa khác, và một khóa có thể đòi hỏi nhiều khóa tiên quyết. Đây là đệ quy M:N.

Ví dụ thứ ba là **cấu thành sản phẩm**: một sản phẩm gồm nhiều linh kiện, mà mỗi linh kiện cũng có thể là một sản phẩm được lắp từ các linh kiện nhỏ hơn.

!!! warning "Chú ý"

    Liên kết đệ quy **M:N phải tách** giống hệt liên kết M:N thông thường. Điểm khác biệt duy nhất là bảng sinh ra sẽ có **hai cột cùng tham chiếu về một bảng**, nên phải đặt tên hai cột khác nhau để phân biệt vai trò — chẳng hạn `TIENQUYET(MAKH_truoc, MAKH_sau)`. Quên đặt tên phân biệt là lỗi rất hay gặp.

## 2.6.3. Thực thể mạnh và thực thể yếu

!!! note "Định nghĩa 2.12"

    **Thực thể yếu** *(weak entity)* là thực thể thỏa mãn **đồng thời hai điều kiện**:

    1. **Phụ thuộc tồn tại**: nó không thể tồn tại nếu thực thể chủ không tồn tại.
    2. **Thuộc tính khóa không đầy đủ**: nó phải mượn thuộc tính khóa của thực thể chủ mới đủ phân biệt.

    Thực thể không thỏa mãn cả hai điều kiện gọi là **thực thể mạnh** *(strong entity)*.

Phải nhấn mạnh chữ **đồng thời**. Rất nhiều thực thể phụ thuộc tồn tại vào thực thể khác nhưng vẫn có thuộc tính khóa riêng đầy đủ, và những thực thể đó **không phải** là thực thể yếu.

!!! example "Ví dụ 2.6"

    Thực thể `DIENTHOAI` của Trung tâm ABC là thực thể **yếu**. Điều kiện thứ nhất thỏa mãn: một số điện thoại chỉ tồn tại trong hệ thống khi gắn với một học viên; xóa học viên thì số điện thoại của họ cũng không còn ý nghĩa. Điều kiện thứ hai cũng thỏa mãn: bản thân số điện thoại không đủ làm thuộc tính khóa nếu ta cho phép hai học viên dùng chung một số máy bàn gia đình, nên thuộc tính khóa phải là cặp `(MAHV, SODT)`.

    Ngược lại, thực thể `LOP` **không phải** là thực thể yếu, dù mỗi lớp đều phải thuộc một khóa học. Lý do: `MALOP` tự nó đã đủ phân biệt mọi lớp, không cần mượn `MAKH`. Đây chỉ là phụ thuộc tồn tại chứ không phải thực thể yếu.

Trong ký pháp Chen, thực thể yếu và liên kết dẫn tới nó đều được vẽ bằng **hai đường viền** — một quy ước rất hợp lý, vì hai đặc điểm ấy luôn đi cùng nhau.

**Hình 2.9. Thực thể yếu trong ký pháp Chen — trường hợp `DIENTHOAI`**

```mermaid
flowchart LR
    K(["<u>MAHV</u>"]) --- HV["HOCVIEN"]
    HV ---|"1"| R{"có"}
    R ---|"M"| DT[["DIENTHOAI"]]
    DT --- K2(["<u>SODT</u>"])
    DT --- K3(["LOAI"])
    style HV fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style DT fill:#FFF2CC,stroke:#C00000,stroke-width:3px
    style R fill:#E2F0D9,stroke:#548235,stroke-width:3px
    style K fill:#fff,stroke:#1F4E79
    style K2 fill:#fff,stroke:#1F4E79
    style K3 fill:#fff,stroke:#1F4E79
```

Hình trên đọc như sau. `DIENTHOAI` vẽ **chữ nhật hai viền** vì nó là thực thể yếu. Liên kết *"có"* vẽ **hình thoi hai viền** vì đây là **liên kết định danh** *(identifying relationship)* — chính nó cung cấp phần khóa còn thiếu. Bên trong `DIENTHOAI`, thuộc tính `SODT` được gạch chân, nhưng **nó chỉ là một nửa của thuộc tính khóa**; nửa còn lại là `MAHV` mượn từ `HOCVIEN` qua liên kết định danh. Ghép lại mới đủ phân biệt.

**Bảng 2.9. Cùng một sự vật, hai cách đặt thuộc tính khóa cho hai kết luận khác nhau**

| Tình huống | Thuộc tính khóa | Có phải thực thể yếu? |
|---|---|---|
| Mỗi số điện thoại chỉ thuộc đúng một học viên và không trùng lặp trong toàn hệ thống | `SODT` — đủ duy nhất một mình | **Không** — chỉ phụ thuộc tồn tại |
| Hai học viên trong cùng gia đình khai chung một số máy bàn | `(MAHV, SODT)` — phải mượn khóa của thực thể chủ | **Có** — thực thể yếu |

Ví dụ này minh họa một điều quan trọng về nghề thiết kế: **cùng một sự vật ngoài đời có thể cho hai mô hình khác nhau, tùy vào quy tắc nghiệp vụ**. Không có đáp án đúng tuyệt đối tách rời khỏi ngữ cảnh — và đó chính là lý do quy tắc nghiệp vụ ở mục 2.1 phải được thu thập cho thật rõ ràng.

## 2.6.4. Thực thể kết hợp — vì sao liên kết M:N bắt buộc phải tách

Đây là nội dung quan trọng nhất của mục 2.6, và là chỗ mà thiết kế của người mới học hay đổ vỡ.

Xét quy tắc thứ năm của Trung tâm ABC: *"Một học viên ghi danh nhiều lớp; một lớp có nhiều học viên. Mỗi lượt ghi danh ghi nhận ngày ghi danh và học phí."*

Câu hỏi đặt ra rất cụ thể: **thuộc tính `HOCPHI` thuộc về thực thể nào?**

**Hình 2.10. Liên kết M:N ẩn chứa một thực thể**

```mermaid
flowchart LR
    Q["<b>HOCPHI<br/>thuộc về đâu?</b>"]
    Q --> A1["Không thuộc <b>HỌC VIÊN</b><br/><i>mỗi học viên đóng nhiều mức<br/>khác nhau cho các lớp khác nhau</i>"]
    Q --> A2["Không thuộc <b>LỚP</b><br/><i>mỗi lớp thu nhiều mức khác nhau<br/>tùy học viên có ưu đãi hay không</i>"]
    A1 --> R["Nó thuộc về<br/><b>LƯỢT GHI DANH</b><br/>─────────<br/>GHIDANH(<u>MAHV</u>, <u>MALOP</u>,<br/>NGAYGHIDANH, HOCPHI)"]
    A2 --> R
    R --> T["<b>Phép thử 'tờ phiếu'</b><br/>Mỗi lần ghi danh, trung tâm<br/>in ra một tờ phiếu.<br/>Tờ phiếu ấy có thật<br/>→ nó là một thực thể"]
    style Q fill:#FFF2CC,stroke:#C00000
    style R fill:#1F4E79,color:#fff,stroke:#1F4E79,stroke-width:2px
    style T fill:#E2F0D9,stroke:#548235
```

Thuộc tính `HOCPHI` **không thuộc về học viên**, vì cùng một học viên có thể đóng các mức khác nhau cho các lớp khác nhau. Nó cũng **không thuộc về lớp**, vì cùng một lớp có thể thu các mức khác nhau tùy học viên có được ưu đãi hay không. Nó chỉ có nghĩa khi gắn với **một cặp cụ thể** *(học viên này, lớp này)*.

Điều đó cho thấy giữa hai thực thể đang tồn tại một **sự vật thứ ba mà ta chưa đặt tên**: bản thân *lượt ghi danh*. Khi được đặt tên và cấp thuộc tính khóa, nó trở thành một thực thể đầy đủ.

!!! note "Định nghĩa 2.13"

    **Thực thể kết hợp** *(associative entity / bridge entity)* là thực thể sinh ra từ việc **tách một liên kết nhiều–nhiều**. Thuộc tính khóa của nó là **khóa phức hợp** ghép từ thuộc tính khóa của hai thực thể gốc, và nó có thể mang **thuộc tính riêng**.

Sau khi tách, liên kết M:N ban đầu được thay bằng **hai liên kết 1:M**: `HOCVIEN` một–nhiều `GHIDANH`, và `LOP` một–nhiều `GHIDANH`.

Một mẹo nhận biết rất hiệu quả là **phép thử tờ phiếu**: hãy tự hỏi *"mỗi lần sự việc này xảy ra, tổ chức có in ra hay ghi lại một tờ giấy nào không?"* Nếu có — phiếu ghi danh, hóa đơn, phiếu mượn sách, vé xe — thì tờ giấy ấy chính là một thực thể có thật, và các thông tin ghi trên đó chính là thuộc tính của nó.

!!! warning "Chú ý"

    Cần phân biệt hai tình huống. Nếu liên kết M:N **có thuộc tính riêng** như trường hợp `GHIDANH`, thì việc tách là hiển nhiên. Nhưng ngay cả khi liên kết M:N **không có thuộc tính nào**, ta **vẫn phải tách** ở bước chuyển sang mô hình quan hệ — vì mô hình quan hệ không có cách nào biểu diễn trực tiếp một liên kết nhiều–nhiều. Điều này sẽ được chứng minh ở Chương 3.

---


---

[← Trang trước](2-5-ket-noi-luc-luong-va-su-tham-gia.md) · [Trang sau →](2-7-mo-hinh-er-mo-rong-eer.md)
