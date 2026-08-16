# Chương 1. Tổng quan về cơ sở dữ liệu

## Mục tiêu chương

Sau khi học xong chương này, người học có thể *(gắn **CLO2** — mức Bloom: **Hiểu**)*:

1. **Phân biệt** dữ liệu với thông tin; **trình bày** được khái niệm cơ sở dữ liệu và vai trò của metadata.
2. **Phân biệt** ba khái niệm thường bị dùng lẫn lộn: cơ sở dữ liệu, hệ quản trị cơ sở dữ liệu và hệ cơ sở dữ liệu; **phân loại** được các hệ quản trị cơ sở dữ liệu theo ba tiêu chí thông dụng.
3. **Giải thích** bốn hạn chế của cách tổ chức dữ liệu bằng hệ thống tệp và **chỉ ra** cách tiếp cận cơ sở dữ liệu khắc phục từng hạn chế như thế nào.
4. **Phân biệt** mô hình dữ liệu, lược đồ và thể hiện; **trình bày** được các thế hệ mô hình dữ liệu và lý do mô hình quan hệ chiếm ưu thế.
5. **Mô tả** kiến trúc ba mức ANSI/SPARC, **giải thích** hai loại độc lập dữ liệu và **phân biệt** kiến trúc này với ba mức của mô hình dữ liệu.
6. **Phân loại** các nhóm ngôn ngữ cơ sở dữ liệu; **trình bày** khái niệm giao dịch cùng bốn tính chất ACID ở mức nhận biết; **mô tả** các chức năng của một hệ quản trị cơ sở dữ liệu và năm thành phần của một hệ cơ sở dữ liệu.

---


## Dẫn nhập

Hãy hình dung một trung tâm Anh ngữ nhỏ. Ngày đầu khai trương, cô phụ trách tuyển sinh mở một tệp bảng tính để ghi danh sách học viên. Ít lâu sau, bộ phận học vụ cần theo dõi lớp học nên lập thêm một tệp nữa. Rồi kế toán cần thu học phí, lại thêm một tệp thứ ba. Mỗi tệp do một người giữ, mỗi người quen tay với cách sắp xếp của riêng mình. Trong sáu tháng đầu, mọi thứ vận hành trơn tru.

Sang năm thứ hai, số học viên tăng gấp năm lần và những rắc rối bắt đầu lộ ra. Một học viên đổi số điện thoại, báo cho bộ phận tuyển sinh; ba tháng sau kế toán gọi điện nhắc học phí thì gọi vào số cũ. Giám đốc trung tâm muốn biết *"doanh thu theo từng lớp trong quý vừa rồi"* — một câu hỏi tưởng đơn giản — nhưng để trả lời phải ghép tay ba tệp với nhau mất trọn một buổi chiều, và con số cuối cùng vẫn không ai dám chắc là đúng. Tệ hơn cả, khi một học viên xin nghỉ và bị xóa khỏi danh sách, hóa ra lớp học của em ấy cũng biến mất theo, bởi vì tên lớp chỉ được ghi trong chính dòng dữ liệu của em.

Câu chuyện này không phải là câu chuyện về phần mềm bảng tính. Bảng tính không có lỗi gì cả — nó vốn được thiết kế để tính toán, không phải để quản lý dữ liệu dùng chung cho nhiều người. Đây là câu chuyện về **cách tổ chức dữ liệu**, và chính những rắc rối vừa kể là lý do khiến ngành công nghệ thông tin phải phát triển ra một lớp công nghệ riêng: **cơ sở dữ liệu**.

Chương 1 đặt nền móng cho toàn bộ học phần. Chương này chưa dạy cách thiết kế — việc đó bắt đầu từ Chương 2 — mà làm một việc quan trọng hơn về mặt nhận thức: giúp người học **nhìn thấy vấn đề**. Chỉ khi hiểu rõ điều gì hỏng trong cách tổ chức dữ liệu tùy tiện, người học mới thấy các kỹ thuật ở những chương sau là cần thiết chứ không phải là quy tắc học thuộc.

Người học đã có sẵn hai điểm tựa để bước vào chương này. Thứ nhất, từ học phần *Tin học cơ bản*, ai cũng quen thao tác với tệp, thư mục và bảng tính; chương này sẽ chỉ ra chính xác bảng tính còn thiếu điều gì để trở thành cơ sở dữ liệu. Thứ hai, từ kinh nghiệm đời sống, ai cũng đã sử dụng cơ sở dữ liệu mà không để ý: mỗi lần tra cứu điểm thi, rút tiền ở máy ATM hay đặt vé xe khách qua ứng dụng, phía sau đều là một cơ sở dữ liệu đang làm việc.

Cần lưu ý ngay từ đầu về phạm vi. Học phần này tập trung vào **nền tảng và thiết kế**. Kỹ thuật viết câu lệnh SQL, các vấn đề an toàn — bảo mật và quản lý giao dịch chuyên sâu thuộc học phần *Hệ quản trị cơ sở dữ liệu* kế tiếp. Chương 1 chỉ giới thiệu những nội dung đó ở mức nhận biết, đủ để người học định vị được chúng trong bức tranh chung.

Toàn chương được dẫn dắt bằng một tình huống xuyên suốt: **Trung tâm Anh ngữ ABC**. Tình huống này sẽ còn theo người học đến hết Chương 5, mỗi chương lại được nhìn dưới một góc độ sâu hơn.

---


## Các mục trong chương

- [1.1. Dữ liệu, thông tin và cơ sở dữ liệu](1-1-du-lieu-thong-tin-va-co-so-du-lieu.md)
- [1.2. Hệ quản trị cơ sở dữ liệu](1-2-he-quan-tri-co-so-du-lieu.md)
- [1.3. Vì sao cần cơ sở dữ liệu](1-3-vi-sao-can-co-so-du-lieu.md)
- [1.4. Mô hình dữ liệu, lược đồ và thể hiện](1-4-mo-hinh-du-lieu-luoc-do-va-the-hien.md)
- [1.5. Kiến trúc ba mức và tính độc lập dữ liệu](1-5-kien-truc-ba-muc-va-tinh-doc-lap-du-lieu.md)
- [1.6. Ngôn ngữ, giao dịch và cấu trúc của một hệ quản trị cơ sở dữ liệu](1-6-ngon-ngu-giao-dich-va-cau-truc-cua-mot-he-quan-tri-co-so-du-lieu.md)
- [1.7. Ví dụ tổng hợp: Trung tâm Anh ngữ ABC](1-7-vi-du-tong-hop-trung-tam-anh-ngu-abc.md)
