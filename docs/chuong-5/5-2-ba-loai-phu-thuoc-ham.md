# 5.2. Ba loại phụ thuộc hàm

*(1,0 tiết)*

## 5.2.1. Nhắc lại và mở rộng

Mục 3.2.2 đã định nghĩa phụ thuộc hàm `X → Y`: *biết `X` thì biết chắc `Y`*. Ở Chương 3 khái niệm này chỉ dùng để định nghĩa khóa. Từ đây nó trở thành **công cụ phân tích chính**.

Cần nhắc lại một cảnh báo đã nêu ở Chương 3, vì nó là nguồn sai lầm phổ biến nhất của cả chương này:

!!! warning "Chú ý"

    Tập phụ thuộc hàm `F` đến từ **quy tắc nghiệp vụ**, **không phải** từ việc nhìn dữ liệu mẫu. Nếu bảng hiện có 3 dòng và tình cờ không ai trùng tên, ta **không được** kết luận `HOTEN → MAHV`. Câu hỏi đúng luôn là: *"nghiệp vụ có cho phép hai học viên trùng tên không?"* Toàn bộ chương này đứng trên `F`; `F` sai thì mọi kết quả sau đó đều sai.

**Bảng 5.3. Ba loại phụ thuộc hàm**

| Loại | Định nghĩa ngắn | Có hại không |
|---|---|---|
| **Đầy đủ** *(full)* | `X → Y` mà **không tập con thực sự nào** của `X` xác định được `Y` | Không — đây là dạng mong muốn |
| **Bộ phận** *(partial)* | `Y` phụ thuộc vào **một phần** của khóa phức hợp | **Có** — vi phạm 2NF |
| **Bắc cầu** *(transitive)* | `K → Z → Y`, trong đó `Z` **không phải khóa** | **Có** — vi phạm 3NF |

Hai loại sau là **hai thủ phạm** gây ra dị thường, và toàn bộ việc chuẩn hóa lên 3NF chính là **diệt lần lượt hai thủ phạm này**.

## 5.2.2. Phụ thuộc hàm đầy đủ

!!! note "Định nghĩa 5.2"

    Phụ thuộc hàm `X → Y` là **đầy đủ** nếu với mọi tập con thực sự `X' ⊂ X`, ta **không có** `X' → Y`.

    **Ví dụ 5.1.** Trong bảng `GHIDANH(MAHV, MALOP, HOCPHI)` với khóa `(MAHV, MALOP)`:

    - `(MAHV, MALOP) → HOCPHI` là **đầy đủ**: biết riêng học viên không đủ suy ra học phí *(mỗi học viên đóng nhiều mức cho nhiều lớp)*, biết riêng lớp cũng không đủ *(mỗi lớp thu nhiều mức tùy ưu đãi)*.

## 5.2.3. Phụ thuộc bộ phận

!!! note "Định nghĩa 5.3"

    Phụ thuộc hàm `X → Y` là **bộ phận** nếu tồn tại tập con thực sự `X' ⊂ X` sao cho `X' → Y`. Nói cách khác: `Y` chỉ cần **một phần** của `X` là đã xác định được.

Loại này chỉ xuất hiện khi khóa là **khóa phức hợp** — vì phải có "phần" thì mới có "một phần".

**Hình 5.2. Phụ thuộc bộ phận — phép loại suy ổ khóa hai chìa**

```mermaid
flowchart LR
    K["<b>KHÓA PHỨC HỢP</b><br/>(MAHV, MALOP)<br/><i>ổ khóa cần HAI chìa</i>"]
    K --> OK["<b>HOCPHI</b><br/>cần <b>CẢ HAI</b> chìa<br/>→ phụ thuộc <b>ĐẦY ĐỦ</b>"]
    K --> BAD1["<b>HOTEN</b><br/>chỉ cần chìa <b>MAHV</b><br/>→ phụ thuộc <b>BỘ PHẬN</b>"]
    K --> BAD2["<b>TENLOP</b><br/>chỉ cần chìa <b>MALOP</b><br/>→ phụ thuộc <b>BỘ PHẬN</b>"]
    style K fill:#1F4E79,color:#fff,stroke:#1F4E79,stroke-width:2px
    style OK fill:#E2F0D9,stroke:#548235
    style BAD1 fill:#FFD9D9,stroke:#C00000
    style BAD2 fill:#FFD9D9,stroke:#C00000
```

Vì sao phụ thuộc bộ phận gây hại? Vì nó **buộc dữ liệu phải lặp lại**. Nếu `HOTEN` chỉ phụ thuộc vào `MAHV` nhưng lại nằm trong bảng có khóa `(MAHV, MALOP)`, thì học viên ghi danh bao nhiêu lớp, tên của người đó **lặp lại bấy nhiêu lần** — đúng gốc rễ dư thừa của mục 1.3.

## 5.2.4. Phụ thuộc bắc cầu

!!! note "Định nghĩa 5.4"

    Phụ thuộc hàm là **bắc cầu** nếu tồn tại chuỗi `K → Z → Y`, trong đó `K` là khóa, `Z` **không phải khóa và không phải tập con của khóa**, còn `Y` là thuộc tính không khóa.

**Hình 5.3. Phụ thuộc bắc cầu — phải đi hai chặng**

```mermaid
flowchart LR
    K["<b>MALOP</b><br/><i>khóa</i>"] -->|"chặng 1"| Z["<b>MAGV</b><br/><i>KHÔNG phải khóa</i>"]
    Z -->|"chặng 2"| Y["<b>HOTEN_GV</b><br/><i>thuộc tính không khóa</i>"]
    K -.->|"phụ thuộc BẮC CẦU<br/>= đi vòng qua Z"| Y
    style K fill:#1F4E79,color:#fff,stroke:#1F4E79,stroke-width:2px
    style Z fill:#FFD9D9,stroke:#C00000,stroke-width:2px
    style Y fill:#FFF2CC,stroke:#C00000
```

Vì sao bắc cầu gây hại? Cũng vì lặp lại, nhưng theo cơ chế khác. Nếu `HOTEN_GV` nằm trong bảng `LOP`, thì một giáo viên phụ trách bao nhiêu lớp, tên của người ấy **lặp lại bấy nhiêu lần**. Đây chính xác là tình huống cô Lê Hoa lặp ba lần ở Bảng 1.5 của Chương 1 — nay đã có tên gọi.

!!! warning "Chú ý — điều kiện `Z` không phải khóa là bắt buộc"

    Nếu `Z` cũng là một khóa dự tuyển thì chuỗi `K → Z → Y` **không phải** phụ thuộc bắc cầu có hại, vì lúc ấy `Z` xác định duy nhất mỗi dòng nên không gây lặp. Bỏ sót điều kiện này dẫn tới việc tách bảng không cần thiết.

---


---

[← Trang trước](5-1-the-nao-la-mot-co-so-du-lieu-tot.md) · [Trang sau →](5-3-he-luat-dan-armstrong.md)
