# Ôn tập Chương 3

## Câu hỏi ôn tập

1. Vì sao mô hình được gọi là *"mô hình quan hệ"*? Bác bỏ cách hiểu *"vì nó có quan hệ giữa các bảng"*.
2. Nêu tám đặc trưng của một bảng quan hệ. Đặc trưng nào đã được dùng ở Chương 2 mà chưa gọi tên?
3. Phân biệt *bậc* và *lực lượng*. Vì sao từ *"lực lượng"* ở Chương 3 khác nghĩa với ở Chương 2?
4. Vì sao không được viết chương trình kiểu *"lấy dòng đầu tiên vì đó là bản ghi mới nhất"*?
5. Phụ thuộc hàm là gì? Vì sao nói nó là **quy tắc nghiệp vụ** chứ không phải quan sát trên dữ liệu?
6. Phân biệt siêu khóa, khóa dự tuyển và khóa chính. Quan hệ giữa ba loại này là gì?
7. Nêu hai ràng buộc toàn vẹn. Vì sao khóa chính cấm rỗng còn khóa ngoại được phép?
8. **Chứng minh** vì sao khóa ngoại của liên kết 1:M bắt buộc phải đặt ở phía "nhiều".
9. Vì sao liên kết M:N phải tách thành bảng mới **kể cả khi** nó không có thuộc tính riêng?
10. Nêu ba phương án ánh xạ phân cấp cha/con. Với ràng buộc *chồng lấn + không đầy đủ*, chọn phương án nào và vì sao?
11. Tính đóng kín của đại số quan hệ là gì? Nó mang lại lợi ích gì?
12. Điều kiện khả hợp gồm mấy điều kiện? **Vì sao tích Descartes không đòi hỏi khả hợp** trong khi ba phép tập hợp còn lại thì có?
13. Phép kết tự nhiên gồm ba bước nào? Bỏ bước nào thì thành tích Descartes?
14. Trình bày kỹ thuật dùng kết ngoài để dò khóa ngoại mồ côi. Cạm bẫy khi dùng kỹ thuật này là gì?
15. Dấu hiệu nào cho biết một bài toán cần dùng phép chia?

??? note "Gợi ý trả lời một số câu — thử tự trả lời trước khi mở"

    *Câu 8.* Giả sử đặt khóa ngoại ở phía "1", tức thêm cột `MALOP` vào bảng `GIAOVIEN`. Vì một giáo viên phụ trách nhiều lớp nên ô `MALOP` của giáo viên ấy phải chứa **nhiều giá trị** — vi phạm **Đặc trưng 4** *(mỗi ô một giá trị đơn)*, tức đúng lỗi thuộc tính đa trị đã bị cấm từ Chương 2. Đặt ở phía "nhiều" thì mỗi lớp chỉ có một giáo viên nên mỗi ô chỉ chứa một giá trị; giáo viên lặp lại ở nhiều **dòng**, điều này hoàn toàn hợp lệ.

    *Câu 12.* Khả hợp gồm **hai** điều kiện: cùng bậc, và các thuộc tính tương ứng cùng miền giá trị. Ba phép `∪`, `∩`, `−` **so sánh các bộ với nhau** để quyết định giữ hay bỏ, nên hai bộ phải cùng cấu trúc mới so sánh được. Tích Descartes **không so sánh gì cả** — nó chỉ nối hai bộ thành một bộ dài hơn *(bậc kết quả bằng tổng hai bậc)*, nên hai quan hệ đầu vào có cấu trúc bất kỳ đều ghép được.

    *Câu 14.* Kết ngoài trái `LOP ⟕ GIAOVIEN` giữ mọi dòng của `LOP`; những lớp có `MAGV` mồ côi sẽ có các cột bên phải **rỗng**. Lọc lấy các dòng ấy là ra danh sách lỗi. **Cạm bẫy**: cột bên phải rỗng có **hai nguyên nhân** — mồ côi thật, hoặc `MAGV` vốn rỗng *(lớp chưa phân giáo viên, có thể hợp lệ)*. Phải thêm điều kiện *"`MAGV` khác rỗng"*, nếu không sẽ báo nhầm hàng loạt dòng hợp lệ thành lỗi.

    ---


## Trắc nghiệm tự kiểm tra

Chọn phương án rồi bấm **Kiểm tra**. Mỗi câu đều có giải thích vì sao đúng
và vì sao các phương án còn lại sai. Tiến độ được lưu ngay trên máy của bạn.

<div class="hl-quiz" data-src="quiz/chuong-3.json"></div>

## Thẻ lật khái niệm

Nhấp vào thẻ để lật xem định nghĩa.

<div class="hl-cards" data-src="quiz/chuong-3.json"></div>

## Tự đánh giá theo mục tiêu chương

Tự đối chiếu xem đã đạt từng mục tiêu của chương chưa.

<div class="hl-check" data-src="quiz/chuong-3.json"></div>
