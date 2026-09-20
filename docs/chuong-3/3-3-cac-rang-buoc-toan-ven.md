# 3.3. Các ràng buộc toàn vẹn

*(1,0 tiết)*

Mô hình quan hệ đặt ra **hai ràng buộc bắt buộc** mà mọi cơ sở dữ liệu quan hệ đều phải tuân thủ. Chúng đơn giản tới mức dễ bị coi nhẹ, nhưng thiếu chúng thì toàn bộ mô hình sụp đổ.

## 3.3.1. Toàn vẹn thực thể

!!! note "Định nghĩa 3.5"

    **Toàn vẹn thực thể** *(entity integrity)*: khóa chính của mọi quan hệ phải **duy nhất** và **không được nhận giá trị rỗng** *(null)* ở bất kỳ thành phần nào.

![](../hinh-ve/slide/internet/ve_so.jpg){width=55%}

*Ảnh minh họa: người chơi điền vé số. Tờ vé không có dãy số thì không dò được, không trả thưởng được; hai vé cùng số thì không biết trả cho ai — đó là ý nghĩa của toàn vẹn thực thể — Nguồn: Wikimedia Commons · Santeri Viinamäki · CC BY-SA 4.0.*

Lý do rất trực tiếp. Khóa chính tồn tại để **định danh** một dòng. Nếu nó rỗng thì dòng đó không có danh tính — ta không có cách nào chỉ đích danh nó để đọc, sửa hay xóa. Nếu nó trùng thì hai dòng có cùng danh tính, và hệ thống không phân biệt được chúng.

Với khóa chính phức hợp, ràng buộc áp cho **từng thành phần**: trong bảng `GHIDANH(MAHV, MALOP, ...)`, cả `MAHV` lẫn `MALOP` đều không được rỗng.

## 3.3.2. Toàn vẹn tham chiếu

!!! note "Định nghĩa 3.6"

    **Toàn vẹn tham chiếu** *(referential integrity)*: mỗi giá trị của khóa ngoại **hoặc là rỗng, hoặc phải khớp với một giá trị khóa chính đang tồn tại** ở bảng được tham chiếu.

Ràng buộc này ngăn hiện tượng **tham chiếu mồ côi** — một dòng trỏ tới thứ không tồn tại.

!!! example "Ví dụ 3.3"

    Bảng `LOP` có dòng `(A5, 'Anh thương mại', 'GV99')`. Nếu bảng `GIAOVIEN` không có giáo viên nào mang mã `GV99`, thì lớp A5 đang được phụ trách bởi **một người không tồn tại**. Toàn vẹn tham chiếu chặn đúng tình huống này ngay tại thời điểm nhập liệu.

## 3.3.3. Vì sao khóa chính cấm rỗng còn khóa ngoại thì được phép

Đây là câu hỏi người học hay thắc mắc, và câu trả lời nằm ở **ý nghĩa nghiệp vụ của giá trị rỗng trong từng trường hợp**.

Với **khóa chính**, giá trị rỗng có nghĩa là *"dòng này không có danh tính"* — một điều vô nghĩa. Một học viên không có mã học viên thì không phải là một học viên trong hệ thống.

Với **khóa ngoại**, giá trị rỗng lại có nghĩa hoàn toàn hợp lý: *"dòng này hiện chưa liên kết với dòng nào cả"*. Và đây chính là cách mô hình quan hệ cài đặt khái niệm **tham gia tùy chọn** đã học ở mục 2.5.2.

!!! example "Ví dụ 3.4"

    Quy tắc 3 của Trung tâm ABC nói giáo viên **có thể chưa** phụ trách lớp nào. Ở chiều ngược lại, mọi lớp **bắt buộc** phải có giáo viên. Điều này ánh xạ thành: cột `MAGV` trong bảng `LOP` là khóa ngoại **không được rỗng**. Nếu quy tắc nghiệp vụ đổi thành *"lớp có thể tạm thời chưa phân giáo viên"*, thì cột ấy **được phép rỗng**.

Nói cách khác: **tính tham gia ở Chương 2 quyết định việc khóa ngoại ở Chương 3 có được rỗng hay không.** Xác định sai tính tham gia ở bước thiết kế quan niệm sẽ dẫn tới ràng buộc sai ở bước cài đặt — hệ thống hoặc từ chối dữ liệu hợp lệ, hoặc chấp nhận dữ liệu vô nghĩa.

Gom Ví dụ 3.3 và 3.4 lại, hãy thử **chèn bốn dòng** vào cặp bảng ở Bảng 3.10 và xem hệ quản trị trả lời thế nào.

**Bảng 3.11. Bốn lần thử chèn dữ liệu và phán quyết của hai ràng buộc toàn vẹn**

| # | Chèn vào bảng | Dòng định chèn | Ràng buộc được hỏi | Phán quyết |
|:--:|---|---|---|---|
| 1 | `GIAOVIEN` | `(rỗng, 'Ngô Lan', 'Thạc sĩ')` | Toàn vẹn **thực thể** | ✗ **Từ chối** — khóa chính rỗng, dòng không có danh tính |
| 2 | `GIAOVIEN` | `('GV1', 'Ngô Lan', 'Thạc sĩ')` | Toàn vẹn **thực thể** | ✗ **Từ chối** — `GV1` đã là cô Lê Hoa |
| 3 | `LOP` | `('A5', 'Anh thương mại', 'GV99')` | Toàn vẹn **tham chiếu** | ✗ **Từ chối** — `GV99` không có trong `GIAOVIEN` *(Ví dụ 3.3)* |
| 4 | `LOP` | `('A6', 'Anh thiếu nhi', rỗng)` | Toàn vẹn **tham chiếu** | ✓ **Chấp nhận** nếu quy tắc 3 cho phép lớp chưa phân giáo viên; ✗ nếu bắt buộc *(Ví dụ 3.4)* |

Ba dòng đầu bị từ chối **bất kể nghiệp vụ nói gì** — đó là phần "cứng" của mô hình quan hệ. Dòng thứ tư là chỗ duy nhất nghiệp vụ được lên tiếng, và tiếng nói ấy đã được thu ở Chương 2 dưới dạng cặp `(0, N)` hay `(1, N)`.

## 3.3.4. Ba lỗ hổng mà hai ràng buộc này không chặn được

Hai ràng buộc trên là **điều kiện cần chứ chưa đủ**. Chúng chỉ bảo vệ **cấu trúc**; chúng không biết gì về **nghiệp vụ**.

**Bảng 3.12. Ba loại lỗi mà toàn vẹn thực thể và tham chiếu không phát hiện được**

| Tình huống sai | Hai ràng buộc có chặn? | Vì sao không |
|---|:--:|---|
| `HOCPHI = -500000` | **Không** | Đây là ràng buộc **miền giá trị**; hai ràng buộc trên chỉ quan tâm khóa |
| `NGAYKG` của lớp **trước** ngày trung tâm thành lập | **Không** | Ràng buộc **liên thuộc tính**, thuộc phạm vi nghiệp vụ |
| Số học viên trong một lớp **vượt sức chứa** | **Không** | Ràng buộc **liên bộ liên quan hệ**, phải đếm mới biết |

Ba lỗ hổng này chính là lý do tồn tại của **Chương 4 — Ràng buộc toàn vẹn**. Ở đó ta sẽ xây dựng một bộ sáu loại ràng buộc đủ để phủ kín các tình huống nghiệp vụ.

---


---

[← Trang trước](3-2-phu-thuoc-ham-va-cac-loai-khoa.md) · [Trang sau →](3-4-bon-quy-tac-anh-xa-er-sang-mo-hinh-quan-he.md)
