# Chương 2. Mô hình thực thể – liên kết

## Mục tiêu chương

Sau khi học xong chương này, người học có thể:

1. **Trình bày** ba mức thiết kế cơ sở dữ liệu và vai trò của **quy tắc nghiệp vụ**; **đánh giá** được một quy tắc nghiệp vụ có đạt tiêu chí "đếm được" hay không *(CLO2)*.
2. **Mô tả** được ba thành phần cơ bản của một **lược đồ ER** và **đọc thành lời** một lược đồ ER đơn giản *(CLO2)*.
3. **Phân biệt** thực thể với thể hiện thực thể; **phân loại** thuộc tính theo bốn cặp tiêu chí và **xử lý đúng** thuộc tính đa trị *(CLO2, CLO3)*.
4. **Xác định** thuộc tính khóa của một thực thể theo hai tiêu chí bắt buộc; **lựa chọn** giữa khóa tự nhiên và khóa thay thế có lập luận *(CLO3)*.
5. **Vận dụng kỹ thuật hỏi hai chiều** để xác định chính xác loại liên kết 1:1, 1:M hay M:N *(CLO3)*.
6. **Xác định** lực lượng và tính tham gia của liên kết; **đọc và vẽ** thành thạo lược đồ theo **ký pháp Chen**, đồng thời **đọc được** lược đồ theo ký pháp Crow's Foot *(CLO2, CLO3)*.
7. **Nhận diện và xử lý** ba trường hợp đặc biệt: liên kết đệ quy, thực thể yếu và liên kết nhiều–nhiều *(CLO3)*.
8. **Trình bày** các khái niệm của mô hình ER mở rộng — thực thể cha/con, kế thừa, chuyên biệt hóa — và **xác định** được hai loại ràng buộc rời nhau/chồng lấn và đầy đủ/không đầy đủ *(CLO2, CLO3)*.
9. **Thực hiện** trọn vẹn quy trình năm bước để xây dựng lược đồ ER cho một bài toán thực tế *(CLO3)*.

---


## Dẫn nhập

Chương 1 đã tách một bảng phẳng của Trung tâm Anh ngữ ABC thành ba bảng liên kết, và cả ba dị thường thêm, sửa, xóa đều biến mất. Nhưng cách tách ấy dựa hoàn toàn vào **trực giác** — nhìn thấy giá trị lặp lại thì tách ra.

Trực giác có một đặc điểm nguy hiểm: nó hoạt động rất tốt trên bài toán nhỏ, nên người ta tin tưởng nó, rồi mang nó áp cho bài toán lớn và thất bại. Với một bảng sáu cột, mắt người nhìn ra ngay chỗ lặp. Với một hệ thống bốn mươi bảng và hai trăm cột, không ai nhìn ra được nữa. Tệ hơn, hai người thiết kế cùng dùng trực giác sẽ cho ra hai kết quả khác nhau, và **không ai có cơ sở nào để nói ai đúng**.

Vấn đề còn sâu hơn thế. Trực giác chỉ nhìn được vào **dữ liệu đã có sẵn**. Nhưng công việc thật của người thiết kế thường bắt đầu khi chưa có dữ liệu nào cả — chỉ có một bản mô tả nghiệp vụ bằng lời của khách hàng. Lúc ấy không có bảng nào để mà "nhìn thấy chỗ lặp".

Chương 2 thay trực giác bằng một **phương pháp**. Phương pháp ấy có tên là **mô hình thực thể – liên kết**, viết tắt là **ER** *(Entity–Relationship)*, do Peter Chen đề xuất năm 1976. Ý tưởng nền tảng của nó rất đơn giản và rất tự nhiên: trước khi nghĩ tới bảng biểu, hãy mô tả **thế giới thực** bằng hai loại thành phần — những **sự vật** ta cần lưu thông tin, và những **mối liên hệ** giữa chúng.

Điều đáng nói là mô hình ER không sinh ra để phục vụ máy tính, mà để phục vụ **cuộc đối thoại giữa người thiết kế và khách hàng**. Một sơ đồ ER vẽ xong có thể đưa cho chủ trung tâm Anh ngữ xem, và người ấy — dù không biết gì về cơ sở dữ liệu — vẫn đọc được và chỉ ra chỗ sai. Đó là giá trị lớn nhất của mô hình này, và cũng là lý do nó sống sót gần năm mươi năm qua trong khi nhiều công nghệ khác đã biến mất.

Người học bước vào chương này với ba điểm tựa từ Chương 1. Thứ nhất là cặp khái niệm **lược đồ – thể hiện**: nó sẽ lặp lại ở đây dưới hình thức *thực thể – thể hiện thực thể*. Thứ hai là **ba mức của mô hình dữ liệu**; toàn bộ Chương 2 chính là công việc ở mức đầu tiên — mức quan niệm. Thứ ba là chuỗi nhân quả **dư thừa → dị thường**; nó sẽ quay lại làm tiêu chuẩn để phán xét mọi quyết định thiết kế trong chương này.

Chương kết thúc bằng một kết quả đáng chú ý: cùng bài toán Trung tâm ABC, phương pháp ER cho ra **bảy thực thể** thay vì ba bảng mà trực giác ở Chương 1 tìm được. Bốn thực thể chênh lệch ấy không phải do Chương 1 sai, mà do trực giác **nhìn không thấy** chúng.

---


## Các mục trong chương

- [2.1. Quá trình thiết kế cơ sở dữ liệu và quy tắc nghiệp vụ](2-1-qua-trinh-thiet-ke-co-so-du-lieu-va-quy-tac-nghiep-vu.md)
- [2.2. Thực thể và thuộc tính](2-2-thuc-the-va-thuoc-tinh.md)
- [2.3. Thuộc tính khóa và định danh](2-3-thuoc-tinh-khoa-va-dinh-danh.md)
- [2.4. Liên kết và kỹ thuật hỏi hai chiều](2-4-lien-ket-va-ky-thuat-hoi-hai-chieu.md)
- [2.5. Kết nối, lực lượng và sự tham gia](2-5-ket-noi-luc-luong-va-su-tham-gia.md)
- [2.6. Bậc liên kết, thực thể yếu và thực thể kết hợp](2-6-bac-lien-ket-thuc-the-yeu-va-thuc-the-ket-hop.md)
- [2.7. Mô hình ER mở rộng (EER)](2-7-mo-hinh-er-mo-rong-eer.md)
- [2.8. Quy trình xây dựng lược đồ ER và các ký pháp](2-8-quy-trinh-xay-dung-luoc-do-er-va-cac-ky-phap.md)
- [2.9. Ví dụ tổng hợp: Trung tâm Anh ngữ ABC](2-9-vi-du-tong-hop-trung-tam-anh-ngu-abc.md)
