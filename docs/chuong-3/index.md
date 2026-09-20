# Chương 3. Mô hình dữ liệu quan hệ

## Mục tiêu chương

Sau khi học xong chương này, người học có thể:

1. **Trình bày** khái niệm quan hệ, bộ, thuộc tính, miền giá trị và **tám đặc trưng** của một bảng quan hệ; **phân biệt** chính xác *quan hệ (relation)* với *liên kết (relationship)* *(CLO2)*.
2. **Xác định** phụ thuộc hàm giữa các thuộc tính và **giải thích** tính có chiều của nó *(CLO2, CLO3)*.
3. **Phân biệt** năm loại khóa — siêu khóa, khóa dự tuyển, khóa chính, khóa ngoại, khóa phụ *(CLO2)*.
4. **Trình bày** hai ràng buộc toàn vẹn thực thể và tham chiếu; **giải thích** vì sao khóa chính cấm giá trị rỗng còn khóa ngoại thì được phép *(CLO2)*.
5. **Vận dụng bốn quy tắc ánh xạ** để chuyển một lược đồ ER — kể cả thực thể yếu, liên kết M:N, liên kết đệ quy và phân cấp cha/con — thành lược đồ quan hệ đầy đủ khóa chính và khóa ngoại *(CLO3)*.
6. **Thực hiện** các phép toán đại số quan hệ: chọn, chiếu, bốn phép toán tập hợp, các biến thể của phép kết và phép chia *(CLO3)*.
7. **Vận dụng phép kết ngoài** để phát hiện lỗi toàn vẹn tham chiếu trong một cơ sở dữ liệu có sẵn *(CLO3)*.
8. **Diễn đạt** một yêu cầu truy vấn bằng lời thành biểu thức đại số quan hệ *(CLO3)*.

---


## Dẫn nhập

Cuối Chương 2, người học đã có trong tay một lược đồ ER hoàn chỉnh của Trung tâm Anh ngữ ABC với bảy thực thể. Nhưng lược đồ ấy vẫn là **một bản vẽ dành cho con người đọc**. Không hệ quản trị cơ sở dữ liệu nào trên thế giới nhận đầu vào là một hình chữ nhật nối với vài hình oval.

Chương 3 làm công việc bắc cầu: chuyển bản vẽ ấy thành một cấu trúc **chặt chẽ về mặt toán học** mà máy tính xử lý được. Cấu trúc đó là **mô hình quan hệ**, do E. F. Codd công bố năm 1970 và đã được giới thiệu sơ lược ở mục 1.4.2 của Chương 1.

Chương này có hai phần rõ rệt, và người học nên ý thức được điều đó ngay từ đầu.

**Phần thứ nhất — cấu trúc.** Các mục 3.1 đến 3.4 trả lời câu hỏi *"dữ liệu được tổ chức thế nào?"*. Ở đây ta học khái niệm quan hệ, hệ thống các loại khóa, hai ràng buộc toàn vẹn nền tảng, và cuối cùng là **bốn quy tắc ánh xạ** biến lược đồ ER thành tập bảng. Phần này chủ yếu là kỹ năng thao tác: một khi đã nắm quy tắc, việc ánh xạ gần như máy móc.

**Phần thứ hai — phép toán.** Các mục 3.5 đến 3.7 trả lời câu hỏi *"lấy dữ liệu ra bằng cách nào?"*. Đây là **đại số quan hệ** — tám phép toán cho phép ta lấy ra bất kỳ thông tin nào từ các bảng đã có. Phần này trừu tượng hơn nhưng cũng chính là chỗ sức mạnh của mô hình quan hệ bộc lộ.

Có một điểm cần nói ngay để tránh hiểu nhầm về phạm vi. Học phần này **không dạy viết câu lệnh SQL**; đó là nội dung của học phần *Hệ quản trị cơ sở dữ liệu*. Nhưng đại số quan hệ chính là **nền tảng lý thuyết của SQL** — mỗi phép toán ở đây tương ứng với một thành phần của câu lệnh truy vấn. Người học nắm chắc đại số quan hệ sẽ học SQL nhanh hơn nhiều, vì lúc đó chỉ còn phải học cú pháp chứ không phải học lại tư duy.

Chương kết thúc bằng việc ánh xạ trọn vẹn lược đồ ABC thành **bảy bảng** với đầy đủ khóa, rồi dùng chính bảy bảng ấy để trả lời sáu câu hỏi nghiệp vụ bằng đại số quan hệ. Đó là lúc ba chương đầu khép lại thành một mạch hoàn chỉnh: Chương 1 thấy vấn đề, Chương 2 có phương pháp, Chương 3 có cấu trúc.

---


## Các mục trong chương

- [3.1. Quan hệ, bộ, thuộc tính và miền giá trị](3-1-quan-he-bo-thuoc-tinh-va-mien-gia-tri.md)
- [3.2. Phụ thuộc hàm và các loại khóa](3-2-phu-thuoc-ham-va-cac-loai-khoa.md)
- [3.3. Các ràng buộc toàn vẹn](3-3-cac-rang-buoc-toan-ven.md)
- [3.4. Bốn quy tắc ánh xạ ER sang mô hình quan hệ](3-4-bon-quy-tac-anh-xa-er-sang-mo-hinh-quan-he.md)
- [3.5. Đại số quan hệ — phép chọn và phép chiếu](3-5-dai-so-quan-he-phep-chon-va-phep-chieu.md)
- [3.6. Các phép toán tập hợp](3-6-cac-phep-toan-tap-hop.md)
- [3.7. Phép kết và phép chia](3-7-phep-ket-va-phep-chia.md)
- [3.8. Ví dụ tổng hợp: Trung tâm Anh ngữ ABC](3-8-vi-du-tong-hop-trung-tam-anh-ngu-abc.md)
