# Ôn tập Chương 5

## Câu hỏi ôn tập

1. Nêu **bốn tiêu chí** của một cơ sở dữ liệu "tốt". Hai tiêu chí nào đôi khi **không thể đạt cùng lúc**?
2. Vì sao nói *"chuẩn hóa không phải để tiết kiệm dung lượng"*? Vậy mục đích thật sự là gì?
3. Phân biệt phụ thuộc **đầy đủ**, **bộ phận**, **bắc cầu**. Vì sao hai loại sau gây hại?
4. Trong định nghĩa phụ thuộc bắc cầu `K → Z → Y`, vì sao điều kiện *"`Z` không phải khóa"* là **bắt buộc**?
5. Nêu ba luật gốc của Armstrong. Vì sao luật phản xạ tuy hiển nhiên nhưng vẫn cần thiết?
6. Trình bày thuật toán tính `X⁺`. Điểm dễ sai nhất khi thực hiện là gì?
7. Phân biệt `F⁺` và `X⁺`. Vì sao toàn bộ lý thuyết chuẩn hóa được xây trên `X⁺` chứ không phải `F⁺`?
8. Giải thích vì sao thuộc tính thuộc `TN` **bắt buộc** có trong mọi khóa, còn thuộc tính thuộc `TĐ` thì **không bao giờ**.
9. Vì sao phải tìm **tất cả** khóa chứ không chỉ một khóa?
10. Trình bày **mẹo rút gọn** khi tìm tất cả khóa. Mẹo này dựa trên tính chất nào của bao đóng?
11. Nêu ba điều kiện của phủ tối thiểu. Vì sao **thứ tự ba bước** trong thuật toán là bắt buộc?
12. Phát biểu 1NF, 2NF, 3NF. Giải thích câu *"the key, the whole key, and nothing but the key"*.
13. **Bộ giả** là gì? Vì sao nó **nguy hiểm hơn** việc mất dữ liệu?
14. Phát biểu điều kiện bảo toàn thông tin. Vì sao *"luôn tách theo phụ thuộc hàm"* thì điều kiện tự động thỏa mãn?
15. Vì sao **mất bảo toàn phụ thuộc hàm** lại là điều đáng lo? Liên hệ với Chương 4.
16. Vì sao thực hành thường **dừng ở 3NF** thay vì leo lên BCNF?
17. Cho một bảng **đã đạt BCNF** nhưng vẫn dư thừa. Nguyên nhân là gì và khắc phục thế nào?
18. Khi nào **phi chuẩn hóa** là hợp lý? Vì sao nó khác với thiết kế cẩu thả?

??? note "Gợi ý trả lời một số câu — thử tự trả lời trước khi mở"

    *Câu 7.* `F⁺` là tập **mọi phụ thuộc hàm** suy ra được từ `F` — kích thước **hàm mũ**, thực tế không tính nổi. `X⁺` là tập **mọi thuộc tính** suy ra được từ `X` — kích thước không quá số thuộc tính của `R`, tính rất nhanh. Mọi câu hỏi tưởng như cần `F⁺` đều quy được về việc tính vài bao đóng `X⁺`; đó là đóng góp thực dụng lớn nhất của khái niệm bao đóng.

    *Câu 10.* Mẹo: duyệt các tập con của `TG` theo **kích thước tăng dần**; nếu `TN ∪ Xᵢ` đã là siêu khóa thì **mọi tập cha** của `Xᵢ` chắc chắn không tối thiểu, loại luôn không cần tính bao đóng. Mẹo dựa trên **tính đơn điệu** của bao đóng: thêm thuộc tính vào `X` thì `X⁺` chỉ có thể lớn lên.

    *Câu 13.* **Bộ giả** là bộ xuất hiện khi ghép các bảng con nhưng **không có trong quan hệ gốc**. Nguy hiểm hơn mất dữ liệu vì: mất dữ liệu thì người dùng **biết mình thiếu** và đi tìm; còn bộ giả khiến hệ thống trả về **nhiều hơn sự thật**, mọi dòng đều trông hợp lệ, và **không ai biết dòng nào bịa**.

    *Câu 15.* Nếu một phụ thuộc hàm bị xé ra hai bảng, thì để kiểm tra nó hệ quản trị phải **ghép hai bảng mỗi lần có thao tác** — tức ràng buộc ấy trở thành loại **liên bộ liên quan hệ**, loại khó nhất trong Bảng 4.6 của Chương 4, phải viết trigger. Nói gọn: **mất bảo toàn phụ thuộc hàm nghĩa là biến một ràng buộc dễ thành một ràng buộc khó.**

    *Câu 17.* Nguyên nhân là **phụ thuộc đa trị**: bảng chứa **hai danh sách độc lập** gắn với cùng một chủ thể, gây **bùng nổ tích**. BCNF không phát hiện được vì bảng có thể không có phụ thuộc hàm không tầm thường nào. Khắc phục: tách về **4NF** — tách `R` thành `X ∪ Y` và `X ∪ Z`; theo định lý Fagin phép tách này luôn bảo toàn thông tin.

    ---


## Trắc nghiệm tự kiểm tra

Chọn phương án rồi bấm **Kiểm tra**. Mỗi câu đều có giải thích vì sao đúng
và vì sao các phương án còn lại sai. Tiến độ được lưu ngay trên máy của bạn.

<div class="hl-quiz" data-src="quiz/chuong-5.json"></div>

## Thẻ lật khái niệm

Nhấp vào thẻ để lật xem định nghĩa.

<div class="hl-cards" data-src="quiz/chuong-5.json"></div>

## Tự đánh giá theo mục tiêu chương

Tự đối chiếu xem đã đạt từng mục tiêu của chương chưa.

<div class="hl-check" data-src="quiz/chuong-5.json"></div>
