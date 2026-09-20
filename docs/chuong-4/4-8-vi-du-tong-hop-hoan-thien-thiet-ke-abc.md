# 4.8. Ví dụ tổng hợp — hoàn thiện thiết kế ABC

## 4.8.1. Chọn hành động cho từng khóa ngoại

![](../hinh-ve/slide/internet/nhap_lieu.jpg){width=55%}

*Ảnh minh họa: nhân viên nhập liệu tại bàn làm việc. Mỗi phím gõ vào là một lần thêm hoặc sửa dữ liệu — và là một lần ràng buộc phải đứng ra kiểm tra, dù người gõ có nhớ quy tắc hay không — Nguồn: Wikimedia Commons · Department of Labor · Public domain.*

Lược đồ ABC có sáu khóa ngoại. Với mỗi khóa phải chọn hành động khi xóa bản ghi cha, và lựa chọn hoàn toàn dựa vào nghiệp vụ.

**Bảng 4.25. Cùng thao tác "xóa", ba khóa ngoại, ba hành động khác nhau**

| Khóa ngoại | Tình huống | Hành động | Lý do nghiệp vụ |
|---|---|---|---|
| `GHIDANH.MAHV → HOCVIEN` | Xóa học viên **còn ghi danh** | **Từ chối** | Phải bảo toàn **hồ sơ học tập** — học viên đã đóng tiền, đã học |
| `DIENTHOAI.MAHV → HOCVIEN` | Xóa học viên | **Lan truyền** | Số điện thoại **vô nghĩa** nếu không còn học viên — đây là **thực thể yếu** *(mục 2.6.3)* |
| `LOP.MAGV → GIAOVIEN` | Xóa giáo viên | **Gán rỗng** | Lớp **vẫn tồn tại**, chỉ là tạm thời chưa có giáo viên |

Điểm đáng chú ý: **cùng một thao tác "xóa" nhưng ba khóa ngoại cần ba hành động khác nhau**, và khác nhau vì **nghiệp vụ khác nhau** chứ không phải vì kỹ thuật khác nhau. Đây chính là nội dung mà Rubric 3 chấm ở tiêu chí *"thuyết minh và bảo vệ quyết định thiết kế"*.

## 4.8.2. Thiết kế sau khi sửa

Áp đơn thuốc ở mục 4.7.5 — bỏ cột `SISO` khỏi bảng `LOP` — ta được thiết kế cuối cùng:

- Bảng `LOP` còn `(MALOP, TENLOP, NGAYKG, NGAYKT, SUCCHUA, MAGV, MAKH)`.
- **R6 biến mất hoàn toàn.** Muốn biết sĩ số thì đếm trên `GHIDANH`.
- Ràng buộc *"không vượt sức chứa"* vẫn còn và vẫn cần trigger, nhưng nay chỉ so **số đếm thực tế** với `SUCCHUA` — không còn nguy cơ hai nguồn sự thật lệch nhau.

Bộ ràng buộc rút từ sáu xuống **năm**, và ràng buộc khó nhất đã được loại bỏ **bằng cách sửa thiết kế chứ không phải bằng cách viết thêm mã**.

## 4.8.3. Nhìn lại bốn chương

**Bảng 4.26. Bốn chương — và một điểm chung đáng lo**

| | Chương 1 | Chương 2 | Chương 3 | Chương 4 |
|---|---|---|---|---|
| **Việc làm được** | Thấy vấn đề | Mô hình hóa nghiệp vụ | Có cấu trúc chặt chẽ | Bảo vệ tính đúng đắn |
| **Kết quả** | 3 bảng | 7 thực thể | 7 bảng có khóa | 5 ràng buộc |
| **Căn cứ khi quyết định tách bảng** | *"thấy lặp thì tách"* | *"thấy nhiều thì tách"* | *"quy tắc bảo thế"* | *"thấy khó thì sửa"* |
| **Chứng minh được không?** | **Không** | **Không** | **Không** | **Không** |

Dòng cuối cùng là điều đáng suy nghĩ nhất của cả chương. Bốn chương đã đi qua, thiết kế đã tốt hơn rất nhiều — nhưng **mọi quyết định tách bảng vẫn dựa trên cảm tính có kinh nghiệm**, không phải trên chứng minh.

Ngay cả chẩn đoán vừa rồi về `SISO` cũng vậy: ta nhận ra vấn đề vì bảng tầm ảnh hưởng có 5/6 ô `+` — một dấu hiệu **kinh nghiệm**, không phải một **định lý**. Nếu bài toán có bốn mươi bảng, dấu hiệu ấy sẽ không còn nhìn ra được.

**Nối sang Chương 5.** Chương 5 đưa vào công cụ toán học — **phụ thuộc hàm và các dạng chuẩn** — cho phép **chứng minh** một thiết kế là tốt hay chưa tốt, thay vì chỉ cảm nhận. Điều đáng chờ đợi là: khi chuẩn hóa lại bài toán Trung tâm ABC bằng toán học, kết quả sẽ ra **đúng những bảng mà bốn chương qua ta đã đoán được** — nhưng lần này **chứng minh được vì sao đúng**.

---


---

[← Trang trước](4-7-thuc-hanh-phat-hien-rang-buoc-toan-ven.md) · [Trang sau →](tom-tat.md)
