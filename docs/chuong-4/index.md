# Chương 4. Ràng buộc toàn vẹn

## Mục tiêu chương

Sau khi học xong chương này, người học có thể:

1. **Trình bày** khái niệm ràng buộc toàn vẹn và **giải thích** vì sao phải đặt ràng buộc ở **tầng cơ sở dữ liệu** chứ không chỉ ở tầng ứng dụng *(CLO2)*.
2. **Mô tả đầy đủ** một ràng buộc toàn vẹn qua **ba yếu tố**: điều kiện, bối cảnh, bảng tầm ảnh hưởng *(CLO2)*.
3. ⭐ **Lập được bảng tầm ảnh hưởng** cho một ràng buộc bất kỳ, bằng cách áp quy tắc *"đúng thành sai"* cho từng ô *(CLO3)*.
4. **Lựa chọn** hành động xử lý khi vi phạm — từ chối, lan truyền, gán rỗng — dựa trên **lý do nghiệp vụ** *(CLO3)*.
5. **Đọc hiểu** các câu lệnh khai báo ràng buộc trong một hệ quản trị thực tế và **đối chiếu** chúng với ràng buộc đã phát biểu bằng lời *(CLO2)*.
6. **Phân loại** một ràng buộc vào đúng một trong **sáu loại** theo bối cảnh và phạm vi tác động *(CLO2, CLO3)*.
7. **Phát hiện đầy đủ** tập ràng buộc toàn vẹn của một bài toán thực tế, không bỏ sót loại nào *(CLO3)*.
8. **Nhận diện "cờ đỏ thiết kế"** — hiểu rằng một ràng buộc quá khó thực thi thường là dấu hiệu thiết kế cần cải thiện *(CLO3)*.

---


## Dẫn nhập

Cuối Chương 3, lược đồ quan hệ của Trung tâm Anh ngữ ABC trông đã hoàn hảo: bảy bảng, khóa chính đầy đủ, khóa ngoại nối đúng chỗ, hai ràng buộc toàn vẹn được tôn trọng. Một hệ quản trị cơ sở dữ liệu nhận lược đồ này sẽ tạo ra bảy bảng mà không phàn nàn gì.

Nhưng hãy thử nhập vào đó ba dòng dữ liệu sau:

- Một lượt ghi danh với `HOCPHI = -500000` — **học phí âm năm trăm nghìn đồng**.
- Một lớp có ngày khai giảng là năm 1990, trong khi trung tâm mới thành lập năm 2020.
- Một lớp sức chứa 25 người nhưng có 40 học viên ghi danh.

Cả ba dòng đều được hệ quản trị **chấp nhận, không một lời cảnh báo**. Khóa chính không rỗng và không trùng; khóa ngoại đều trỏ tới dòng có thật. Hai ràng buộc của Chương 3 đã được thỏa mãn trọn vẹn — và cả ba dữ liệu vô lý vẫn lọt vào.

Nguyên nhân nằm ở chỗ hai ràng buộc ấy chỉ bảo vệ **cấu trúc**. Chúng biết một khóa ngoại phải trỏ tới đâu, nhưng **không biết gì về nghiệp vụ của trung tâm**. Chúng không biết học phí phải dương, không biết trung tâm thành lập năm nào, không biết mỗi lớp chứa được bao nhiêu người.

Chương 4 lấp đúng khoảng trống đó. Nội dung của chương là xây dựng một **bộ sáu loại ràng buộc** đủ để diễn đạt mọi quy tắc nghiệp vụ, cùng một **quy trình có kỷ luật** để phát hiện chúng mà không bỏ sót.

Chương này có một đặc điểm riêng đáng lưu ý. Ba chương trước dạy cách **xây dựng** — xây mô hình, xây bảng. Chương 4 dạy cách **bảo vệ** cái đã xây. Đây là công việc mà người mới học thường xem nhẹ, vì nó không tạo ra thứ gì nhìn thấy được. Nhưng trong thực tế nghề nghiệp, phần lớn sự cố dữ liệu nghiêm trọng đều bắt nguồn từ những ràng buộc **lẽ ra phải có mà không ai nghĩ tới**.

Chương cũng chứa một ý tưởng bất ngờ, xuất hiện ở mục 4.7.5 và dẫn thẳng sang Chương 5: **khi một ràng buộc trở nên quá khó thực thi, đó thường không phải lỗi của công cụ mà là lời tố cáo về thiết kế.** Người thiết kế có kinh nghiệm, khi gặp ràng buộc khó, không đi tìm công cụ mạnh hơn mà dừng lại xem thiết kế của mình có vấn đề gì.

---


## Các mục trong chương

- [4.1. Khái niệm ràng buộc toàn vẹn](4-1-khai-niem-rang-buoc-toan-ven.md)
- [4.2. Ba yếu tố của một ràng buộc toàn vẹn](4-2-ba-yeu-to-cua-mot-rang-buoc-toan-ven.md)
- [4.3. Lập bảng tầm ảnh hưởng](4-3-lap-bang-tam-anh-huong.md)
- [4.4. Hành động khi vi phạm và cú pháp khai báo](4-4-hanh-dong-khi-vi-pham-va-cu-phap-khai-bao.md)
- [4.5. Ràng buộc toàn vẹn bối cảnh một quan hệ](4-5-rang-buoc-toan-ven-boi-canh-mot-quan-he.md)
- [4.6. Ràng buộc toàn vẹn bối cảnh nhiều quan hệ](4-6-rang-buoc-toan-ven-boi-canh-nhieu-quan-he.md)
- [4.7. Thực hành phát hiện ràng buộc toàn vẹn](4-7-thuc-hanh-phat-hien-rang-buoc-toan-ven.md)
- [4.8. Ví dụ tổng hợp — hoàn thiện thiết kế ABC](4-8-vi-du-tong-hop-hoan-thien-thiet-ke-abc.md)
