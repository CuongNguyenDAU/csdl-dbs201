# Chương 5. Lý thuyết thiết kế và chuẩn hóa

## Mục tiêu chương

Sau khi học xong chương này, người học có thể:

1. **Phát biểu** định nghĩa **đo được** của một cơ sở dữ liệu "tốt" và **xác định** vị trí của chuẩn hóa trong quy trình thiết kế *(CLO2)*.
2. **Phân biệt** ba loại phụ thuộc hàm — đầy đủ, bộ phận, bắc cầu — và **chỉ ra** chúng trên một lược đồ cụ thể *(CLO2, CLO3)*.
3. **Vận dụng hệ luật dẫn Armstrong** để suy ra các phụ thuộc hàm mới *(CLO3)*.
4. ⭐ **Tính được bao đóng `X⁺`** của một tập thuộc tính và **phân biệt** nó với `F⁺` *(CLO3)*.
5. ⭐ **Tìm được tất cả khóa** của một lược đồ quan hệ bằng thuật toán TN–TG *(CLO3)*.
6. **Tìm được phủ tối thiểu** của một tập phụ thuộc hàm theo thuật toán ba bước *(CLO3)*.
7. **Xác định** dạng chuẩn cao nhất mà một lược đồ đạt được, có **chứng minh** *(CLO3)*.
8. **Thực hiện phép tách** lược đồ và **chứng minh** phép tách bảo toàn thông tin; **giải thích** hiện tượng **bộ giả** khi tách sai *(CLO3)*.
9. **Chuẩn hóa trọn vẹn** một lược đồ từ bảng phẳng về 3NF, có lập luận đầy đủ ở mỗi bước *(CLO3)*.
10. **Trình bày** BCNF, phụ thuộc đa trị và 4NF; **giải thích** khi nào **phi chuẩn hóa** là hợp lý *(CLO2)*.

---


## Dẫn nhập

Bảng 4.13 ở cuối Chương 4 kết thúc bằng một dòng đáng suy nghĩ. Bốn chương đã đi qua, thiết kế cơ sở dữ liệu của Trung tâm Anh ngữ ABC đã tốt lên rất nhiều — nhưng ở cột cuối cùng, câu hỏi *"chứng minh được không?"* nhận bốn lần trả lời **"không"**.

Ở Chương 1 ta tách bảng vì *"thấy giá trị lặp lại"*. Ở Chương 2 ta tách thực thể vì *"thấy quan hệ nhiều–nhiều"*. Ở Chương 3 ta đặt khóa ngoại vì *"quy tắc ánh xạ bảo thế"*. Ở Chương 4 ta bỏ cột `SISO` vì *"bảng tầm ảnh hưởng có 5 trên 6 ô cộng"*. Mọi lần đều **đúng** — nhưng mọi lần đều dựa vào **kinh nghiệm và trực giác**, không phải chứng minh.

Điều đó có hai hệ quả. Thứ nhất, khi hai người thiết kế bất đồng, **không có trọng tài** — cảm tính chọi cảm tính. Thứ hai, và nghiêm trọng hơn: trực giác **không mở rộng được**. Với bảy bảng thì nhìn ra, với bốn mươi bảng thì không.

Chương 5 cung cấp thứ còn thiếu: một **công cụ toán học** để chứng minh một thiết kế là tốt hay chưa tốt. Công cụ ấy gồm hai phần. Phần thứ nhất là **phụ thuộc hàm** — người học đã gặp ở mục 3.2.2 nhưng khi đó chỉ dùng để định nghĩa khóa; ở đây nó trở thành công cụ phân tích chính. Phần thứ hai là hệ thống **các dạng chuẩn** — một thang đo cho biết lược đồ đang ở mức nào và còn thiếu gì.

Chương này khó hơn bốn chương trước, và cái khó nằm ở tính trừu tượng. Bốn chương đầu luôn có thứ để nhìn: bảng dữ liệu, sơ đồ ER, lược đồ quan hệ. Chương 5 làm việc chủ yếu với **ký hiệu**. Vì vậy giáo trình sắp xếp theo trình tự **công cụ trước, ứng dụng sau**: các mục 5.2 đến 5.6 xây dựng công cụ toán học, các mục 5.7 đến 5.9 dùng chúng để chuẩn hóa. Người học nên chấp nhận rằng bốn mục đầu tiên có vẻ chưa dùng vào việc gì — chúng là móng, và móng thì không nhìn thấy được khi nhà đã xây xong.

Chương kết thúc bằng khoảnh khắc mà cả học phần hướng tới. Khi chuẩn hóa lại **chính bảng phẳng của Chương 1** bằng toán học, kết quả sẽ ra **đúng những bảng mà bốn chương qua ta đã đoán được**. Trực giác đã đoán đúng, bản vẽ đã làm rõ, và toán học **chứng minh**. Đó chính là bước trưởng thành từ *"tôi nghĩ thế này đúng"* sang *"tôi chứng minh được thế này đúng"*.

---


## Các mục trong chương

- [5.1. Thế nào là một cơ sở dữ liệu "tốt"](5-1-the-nao-la-mot-co-so-du-lieu-tot.md)
- [5.2. Ba loại phụ thuộc hàm](5-2-ba-loai-phu-thuoc-ham.md)
- [5.3. Hệ luật dẫn Armstrong](5-3-he-luat-dan-armstrong.md)
- [5.4. Bao đóng của tập thuộc tính](5-4-bao-dong-cua-tap-thuoc-tinh.md)
- [5.5. Thuật toán tìm khóa](5-5-thuat-toan-tim-khoa.md)
- [5.6. Phủ tối thiểu](5-6-phu-toi-thieu.md)
- [5.7. Các dạng chuẩn 1NF, 2NF, 3NF](5-7-cac-dang-chuan-1nf-2nf-3nf.md)
- [5.8. Phép tách lược đồ](5-8-phep-tach-luoc-do.md)
- [5.9. Quy trình chuẩn hóa hoàn chỉnh](5-9-quy-trinh-chuan-hoa-hoan-chinh.md)
- [5.10. Dạng chuẩn mức cao và phi chuẩn hóa](5-10-dang-chuan-muc-cao-va-phi-chuan-hoa.md)
- [5.11. Khép lại học phần](5-11-khep-lai-hoc-phan.md)
