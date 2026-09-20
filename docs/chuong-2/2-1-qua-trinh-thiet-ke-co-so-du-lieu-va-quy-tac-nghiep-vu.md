# 2.1. Quá trình thiết kế cơ sở dữ liệu và quy tắc nghiệp vụ

*(1,0 tiết)*

## 2.1.1. Ba mức thiết kế

Chương 1 đã giới thiệu ba mức của mô hình dữ liệu ở mục 1.4.3. Mục này nhìn lại chúng dưới góc độ **quy trình làm việc**, vì đó chính là bản đồ cho phần còn lại của học phần.

**Thiết kế quan niệm** *(conceptual design)* trả lời câu hỏi **"nghiệp vụ có những gì?"**. Kết quả là một lược đồ ER mô tả thế giới thực, hoàn toàn độc lập với mọi công nghệ. Đây là nội dung của **Chương 2**.

**Thiết kế logic** *(logical design)* trả lời câu hỏi **"tổ chức thành bảng ra sao?"**. Kết quả là một tập các quan hệ với đầy đủ khóa chính và khóa ngoại. Đây là nội dung của **Chương 3**, và một phần của Chương 5.

**Thiết kế vật lý** *(physical design)* trả lời câu hỏi **"lưu lên đĩa thế nào?"** — chọn kiểu dữ liệu cụ thể, tạo chỉ mục, phân vùng. Phần này thuộc học phần *Hệ quản trị cơ sở dữ liệu*.

!!! warning "Chú ý"

    Trình tự ba mức phải được tôn trọng. Sai lầm phổ biến nhất của người mới học là **nhảy thẳng vào thiết kế bảng** ngay khi đọc xong đề bài, bỏ qua mức quan niệm. Hậu quả là thiết kế bám sát cách diễn đạt tình cờ của đề bài thay vì bám sát bản chất nghiệp vụ, và khi nghiệp vụ thay đổi một chút thì toàn bộ thiết kế phải làm lại.

## 2.1.2. Quy tắc nghiệp vụ — nguyên liệu đầu vào

Thiết kế quan niệm cần nguyên liệu, và nguyên liệu ấy là quy tắc nghiệp vụ.

!!! note "Định nghĩa 2.1"

    **Quy tắc nghiệp vụ** *(business rule)* là một **phát biểu ngắn gọn, rõ ràng, bằng ngôn ngữ tự nhiên**, mô tả một chính sách, một quy trình hoặc một ràng buộc trong hoạt động của tổ chức.

![](../hinh-ve/slide/internet/bang_noi_quy.jpg){width=55%}

*Ảnh minh họa: bảng nội quy học sinh treo ở một trường học. Mỗi dòng là một phát biểu ngắn, rõ, về việc được làm và không được làm — đúng nghĩa một tập quy tắc nghiệp vụ — Nguồn: Wikimedia Commons · Danhviet1493 · CC BY-SA 4.0.*

Quy tắc nghiệp vụ không do người thiết kế nghĩ ra. Chúng được **thu thập** từ ba nguồn: phỏng vấn người sử dụng hệ thống, đọc tài liệu và biểu mẫu hiện hành, và quan sát quy trình làm việc thực tế. Đây là công việc của con người với con người, không phải công việc kỹ thuật — nhưng chất lượng của toàn bộ thiết kế phụ thuộc vào nó.

Vai trò của quy tắc nghiệp vụ đối với người thiết kế có ba mặt. Thứ nhất, chúng **xác định phạm vi**: cái gì cần lưu, cái gì không. Thứ hai, chúng **quyết định cấu trúc**: mỗi quy tắc thường ứng với một thành phần cụ thể của lược đồ ER. Thứ ba, chúng là **căn cứ để tranh luận**: khi hai người thiết kế bất đồng, cách giải quyết không phải là ai lớn tiếng hơn mà là quay lại đọc quy tắc nghiệp vụ.

## 2.1.3. Thế nào là một quy tắc nghiệp vụ tốt

Không phải phát biểu nào của khách hàng cũng dùng được. Một quy tắc nghiệp vụ tốt phải **đếm được** — nghĩa là từ nó, người thiết kế rút ra được một con số hoặc một quyết định dứt khoát.

!!! example "Ví dụ 2.1"

    Xét ba phát biểu sau về Trung tâm ABC.

    **(a)** *"Chúng tôi quản lý học viên rất chặt chẽ."* — Đây **không phải** quy tắc nghiệp vụ. Nó không cho biết cần lưu gì, cũng không cho biết ràng buộc nào. Người thiết kế không rút ra được điều gì.

    **(b)** *"Học viên có thể học nhiều lớp."* — Đây là một quy tắc **chấp nhận được nhưng chưa đủ**. Nó cho biết một chiều của liên kết, còn thiếu chiều kia.

    **(c)** *"Một học viên có thể ghi danh nhiều lớp; một lớp có nhiều học viên; mỗi lượt ghi danh được ghi nhận ngày ghi danh và mức học phí."* — Đây là một quy tắc **tốt**. Từ nó, người thiết kế rút ra ngay: liên kết là **nhiều–nhiều**, và liên kết ấy **có thuộc tính riêng**.

Ba đặc điểm của một quy tắc nghiệp vụ tốt có thể tóm lại như sau. Nó **nói về một sự việc cụ thể** chứ không phải một cảm nhận chung. Nó **dùng các từ chỉ số lượng** — một, nhiều, không quá, ít nhất — để người đọc đếm được. Và nó **nêu cả hai chiều** khi mô tả mối liên hệ giữa hai sự vật.

!!! warning "Chú ý"

    Khi khách hàng phát biểu mơ hồ, nhiệm vụ của người thiết kế **không phải** là tự đoán mà là **hỏi lại cho rõ**. Câu hỏi hữu ích nhất luôn có dạng *"Một X thì liên quan tới bao nhiêu Y?"* — và phải hỏi cả chiều ngược lại. Kỹ thuật này được trình bày ở mục 2.4.2.

## 2.1.4. Lược đồ ER — sản phẩm của thiết kế quan niệm

Mục 2.1.1 đã nói rằng thiết kế quan niệm cho ra một **lược đồ ER**, nhưng chưa nói lược đồ ấy trông như thế nào. Cần bổ khuyết điều đó ngay bây giờ, vì lý do rất giản dị: người thợ chỉ đọc được bản vẽ khi đã hình dung được ngôi nhà hoàn thiện. Mục này đưa ra **cái nhìn toàn cảnh** — vừa đủ để đọc một lược đồ nhỏ và để hiểu các mục sau đang bàn về cái gì. Chi tiết của từng thành phần sẽ được trình bày lần lượt từ mục 2.2 đến mục 2.7.

!!! note "Định nghĩa 2.2"

    **Mô hình thực thể – liên kết** *(Entity–Relationship model, ER)* là một mô hình dữ liệu ở **mức quan niệm**, mô tả thế giới thực bằng **ba loại thành phần**: **thực thể**, **thuộc tính** và **liên kết**. Bản vẽ biểu diễn mô hình ấy được gọi là **lược đồ ER** *(Entity–Relationship Diagram, ERD)*.

Ba thành phần ấy không phải là phát minh kỹ thuật xa lạ. Chúng ứng với ba câu hỏi rất đời thường mà bất kỳ ai cũng đặt ra khi tìm hiểu một tổ chức.

**Thực thể** trả lời câu hỏi **"ở đây có những sự vật nào?"** — học viên, lớp học, giáo viên. Trên lược đồ, mỗi thực thể là một **hình chữ nhật**.

**Thuộc tính** trả lời câu hỏi **"mỗi sự vật ấy cần biết những gì?"** — học viên thì cần biết mã, họ tên, ngày sinh. Trên lược đồ, mỗi thuộc tính là một **hình oval** nối vào thực thể của nó bằng một đoạn thẳng.

**Liên kết** trả lời câu hỏi **"các sự vật ấy quan hệ với nhau ra sao?"** — giáo viên phụ trách lớp. Trên lược đồ, mỗi liên kết là một **hình thoi** đặt giữa hai thực thể, và **con số ghi trên cạnh nối** cho biết một bên đi với bao nhiêu bên kia.

Hình 2.1 là một lược đồ ER hoàn chỉnh — nhỏ nhất có thể, nhưng đã đủ cả ba thành phần.

**Hình 2.1. Một lược đồ ER nhỏ — ba thành phần cơ bản**

```mermaid
flowchart LR
    K1(["<u>MAGV</u>"]) --- GV["GIAOVIEN"]
    A1(["HOTEN"]) --- GV
    A2(["BANGCAP"]) --- GV
    GV ---|"1"| R{"phụ trách"}
    R ---|"M"| L["LOP"]
    L --- K2(["<u>MALOP</u>"])
    L --- A3(["TENLOP"])
    style GV fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style L fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style R fill:#E2F0D9,stroke:#548235
    style K1 fill:#fff,stroke:#1F4E79
    style K2 fill:#fff,stroke:#1F4E79
    style A1 fill:#fff,stroke:#1F4E79
    style A2 fill:#fff,stroke:#1F4E79
    style A3 fill:#fff,stroke:#1F4E79
```

Điều đáng chú ý nhất ở hình trên là nó **đọc thành lời được**, và câu đọc ra là một câu tiếng Việt bình thường: *"Mỗi giáo viên — có mã giáo viên, họ tên, bằng cấp — phụ trách nhiều lớp; mỗi lớp — có mã lớp, tên lớp — do đúng một giáo viên phụ trách."* Chính đặc điểm này làm nên giá trị của mô hình ER. Chủ trung tâm ABC không biết gì về cơ sở dữ liệu vẫn đọc được lược đồ và có thể nói ngay: *"chỗ này chưa đúng, một lớp bên tôi đôi khi có hai giáo viên dạy chung"*. Một sai sót được phát hiện ở giai đoạn này chỉ tốn công sửa một nét vẽ; cũng sai sót ấy nếu để lọt tới lúc hệ thống đã chạy thì tốn kém gấp bội.

!!! warning "Chú ý"

    Lược đồ ER **không phải** bản thiết kế bảng. Trong Hình 2.1 không có dòng dữ liệu nào, không có kiểu dữ liệu, không có khóa ngoại — vì đây là bản mô tả **thế giới thực**, chưa phải bản mô tả **cách lưu trữ**. Việc biến lược đồ ER thành các bảng cụ thể là công việc của Chương 3.

Ba thành phần trên mới là bộ khung. Trên bộ khung ấy, mô hình ER còn bổ sung một số sắc thái mà chương này sẽ lần lượt trình bày: thuộc tính nào đóng vai trò **thuộc tính khóa** để phân biệt các cá thể *(mục 2.3)*; một liên kết có **kết nối** và **sự tham gia** ra sao *(mục 2.5)*; và ba trường hợp đặc biệt — liên kết đệ quy, thực thể yếu, liên kết nhiều–nhiều *(mục 2.6)*. Bộ ký hiệu đầy đủ được tổng hợp thành bảng tra ở **mục 2.2.2**.

## 2.1.5. Từ quy tắc nghiệp vụ sang thành phần của mô hình ER

Đã có nguyên liệu *(quy tắc nghiệp vụ, mục 2.1.2)* và đã biết sản phẩm cần làm ra trông như thế nào *(lược đồ ER, mục 2.1.4)*, còn lại là câu hỏi nối hai đầu ấy: **đọc một câu quy tắc nghiệp vụ thì rút ra được thành phần nào của lược đồ?**

![](../hinh-ve/slide/internet/ban_ve_kien_truc.jpg){width=70%}

*Ảnh minh họa: mô hình mặt bằng một căn hộ. Người thiết kế cơ sở dữ liệu cũng làm việc như kiến trúc sư: thống nhất ý tưởng với chủ nhà (quy tắc nghiệp vụ) trước, rồi mới vẽ bản vẽ (lược đồ ER), sau cùng mới thi công (tạo bảng) — Nguồn: Wikimedia Commons · Tallbox · CC BY-SA 4.0.*

Có một quy luật rất tiện dụng: **loại từ trong câu quy tắc nghiệp vụ gợi ý loại thành phần trong lược đồ ER**. Quy luật này không phải là công thức máy móc, nhưng nó cho người thiết kế một điểm khởi đầu vững chắc.

**Bảng 2.1. Phiên dịch quy tắc nghiệp vụ sang thành phần ER**

| Trong câu quy tắc nghiệp vụ | Thường tương ứng với | Ví dụ tại Trung tâm ABC |
|---|---|---|
| **Danh từ** chỉ sự vật cần lưu thông tin | **Thực thể** *(mục 2.2)* | *"trung tâm có nhiều **giáo viên**"* → thực thể `GIAOVIEN` |
| **Danh từ** chỉ đặc điểm của một sự vật | **Thuộc tính** *(mục 2.2)* | *"mỗi giáo viên có **họ tên**, **bằng cấp**"* |
| **Động từ** nối hai danh từ | **Liên kết** *(mục 2.4)* | *"mỗi lớp **do** một giáo viên **phụ trách**"* |
| Từ chỉ **số lượng**: một, nhiều | **Kết nối** *(1:1, 1:M, M:N — mục 2.5)* | *"một giáo viên phụ trách **nhiều** lớp"* |
| Cụm **"có thể"**, **"chưa có"** | **Tham gia tùy chọn** *(mục 2.5)* | *"giáo viên **có thể chưa** phụ trách lớp nào"* |
| Cụm **"bắt buộc"**, **"phải"** | **Tham gia bắt buộc** *(mục 2.5)* | *"mỗi lớp **phải** thuộc một khóa học"* |
| **Nhiều giá trị** cho cùng một đặc điểm | **Thuộc tính đa trị** → phải tách *(mục 2.2.4)* | *"học viên có **nhiều số điện thoại**"* |

Để thấy bảng trên vận hành ra sao, hãy áp nó vào quy tắc **(c)** của Ví dụ 2.1 — quy tắc "tốt" duy nhất trong ba phát biểu. Mỗi cụm từ trong câu rơi đúng vào một dòng của bảng, và mỗi dòng cho ra một mảnh lược đồ.

**Hình 2.2. Áp Bảng 2.1 vào quy tắc (c) của Ví dụ 2.1 — từ câu chữ tới mảnh lược đồ**

```mermaid
flowchart LR
    T1["<b>danh từ</b><br/>học viên, lớp"]
    T2["<b>động từ</b><br/>ghi danh"]
    T3["<b>số lượng</b><br/>nhiều lớp · nhiều học viên"]
    T4["<b>đặc điểm của lượt ghi danh</b><br/>ngày ghi danh, học phí"]
    HV["HOCVIEN"] ---|"M"| R{"ghi danh"}
    R ---|"N"| LOP["LOP"]
    R --- A1(["NGAYGHIDANH"])
    R --- A2(["HOCPHI"])
    T1 -.-> HV
    T1 -.-> LOP
    T2 -.-> R
    T3 -.-> R
    T4 -.-> A1
    T4 -.-> A2
    style HV fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style LOP fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
    style R fill:#FFD9D9,stroke:#C00000,stroke-width:2px
    style A1 fill:#fff,stroke:#1F4E79
    style A2 fill:#fff,stroke:#1F4E79
    style T1 fill:#FFF2CC,stroke:#BF9000
    style T2 fill:#FFF2CC,stroke:#BF9000
    style T3 fill:#FFF2CC,stroke:#BF9000
    style T4 fill:#FFF2CC,stroke:#BF9000
```

Đọc hình từ trái sang phải. Hai danh từ *học viên*, *lớp* thành hai **hình chữ nhật**; động từ *ghi danh* thành **hình thoi** nối chúng; hai chữ *nhiều* thành hai chữ cái `M`, `N` ở hai đầu — tức liên kết nhiều–nhiều; và hai đặc điểm *ngày ghi danh*, *học phí* thành hai **oval treo trên hình thoi**, vì chúng không thuộc riêng học viên hay lớp mà thuộc về *lượt ghi danh*. Hình thoi được tô đỏ để đánh dấu một việc còn phải làm: liên kết nhiều–nhiều có thuộc tính riêng sẽ được xử lý ở mục 2.6.4. Ở đây người học chưa cần hiểu vì sao — chỉ cần thấy rằng **một câu quy tắc tốt tự nó đã vẽ ra được lược đồ**.

Cột giữa có ghi kèm số mục, vì ở đây người học mới chỉ cần **nhận ra tên gọi** của từng thành phần chứ chưa cần nắm hết sắc thái của nó; mỗi thành phần sẽ được học kỹ ở mục tương ứng. Bảng này vì vậy nên được xem như một **bảng tra dùng lại nhiều lần**: mục 2.9 sẽ quay lại dùng đúng nó để giải trọn vẹn bài toán Trung tâm ABC.

Cần nhấn mạnh rằng bảng trên là **gợi ý chứ không phải quy tắc tuyệt đối**. Không phải danh từ nào cũng thành thực thể — nếu một danh từ chỉ có duy nhất một đặc điểm và không liên kết với gì khác, nó thường chỉ nên là thuộc tính. Mục 2.2.1 sẽ đưa ra tiêu chí phân biệt.

---


---

[← Trang trước](index.md) · [Trang sau →](2-2-thuc-the-va-thuoc-tinh.md)
