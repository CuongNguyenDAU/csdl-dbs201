# Ôn tập Chương 2

## Câu hỏi ôn tập

1. Vì sao phải làm thiết kế quan niệm trước thiết kế logic? Điều gì xảy ra nếu nhảy thẳng vào thiết kế bảng?
2. Phát biểu *"Trung tâm chúng tôi phục vụ khách hàng tận tình"* có phải quy tắc nghiệp vụ không? Vì sao?
3. Nêu ba tiêu chí để một danh từ xứng đáng trở thành thực thể. Cho một ví dụ danh từ **không** nên làm thực thể.
4. Vì sao thuộc tính đa trị **bắt buộc** phải tách? Phân tích cụ thể hai cách xử lý sai.
5. Nêu hai tiêu chí bắt buộc của thuộc tính khóa. Cặp `(MAHV, HOTEN)` vi phạm tiêu chí nào?
6. So sánh khóa tự nhiên và khóa thay thế. Vì sao khuyến nghị chung là ưu tiên khóa thay thế làm khóa chính?
7. Trình bày kỹ thuật hỏi hai chiều. Vì sao chỉ hỏi một chiều là không đủ?
8. Cho ví dụ một liên kết mà **tính tham gia khác nhau ở hai chiều**, và giải thích hệ quả ở bước thiết kế bảng.
9. Nêu hai điều kiện của thực thể yếu. Vì sao `LOP` không phải thực thể yếu dù mỗi lớp đều thuộc một khóa học?
10. Vì sao liên kết M:N phải tách, kể cả khi nó **không có** thuộc tính riêng nào?
11. Trình bày quan hệ cha–con trong EER. Phép thử nào giúp phân biệt nó với liên kết thông thường?
12. Phân biệt chuyên biệt hóa và tổng quát hóa. Hai quá trình này khác nhau ở điểm nào?
13. Nêu bốn tổ hợp ràng buộc của phân cấp cha–con. Cho một ví dụ cho tổ hợp *chồng lấn + không đầy đủ*.
14. Khi nào **không nên** dùng EER? Nêu ba trường hợp.
15. Vì sao lược đồ ER của Chương 2 có bảy thực thể trong khi Chương 1 chỉ tìm được ba bảng?

??? note "Gợi ý trả lời một số câu — thử tự trả lời trước khi mở"

    *Câu 5.* Cặp `(MAHV, HOTEN)` thỏa mãn **tính duy nhất** nhưng vi phạm **tính tối thiểu**, vì bỏ `HOTEN` đi thì `MAHV` vẫn đủ phân biệt. Hậu quả: mọi bảng tham chiếu tới học viên phải mang theo cả hai cột, và khi học viên đổi tên thì phải sửa dây chuyền.

    *Câu 9.* Thực thể yếu phải thỏa mãn **đồng thời** phụ thuộc tồn tại **và** khóa không đầy đủ. `LOP` thỏa mãn điều kiện thứ nhất — lớp phải thuộc một khóa học — nhưng **không** thỏa mãn điều kiện thứ hai, vì `MALOP` tự nó đã đủ phân biệt mọi lớp mà không cần mượn `MAKH`. Đây chỉ là phụ thuộc tồn tại thông thường.

    *Câu 10.* Vì **mô hình quan hệ không có cách nào biểu diễn trực tiếp liên kết nhiều–nhiều**. Trong mô hình quan hệ, liên kết được thể hiện bằng khóa ngoại đặt ở một phía; với M:N thì đặt ở phía nào cũng sai, vì cả hai phía đều cần lưu nhiều giá trị. Chương 3 sẽ chứng minh điều này.

    *Câu 11.* Quan hệ cha–con nối một thực thể tổng quát với các nhóm con có thuộc tính riêng; thực thể con kế thừa mọi thuộc tính và liên kết của cha, đồng thời dùng chung thuộc tính khóa. Phép thử là câu **"LÀ MỘT"**: nếu nói *"giáo viên **là một** nhân sự"* nghe xuôi thì là cha–con; còn nếu phải nói *"lớp **có** học viên"* thì đó là liên kết thông thường.

    ---


## Trắc nghiệm tự kiểm tra

Chọn phương án rồi bấm **Kiểm tra**. Mỗi câu đều có giải thích vì sao đúng
và vì sao các phương án còn lại sai. Tiến độ được lưu ngay trên máy của bạn.

<div class="hl-quiz" data-src="quiz/chuong-2.json"></div>

## Thẻ lật khái niệm

Nhấp vào thẻ để lật xem định nghĩa.

<div class="hl-cards" data-src="quiz/chuong-2.json"></div>

## Tự đánh giá theo mục tiêu chương

Tự đối chiếu xem đã đạt từng mục tiêu của chương chưa.

<div class="hl-check" data-src="quiz/chuong-2.json"></div>
