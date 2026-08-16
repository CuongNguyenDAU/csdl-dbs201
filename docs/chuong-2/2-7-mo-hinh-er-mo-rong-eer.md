# 2.7. Mô hình ER mở rộng (EER)

*(1,0 tiết)*

## 2.7.1. Vì sao cần mở rộng mô hình ER

Mô hình ER cơ bản trình bày ở các mục trên đã đủ dùng cho phần lớn bài toán. Nhưng có một tình huống mà nó xử lý rất vụng về, và tình huống ấy lại xuất hiện thường xuyên: khi **nhiều loại sự vật vừa giống nhau vừa khác nhau**.

!!! example "Ví dụ 2.7"

    Trung tâm ABC muốn quản lý toàn bộ **nhân sự** — bao gồm giáo viên và nhân viên hành chính. Cả hai nhóm đều có mã nhân sự, họ tên, ngày sinh, số điện thoại, ngày vào làm. Nhưng riêng giáo viên còn có bằng cấp và chứng chỉ tiếng Anh; riêng nhân viên hành chính có bộ phận công tác và ca làm việc.

Với mô hình ER cơ bản, người thiết kế chỉ có hai lựa chọn, và **cả hai đều tồi**.

Lựa chọn thứ nhất là **tạo hai thực thể riêng biệt** `GIAOVIEN` và `NHANVIEN_HANHCHINH`. Khi ấy năm thuộc tính chung phải khai báo **hai lần**. Đó chính là dư thừa — lần này không phải dư thừa dữ liệu mà là **dư thừa ở mức cấu trúc**. Hậu quả rất thực tế: khi trung tâm muốn bổ sung trường "email công vụ" cho mọi nhân sự, phải sửa ở hai chỗ; quên một chỗ là hai nhóm nhân sự có cấu trúc lệch nhau.

Lựa chọn thứ hai là **gộp tất cả vào một thực thể** `NHANSU` với đầy đủ mọi thuộc tính. Khi ấy mọi giáo viên đều có ô "bộ phận công tác" bỏ trống, và mọi nhân viên hành chính đều có ô "bằng cấp" bỏ trống. Bảng dữ liệu đầy ô rỗng, và tệ hơn, hệ thống **không thể ngăn** việc điền nhầm bộ phận công tác cho một giáo viên.

**Mô hình ER mở rộng** *(Extended Entity–Relationship — EER)* bổ sung đúng những khái niệm cần thiết để thoát khỏi thế lưỡng nan này.

## 2.7.2. Thực thể cha và thực thể con

!!! note "Định nghĩa 2.14"

    **Thực thể cha** *(supertype)* là thực thể chứa các **thuộc tính chung** cho một nhóm sự vật. **Thực thể con** *(subtype)* là thực thể chứa các **thuộc tính riêng** của một tập hợp con cụ thể trong nhóm đó.

    Quan hệ giữa chúng gọi là **quan hệ cha–con** hay **quan hệ IS-A** — đọc là *"một thực thể con LÀ MỘT thực thể cha"*.

**Hình 2.11. Phân cấp chuyên biệt hóa tại Trung tâm ABC**

```mermaid
flowchart TB
    NS["<b>NHANSU</b> — THỰC THỂ CHA<br/>─────────<br/>MANS <i>(khóa)</i><br/>HOTEN · NGAYSINH<br/>SDT · NGAYVAOLAM<br/><i>thuộc tính DÙNG CHUNG</i>"]
    NS --> D{"chuyên biệt hóa theo<br/><b>VAI TRÒ CÔNG VIỆC</b>"}
    D --> GV["<b>GIAOVIEN</b> — thực thể con<br/>─────────<br/>MANS <i>(khóa, dùng chung với cha)</i><br/>BANGCAP<br/>CHUNGCHI_TIENGANH"]
    D --> HC["<b>NHANVIEN_HANHCHINH</b> — thực thể con<br/>─────────<br/>MANS <i>(khóa, dùng chung với cha)</i><br/>BOPHAN<br/>CA_LAMVIEC"]
    style NS fill:#1F4E79,color:#fff,stroke:#1F4E79,stroke-width:2px
    style D fill:#FFF2CC,stroke:#C00000
    style GV fill:#D9E2F3,stroke:#1F4E79
    style HC fill:#D9E2F3,stroke:#1F4E79
```

Cách đọc sơ đồ trên: *"Một giáo viên **là một** nhân sự"* và *"một nhân viên hành chính **là một** nhân sự"*. Phép thử để kiểm tra xem có đúng là quan hệ cha–con hay không chính là câu **"LÀ MỘT"**: nếu đặt vào câu ấy mà nghe xuôi thì đúng, còn nếu phải nói *"có một"* thì đó là liên kết thông thường chứ không phải cha–con.

!!! warning "Chú ý"

    Đây là chỗ nhầm lẫn phổ biến nhất khi học EER. *"Lớp **có** nhiều học viên"* — dùng động từ **có**, nên đó là **liên kết** bình thường. *"Giáo viên **là một** nhân sự"* — dùng **là một**, nên đó là **quan hệ cha–con**. Người học nên đọc thành tiếng câu tiếng Việt trước khi vẽ.

Trong ký pháp chuẩn, quan hệ cha–con được vẽ bằng một hình tròn hoặc hình tam giác đặt giữa cha và các con, bên trong ghi ký hiệu ràng buộc sẽ trình bày ở mục 2.7.5.

## 2.7.3. Tính kế thừa

!!! note "Định nghĩa 2.15"

    **Kế thừa** *(inheritance)* là nguyên tắc theo đó **thực thể con tự động có mọi thuộc tính và mọi liên kết của thực thể cha**, mà không cần khai báo lại.

Đây chính là cơ chế loại bỏ dư thừa cấu trúc. Trong Hình 2.11, thực thể `GIAOVIEN` chỉ khai báo hai thuộc tính riêng, nhưng trên thực tế nó **có đầy đủ bảy thuộc tính** — năm thuộc tính kế thừa từ `NHANSU` cộng hai thuộc tính riêng.

Kế thừa áp dụng cho **cả liên kết**, và điều này rất đáng chú ý. Nếu ta khai báo liên kết *"nhân sự thuộc về một phòng ban"* ở mức thực thể cha, thì cả giáo viên lẫn nhân viên hành chính đều tự động có liên kết ấy.

Ngược lại, **liên kết riêng của thực thể con thì không lan lên cha**. Liên kết *"giáo viên phụ trách lớp"* chỉ gắn với `GIAOVIEN`; nhân viên hành chính không phụ trách lớp nào. Đây chính là ưu điểm lớn nhất của EER so với phương án gộp chung ở mục 2.7.1: nó **diễn tả được rằng chỉ một nhóm con mới có liên kết ấy**.

Thuộc tính khóa của thực thể con luôn là **thuộc tính khóa của thực thể cha**. Trong ví dụ trên, thuộc tính khóa của `GIAOVIEN` vẫn là `MANS`, không phải một mã mới. Lý do rất tự nhiên: một giáo viên **là một** nhân sự, nên hai bên nói về cùng một cá thể và phải dùng chung định danh.

## 2.7.4. Chuyên biệt hóa và tổng quát hóa

Có hai hướng đi để đến được một phân cấp cha–con, và chúng phản ánh hai tình huống làm việc khác nhau trong thực tế.

!!! note "Định nghĩa 2.16"

    **Chuyên biệt hóa** *(specialization)* là quá trình đi **từ trên xuống**: xuất phát từ một thực thể tổng quát, phát hiện ra các nhóm con có thuộc tính riêng và tách chúng ra.

    **Tổng quát hóa** *(generalization)* là quá trình đi **từ dưới lên**: xuất phát từ nhiều thực thể riêng lẻ, nhận ra chúng có phần chung và gộp phần chung ấy thành một thực thể cha.

**Chuyên biệt hóa** là con đường thường gặp khi xây hệ thống mới. Người thiết kế bắt đầu với `NHANSU`, rồi trong quá trình phỏng vấn phát hiện ra giáo viên cần lưu bằng cấp còn nhân viên hành chính thì không — thế là tách.

**Tổng quát hóa** là con đường thường gặp khi cải tạo hệ thống cũ. Trung tâm đã có sẵn hai bảng riêng biệt, chạy nhiều năm; người thiết kế nhìn vào và nhận ra chúng lặp lại năm cột giống hệt nhau — thế là gộp phần chung lên thành `NHANSU`.

Hai quá trình cho ra **cùng một kết quả**; chúng chỉ khác nhau ở điểm xuất phát.

## 2.7.5. Hai ràng buộc của phân cấp cha–con

Vẽ được phân cấp mới chỉ là một nửa công việc. Phần còn lại là trả lời **hai câu hỏi ràng buộc**, và câu trả lời quyết định trực tiếp cách cài đặt ở Chương 3.

**Câu hỏi thứ nhất — một cá thể có thể thuộc mấy nhóm con cùng lúc?**

!!! note "Định nghĩa 2.17"

    Ràng buộc **rời nhau** *(disjoint)*: mỗi thể hiện của thực thể cha chỉ thuộc **đúng một** thực thể con. Ký hiệu **`d`**.

    Ràng buộc **chồng lấn** *(overlapping)*: một thể hiện **có thể thuộc nhiều** thực thể con cùng lúc. Ký hiệu **`o`**.

**Câu hỏi thứ hai — mọi cá thể có bắt buộc thuộc một nhóm con nào đó không?**

!!! note "Định nghĩa 2.18"

    Ràng buộc **đầy đủ** *(total / complete)*: mọi thể hiện của cha **đều phải** thuộc ít nhất một con. Ký hiệu bằng **hai gạch** nối cha với vòng tròn.

    Ràng buộc **không đầy đủ** *(partial / incomplete)*: **có thể có** thể hiện của cha không thuộc con nào. Ký hiệu bằng **một gạch**.

Hai câu hỏi độc lập với nhau, nên có bốn tổ hợp.

**Bảng 2.10. Bốn tổ hợp ràng buộc và ví dụ tại Trung tâm ABC**

| Tổ hợp | Nghĩa | Tình huống minh họa |
|---|---|---|
| **Rời nhau + Đầy đủ** | Mỗi nhân sự thuộc **đúng một** nhóm, và **không ai** đứng ngoài | Trung tâm quy định mọi nhân sự **hoặc** là giáo viên **hoặc** là nhân viên hành chính, không kiêm nhiệm |
| **Rời nhau + Không đầy đủ** | Mỗi nhân sự thuộc **nhiều nhất một** nhóm, **có người** đứng ngoài | Ngoài hai nhóm trên còn có bảo vệ, tạp vụ — chưa được mô hình hóa thành nhóm con |
| **Chồng lấn + Đầy đủ** | Có thể thuộc **nhiều nhóm**, nhưng **không ai** đứng ngoài | Một giáo viên kiêm quản lý học vụ — thuộc cả hai nhóm; mọi nhân sự đều thuộc ít nhất một nhóm |
| **Chồng lấn + Không đầy đủ** | Có thể thuộc **nhiều nhóm**, và **có người** đứng ngoài | Trường hợp tổng quát nhất, ít ràng buộc nhất |

!!! example "Ví dụ 2.8"

    Với Trung tâm ABC, câu trả lời **phụ thuộc hoàn toàn vào quy tắc nghiệp vụ**, không phải vào sở thích của người thiết kế. Nếu chủ trung tâm nói *"cô Lê Hoa vừa dạy lớp A1 vừa phụ trách học vụ buổi sáng"*, thì ràng buộc là **chồng lấn**. Nếu chủ trung tâm nói *"chúng tôi còn có một bác bảo vệ và một cô tạp vụ"*, thì ràng buộc là **không đầy đủ**. Đây chính là lý do mục 2.1 nhấn mạnh việc thu thập quy tắc nghiệp vụ cho rõ — nếu không hỏi, người thiết kế sẽ mặc định sai.

## 2.7.6. Khi nào nên và không nên dùng EER

EER là công cụ mạnh, và giống mọi công cụ mạnh, nó bị lạm dụng khá thường xuyên. Ba tiêu chí sau giúp quyết định.

**Nên dùng** khi các nhóm con có **thuộc tính riêng khác nhau đáng kể** — từ khoảng ba thuộc tính trở lên; hoặc khi chúng có **liên kết riêng** mà nhóm khác không có; hoặc khi nghiệp vụ **thật sự phân biệt** các nhóm ấy trong quy trình làm việc.

**Không nên dùng** khi sự khác biệt giữa các nhóm chỉ nằm ở **một thuộc tính** — khi ấy chỉ cần thêm một cột phân loại là đủ; hoặc khi các nhóm con **không có thuộc tính riêng nào**, chỉ khác nhau về tên gọi; hoặc khi phân cấp sâu quá **ba tầng**, vì lúc đó sơ đồ trở nên khó đọc hơn cả vấn đề nó định giải quyết.

!!! warning "Chú ý"

    Người học đã biết lập trình hướng đối tượng rất dễ lạm dụng EER, vì quan hệ cha–con trông giống hệt tính kế thừa của lớp đối tượng. Nhưng có một khác biệt căn bản: trong lập trình, kế thừa là công cụ **tái sử dụng mã nguồn**; trong thiết kế cơ sở dữ liệu, quan hệ cha–con phải phản ánh một **sự phân loại có thật trong nghiệp vụ**. Tiêu chuẩn để dùng nó không phải là "làm thế cho gọn", mà là "nghiệp vụ có thật sự phân biệt hai nhóm này không".

---


---

[← Trang trước](2-6-bac-lien-ket-thuc-the-yeu-va-thuc-the-ket-hop.md) · [Trang sau →](2-8-quy-trinh-xay-dung-luoc-do-er-va-cac-ky-phap.md)
