# Học phần Cơ sở dữ liệu

**Mã học phần DBS201 · 3 tín chỉ · 45 tiết lên lớp**
Khoa Công nghệ Thông tin — Trường Đại học Kiến trúc Đà Nẵng

Đây là trang học liệu điện tử của học phần. Toàn bộ nội dung năm chương, câu hỏi
ôn tập và bài tập đều nằm ở đây, đọc được trên máy tính lẫn điện thoại.

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

    *4 tiết · tuần 1.* Dữ liệu và thông tin, metadata, hệ quản trị, kiến trúc ba
    mức, và chuỗi nhân quả **dư thừa → dị thường** — thứ sẽ dùng để phán xét mọi
    quyết định thiết kế về sau.

- **[Chương 2 — Mô hình thực thể – liên kết](chuong-2/index.md)**

    *8 tiết · tuần 2–3.* Quy tắc nghiệp vụ, lược đồ ER, kỹ thuật hỏi hai chiều,
    ba ca đặc biệt, mô hình mở rộng EER, và quy trình năm bước.

- **[Chương 3 — Mô hình dữ liệu quan hệ](chuong-3/index.md)**

    *8 tiết · tuần 4–5.* Quan hệ và năm loại khóa, bốn quy tắc ánh xạ từ lược đồ
    ER sang bảng, và tám phép toán đại số quan hệ.

- **[Chương 4 — Ràng buộc toàn vẹn](chuong-4/index.md)**

    *8 tiết · tuần 6–7.* Ba yếu tố của một ràng buộc, bảng tầm ảnh hưởng, sáu
    loại ràng buộc, và cách xử lý khi bị vi phạm.

- **[Chương 5 — Lý thuyết thiết kế và chuẩn hóa](chuong-5/index.md)**

    *12 tiết · tuần 8–10.* Phụ thuộc hàm, bao đóng, thuật toán tìm khóa, phủ tối
    thiểu, các dạng chuẩn và phép tách bảo toàn thông tin.

</div>

## Mỗi chương có gì

| Phần | Dùng để làm gì |
|---|---|
| **Các mục nội dung** | Bài giảng đầy đủ, chia nhỏ theo từng mục để dễ đọc và dễ tra |
| **Tóm tắt chương** | Ôn nhanh trước khi thi; kèm danh mục hình, bảng, từ viết tắt |
| **Ôn tập và trắc nghiệm** | Câu hỏi tự luận, **trắc nghiệm tự chấm có giải thích**, thẻ lật khái niệm, bảng tự đánh giá |
| **Bài tập** | Ba mức A, B, C kèm lời giải đầy đủ, mở ra sau khi đã tự làm |

!!! tip "Cách dùng phần trắc nghiệm cho hiệu quả"

    Bài thi cuối kỳ là **trắc nghiệm**, chiếm 50% điểm, chia ba khối: **khối A**
    60% số câu về khái niệm nền, **khối B1** 15% là tình huống ràng buộc toàn vẹn
    của Chương 4, **khối B2** 25% là tình huống chuẩn hóa của Chương 5. Mọi câu
    khối B đều **kèm dữ kiện** — một lược đồ, một tập phụ thuộc hàm, một bảng tầm
    ảnh hưởng — nên phải chạy thuật toán rồi mới chọn được đáp án.

    Mỗi câu trên site đều ghi rõ nó thuộc khối nào, nên anh chị biết mình đang
    luyện cho phần nào của đề. Riêng Chương 2 và Chương 3 còn được đo bằng **hai
    bài kiểm tra viết** ở tuần 5 và tuần 6 — câu gắn nhãn *Dạng bài kiểm tra viết*
    là để luyện cho hai bài đó.

    Hãy **tự trả lời trước khi mở lời giải**. Mọi gợi ý và đáp án trên site đều được
    giấu trong khối gập, đó là chủ ý — mở ra quá sớm thì mất phần lớn giá trị.

    Kết quả làm bài được lưu **ngay trên máy của bạn**, không gửi đi đâu cả và không
    ai chấm điểm phần này.

## Đánh giá học phần

| Thành phần | Trọng số | Đo chuẩn đầu ra | Rubric |
|---|:--:|---|:--:|
| Nhận thức thái độ — chuyên cần, nội quy, hồ sơ tự học, hợp tác nhóm | 15% | CLO1 | 1 |
| Bài kiểm tra viết — quy tắc nghiệp vụ thành mô hình ER *(tuần 5)* | 15% | CLO3 | 2 |
| Bài kiểm tra giữa học phần — ánh xạ ER sang quan hệ và đại số quan hệ *(tuần 6)* | 20% | CLO3 | 3 |
| **Thi cuối kỳ — trắc nghiệm theo khối kiến thức** | **50%** | CLO2 60% · CLO3 40% | 4 |

Ba bài đánh giá đều **làm trên lớp, trên giấy** — học phần không yêu cầu viết SQL
hay cài đặt hệ quản trị nào. Điểm đáng chú ý: **hồ sơ tự học chiếm 30 trong 100
điểm của Rubric 1**, tức là 11 nhiệm vụ tự học hằng tuần có ảnh hưởng thật tới điểm.

Chi tiết chuẩn đầu ra, cả bốn rubric chấm điểm và kế hoạch tự học từng tuần xem ở
trang [Đề cương học phần](de-cuong.md).

## Cần chuẩn bị gì

Học phần này **không yêu cầu cài đặt phần mềm nào**. Toàn bộ bài tập làm được bằng
giấy bút; riêng phần vẽ lược đồ có thể dùng [draw.io](https://app.diagrams.net) miễn
phí, chạy thẳng trên trình duyệt.
