# Học phần Cơ sở dữ liệu

**Mã học phần DBS201 · 3 tín chỉ · 45 tiết lên lớp**
Khoa Công nghệ Thông tin — Trường Đại học Kiến trúc Đà Nẵng

Đây là trang học liệu điện tử của học phần. Toàn bộ nội dung năm chương, slide bài
giảng, câu hỏi ôn tập và bài tập đều nằm ở đây, đọc được trên máy tính lẫn điện thoại.

## Học phần này dạy điều gì

Một câu hỏi duy nhất chạy suốt học phần: **cho một mô tả nghiệp vụ bằng lời, làm
sao thiết kế ra một cơ sở dữ liệu đúng?**

Chương 1 cho thấy vì sao cách làm tùy tiện sinh ra lỗi. Chương 2 thay tùy tiện bằng
một phương pháp có thể kiểm chứng. Chương 3 biến kết quả ấy thành các bảng dữ liệu.
Chương 4 bổ sung các ràng buộc để dữ liệu không bị sai. Chương 5 chứng minh bằng lý
thuyết rằng thiết kế thu được là tốt, và chỉ ra cách sửa khi nó chưa tốt.

Một bài toán thực tế — **Trung tâm Anh ngữ ABC** — theo suốt cả năm chương. Cùng bài
toán ấy, Chương 1 giải bằng trực giác cho ra ba bảng, còn Chương 2 giải bằng phương
pháp cho ra bảy thực thể. Bốn thứ chênh lệch đó chính là nội dung của học phần.

## Năm chương

<div class="grid cards" markdown>

- **[Chương 1 — Tổng quan về cơ sở dữ liệu](chuong-1/index.md)**

    *4 tiết.* Dữ liệu và thông tin, metadata, hệ quản trị, kiến trúc ba mức,
    và chuỗi nhân quả **dư thừa → dị thường** — thứ sẽ dùng để phán xét mọi
    quyết định thiết kế về sau.

- **Chương 2 — Mô hình thực thể – liên kết**

    *8 tiết.* Quy tắc nghiệp vụ, lược đồ ER, kỹ thuật hỏi hai chiều, ba ca đặc
    biệt, mô hình mở rộng EER, và quy trình năm bước.

- **Chương 3 — Mô hình dữ liệu quan hệ**

    *8 tiết.* Quan hệ và khóa, bốn quy tắc ánh xạ từ lược đồ ER sang bảng,
    và đại số quan hệ.

- **Chương 4 — Ràng buộc toàn vẹn**

    *8 tiết.* Ba yếu tố của một ràng buộc, bảng tầm ảnh hưởng, sáu loại ràng
    buộc, và cách xử lý khi bị vi phạm.

- **Chương 5 — Lý thuyết thiết kế và chuẩn hóa**

    *12 tiết.* Phụ thuộc hàm, bao đóng, thuật toán tìm khóa, phủ tối thiểu,
    các dạng chuẩn và phép tách bảo toàn thông tin.

</div>

## Mỗi chương có gì

| Phần | Dùng để làm gì |
|---|---|
| **Các mục nội dung** | Bài giảng đầy đủ, chia nhỏ theo từng mục để dễ đọc và dễ tra |
| **Tóm tắt chương** | Ôn nhanh trước khi thi; kèm danh mục hình, bảng, từ viết tắt |
| **Ôn tập và trắc nghiệm** | Câu hỏi tự luận, **trắc nghiệm tự chấm có giải thích**, thẻ lật khái niệm, bảng tự đánh giá |
| **Bài tập** | Ba mức A, B, C kèm lời giải đầy đủ, mở ra sau khi đã tự làm |
| **Slide bài giảng** | Bản trình chiếu tương tác của từng buổi học |

!!! tip "Cách dùng phần trắc nghiệm cho hiệu quả"

    Bài thi cuối kỳ của học phần này là **trắc nghiệm**, chiếm 50% điểm, trong đó
    60% số câu là **câu tình huống có dữ kiện** — cho một lược đồ, một bảng dữ liệu
    hay một tập quy tắc rồi hỏi. Phần trắc nghiệm trên site được soạn theo đúng tỷ
    lệ ấy, nên làm hết là luyện đúng dạng sẽ gặp.

    Hãy **tự trả lời trước khi mở lời giải**. Mọi gợi ý và đáp án trên site đều được
    giấu trong khối gập, đó là chủ ý — mở ra quá sớm thì mất phần lớn giá trị.

    Kết quả làm bài được lưu **ngay trên máy của bạn**, không gửi đi đâu cả và không
    ai chấm điểm phần này.

## Đánh giá học phần

| Thành phần | Trọng số | Đo chuẩn đầu ra |
|---|:--:|---|
| Chuyên cần và thái độ học tập | 10% | CLO1 |
| Bài tập nhóm tổng hợp | 5% | CLO1 |
| Bài kiểm tra viết *(tuần 5)* | 15% | CLO2 |
| Kiểm tra thực hành — thiết kế trên giấy *(tuần 11)* | 20% | CLO3 |
| **Thi cuối kỳ — trắc nghiệm** | **50%** | CLO2 · CLO3 |

Chi tiết chuẩn đầu ra, rubric chấm điểm và kế hoạch tự học từng tuần xem ở trang
[Đề cương học phần](de-cuong.md).

## Cần chuẩn bị gì

Học phần này **không yêu cầu cài đặt phần mềm nào**. Toàn bộ bài tập làm được bằng
giấy bút; riêng phần vẽ lược đồ có thể dùng [draw.io](https://app.diagrams.net) miễn
phí, chạy thẳng trên trình duyệt.
