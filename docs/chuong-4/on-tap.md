# Ôn tập Chương 4

## Câu hỏi ôn tập

1. Vì sao hai ràng buộc của Chương 3 không đủ? Cho ba ví dụ dữ liệu vô lý mà chúng không chặn được.
2. Vì sao nói *"cứ để phần mềm ứng dụng kiểm tra là được"* là một sai lầm tốn kém? Nêu ít nhất ba đường vào cơ sở dữ liệu không đi qua ứng dụng.
3. Nêu ba yếu tố mô tả đầy đủ một ràng buộc. Yếu tố nào quyết định loại của ràng buộc?
4. Viết bằng ký hiệu logic ràng buộc *"mỗi lớp có nhiều nhất 40 học viên"*.
5. Bảng tầm ảnh hưởng dùng để làm gì? Vì sao **không nên** đánh dấu `+` cho mọi ô?
6. Phát biểu **quy tắc vàng** khi lập bảng tầm ảnh hưởng. Giả thiết ngầm của câu hỏi ấy là gì?
7. Giải thích câu thần chú *"thêm ở con, xóa ở cha"*. Vì sao thêm vào bảng cha lại **không** nguy hiểm?
8. Nêu ba hành động khi vi phạm. Khi nào **được phép** dùng lan truyền?
9. Vì sao trong cùng bảng `GHIDANH`, khóa ngoại trỏ về `HOCVIEN` dùng *từ chối* còn khóa ngoại trỏ về `LOP` dùng *lan truyền*?
10. Cơ chế `CHECK` diễn đạt được những loại ràng buộc nào? Nó **không** diễn đạt được loại nào, và vì sao?
11. Phép thử nào phân biệt ràng buộc **liên thuộc tính** với **liên bộ**?
12. Trigger là gì? Nêu ba rủi ro khi dùng trigger.
13. Vì sao ràng buộc **liên bộ liên quan hệ** là loại khó nhất trong sáu loại?
14. Ràng buộc R6 có 5/6 ô `+`. Điều đó **chẩn đoán** ra vấn đề gì, và **đơn thuốc** là gì?
15. Sau bốn chương, điều gì vẫn còn thiếu trong cách ta ra quyết định thiết kế?

??? note "Gợi ý trả lời một số câu — thử tự trả lời trước khi mở"

    *Câu 6.* Quy tắc vàng: *"thao tác này có thể biến điều kiện từ **đúng** thành **sai** không?"* Giả thiết ngầm là **điều kiện đang đúng trước thao tác**. Nếu bỏ giả thiết này thì câu hỏi trở thành *"dữ liệu có thể sai không"* — luôn luôn có, và bảng mất ý nghĩa.

    *Câu 7.* Thêm vào bảng **con** là **tạo ra một mũi tên mới**, mà mũi tên ấy có thể trỏ vào chỗ không tồn tại. Xóa ở bảng **cha** là **rút đi cái đích**, làm các mũi tên đang trỏ tới bị treo. Ngược lại, thêm vào cha chỉ là **tạo thêm đích** — không mũi tên nào đang có bị ảnh hưởng; xóa ở con là **bớt mũi tên** — càng ít thứ phải kiểm.

    *Câu 10.* `CHECK` chỉ kiểm tra được trong phạm vi **một dòng của một bảng**, nên nó diễn đạt được ràng buộc **miền giá trị** và **liên thuộc tính**. Nó **không** diễn đạt được ràng buộc **liên bộ** *(phải so với dòng khác)*, **liên thuộc tính liên quan hệ** và **liên bộ liên quan hệ** *(phải nhìn bảng khác)*. Đó là lý do phải dùng trigger cho ba loại ấy.

    *Câu 14.* **Chẩn đoán**: `SISO` là **thuộc tính dẫn xuất** — nó tính được từ số dòng của `GHIDANH`. Lưu nó tạo ra **hai nguồn sự thật** cho cùng một thông tin, nên gần như thao tác nào cũng làm hai nguồn lệch nhau. **Đơn thuốc**: bỏ hẳn cột `SISO`, tính khi cần bằng phép đếm. Khi đó **R6 biến mất** — không cần ràng buộc nữa vì chỉ còn một nguồn sự thật.

    ---


## Trắc nghiệm tự kiểm tra

Chọn phương án rồi bấm **Kiểm tra**. Mỗi câu đều có giải thích vì sao đúng
và vì sao các phương án còn lại sai. Tiến độ được lưu ngay trên máy của bạn.

<div class="hl-quiz" data-src="quiz/chuong-4.json"></div>

## Thẻ lật khái niệm

Nhấp vào thẻ để lật xem định nghĩa.

<div class="hl-cards" data-src="quiz/chuong-4.json"></div>

## Tự đánh giá theo mục tiêu chương

Tự đối chiếu xem đã đạt từng mục tiêu của chương chưa.

<div class="hl-check" data-src="quiz/chuong-4.json"></div>
