# Ôn tập Chương 1

## Câu hỏi ôn tập

Người học tự trả lời trước khi đối chiếu với gợi ý ở cuối mục.

1. Vì sao nói "dữ liệu không có ngữ cảnh thì không phải là thông tin"? Cho một ví dụ của riêng bạn, khác với ví dụ trong sách.
2. Metadata là gì? Nêu ba thành phần điển hình của metadata cho một cột dữ liệu.
3. Phân biệt cơ sở dữ liệu, hệ quản trị cơ sở dữ liệu và hệ cơ sở dữ liệu. Câu nói "*tôi vừa cài đặt cơ sở dữ liệu MySQL*" sai ở chỗ nào?
4. Kể tên bốn hạn chế của hệ thống tệp. Trong bốn hạn chế đó, hạn chế nào là **nguyên nhân gốc** của những hạn chế còn lại? Giải thích.
5. Cho một bảng có 5 dòng và 7 cột, trong đó ba cột cuối phụ thuộc hoàn toàn vào cột thứ hai và cột thứ hai chỉ nhận đúng hai giá trị phân biệt. Hãy ước lượng số ô dư thừa.
6. Phân biệt lược đồ và thể hiện. Trong hai thứ đó, thứ nào thay đổi thường xuyên hơn, và vì sao điều ngược lại là dấu hiệu đáng lo?
7. Trình bày ba mức của kiến trúc ANSI/SPARC. Vì sao mức ngoài có thể có nhiều, còn mức quan niệm chỉ có một?
8. Phân biệt độc lập dữ liệu logic và độc lập dữ liệu vật lý. Cho một ví dụ cho mỗi loại.
9. Ba mức của **mô hình dữ liệu** khác ba mức của **kiến trúc** ở điểm nào? Hai bộ khái niệm này giao nhau ở đâu?
10. Bốn nhóm ngôn ngữ cơ sở dữ liệu khác nhau ở điểm gì? Nhóm nào tác động lên metadata?
11. Giao dịch là gì? Giải thích tính chất *Atomicity* qua ví dụ chuyển khoản.
12. Trong ba loại dị thường của bảng phẳng, loại nào nguy hiểm nhất? Vì sao?

??? note "Gợi ý trả lời một số câu — thử tự trả lời trước khi mở"

    *Câu 4.* Nguyên nhân gốc là **dư thừa**. Vì cùng một sự thật được lưu ở nhiều chỗ nên mỗi lần cập nhật phải sửa đồng loạt; sót một chỗ là sinh ra **không nhất quán**. Cấu trúc lưu trữ gộp nhiều loại sự vật vào một bảng cũng chính là nguồn gốc của các **dị thường**. Riêng **phụ thuộc dữ liệu** có nguyên nhân khác — nó đến từ việc chương trình gắn chặt với cấu trúc tệp — và được giải quyết bằng kiến trúc ba mức.

    *Câu 5.* Bảng có 35 ô. Ba cột cuối phụ thuộc vào cột thứ hai, mà cột thứ hai chỉ có hai giá trị phân biệt, nghĩa là chỉ cần lưu **2 dòng** thông tin cho ba cột ấy thay vì 5. Mỗi cột thừa 3 ô, ba cột thừa **9 ô** — chiếm khoảng 26%.

    *Câu 7.* Mức ngoài có nhiều vì **mỗi nhóm người dùng có một nhu cầu khác nhau**, và việc cho mỗi nhóm một khung nhìn riêng vừa đơn giản hóa công việc của họ vừa là biện pháp bảo mật. Mức quan niệm chỉ có một vì nó là **mô tả tổng thể duy nhất** của toàn tổ chức; nếu có hai mô tả tổng thể khác nhau thì chính cơ sở dữ liệu đã mâu thuẫn với bản thân nó.

    *Câu 12.* **Dị thường xóa** nguy hiểm nhất, vì hai lý do. Thứ nhất, đây là mất mát dữ liệu thật sự chứ không chỉ là mâu thuẫn. Thứ hai, và quan trọng hơn, nó xảy ra **trong im lặng** — hệ thống thực hiện đúng lệnh xóa được yêu cầu, không có lỗi nào để báo, nên người dùng không hề biết mình vừa mất dữ liệu cho tới khi cần dùng tới.

    ---


## Trắc nghiệm tự kiểm tra

Chọn phương án rồi bấm **Kiểm tra**. Mỗi câu đều có giải thích vì sao đúng
và vì sao các phương án còn lại sai. Tiến độ được lưu ngay trên máy của bạn.

<div class="hl-quiz" data-src="quiz/chuong-1.json"></div>

## Thẻ lật khái niệm

Nhấp vào thẻ để lật xem định nghĩa.

<div class="hl-cards" data-src="quiz/chuong-1.json"></div>

## Tự đánh giá theo mục tiêu chương

Tự đối chiếu xem đã đạt từng mục tiêu của chương chưa.

<div class="hl-check" data-src="quiz/chuong-1.json"></div>
