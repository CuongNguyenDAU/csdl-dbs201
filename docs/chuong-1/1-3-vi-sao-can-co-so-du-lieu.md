# 1.3. Vì sao cần cơ sở dữ liệu

*(1,0 tiết)*

Mục này trả lời câu hỏi nền tảng nhất của chương: **nếu đã có tệp và bảng tính, tại sao còn phải học cơ sở dữ liệu?** Câu trả lời không nằm ở chỗ cơ sở dữ liệu "hiện đại hơn", mà nằm ở bốn hạn chế cụ thể, có thể chỉ ra và định lượng được, của cách tổ chức dữ liệu bằng hệ thống tệp.

## 1.3.1. Hệ thống tệp và bốn hạn chế của nó

Trước khi cơ sở dữ liệu ra đời vào cuối những năm 1960, các tổ chức quản lý dữ liệu bằng **hệ thống tệp** *(file system)*: mỗi bộ phận nghiệp vụ có tệp dữ liệu riêng và chương trình xử lý riêng. Cách làm này vẫn còn phổ biến đến ngày nay dưới hình thức "mỗi phòng một tệp bảng tính".

**Hình 1.2. Hệ thống tệp và cách tiếp cận cơ sở dữ liệu**

```mermaid
flowchart LR
    subgraph FS["HỆ THỐNG TỆP — mỗi bộ phận một tệp riêng"]
        A1["Phòng Tuyển sinh"] --> F1[("HOCVIEN.xls")]
        A2["Phòng Học vụ"] --> F2[("LOP.xls")]
        A3["Phòng Kế toán"] --> F3[("HOCPHI.xls")]
    end
    subgraph DBA["CÁCH TIẾP CẬN CSDL — một kho dùng chung"]
        B1["Phòng Tuyển sinh"] --> D["<b>DBMS</b>"]
        B2["Phòng Học vụ"] --> D
        B3["Phòng Kế toán"] --> D
        D --> DB[("<b>CSDL</b><br/>dùng chung")]
    end
    style F1 fill:#FFD9D9,stroke:#C00000
    style F2 fill:#FFD9D9,stroke:#C00000
    style F3 fill:#FFD9D9,stroke:#C00000
    style D fill:#1F4E79,color:#fff,stroke:#1F4E79,stroke-width:2px
    style DB fill:#D9E2F3,stroke:#1F4E79,stroke-width:2px
```

Nhìn vào **khối phía dưới** của hình vẽ — phần mô tả hệ thống tệp — có thể thấy ngay điều bất thường: **họ tên và số điện thoại của cùng một học viên xuất hiện trong cả ba tệp**. Từ quan sát đó, bốn hạn chế lần lượt lộ ra.

**Hạn chế thứ nhất — dư thừa dữ liệu** *(data redundancy)*. Cùng một sự kiện được lưu ở nhiều nơi. Đây không đơn thuần là chuyện tốn dung lượng lưu trữ; dung lượng ngày nay rất rẻ. Vấn đề nằm ở chỗ dư thừa là **nguồn gốc** của ba hạn chế còn lại.

**Hạn chế thứ hai — không nhất quán dữ liệu** *(data inconsistency)*. Khi một sự kiện được lưu ở ba nơi, chỉ cần cập nhật thiếu một nơi là cơ sở dữ liệu chứa hai giá trị mâu thuẫn cho cùng một sự thật. Điều đáng sợ là hệ thống **không hề báo lỗi**: cả hai giá trị đều là dữ liệu hợp lệ xét riêng lẻ. Sự mâu thuẫn chỉ bị phát hiện khi có người tình cờ đối chiếu, thường là rất muộn.

**Hạn chế thứ ba — dị thường khi cập nhật** *(update anomalies)*. Do cấu trúc lưu trữ nhập nhằng, các thao tác thêm, sửa, xóa gây ra những hậu quả ngoài ý muốn. Ba loại dị thường cụ thể sẽ được phân tích chi tiết ở mục 1.7.

**Hạn chế thứ tư — phụ thuộc dữ liệu** *(data dependence)*. Trong hệ thống tệp, mỗi chương trình phải tự biết cấu trúc vật lý của tệp: cột nào ở vị trí nào, dài bao nhiêu ký tự. Hệ quả là **chỉ cần đổi cấu trúc tệp một chút là mọi chương trình đọc tệp ấy đều phải sửa lại**. Thêm một cột "email" vào tệp học viên có thể buộc phải sửa và biên dịch lại năm chương trình khác nhau. Đây là hạn chế tốn kém nhất về lâu dài và cũng chính là hạn chế mà kiến trúc ba mức ở mục 1.5 được sinh ra để giải quyết.

## 1.3.2. Định lượng mức dư thừa trên một trường hợp cụ thể

Nói "dư thừa gây hại" là nói định tính. Người thiết kế cần biết định lượng. Ta xét bảng dữ liệu phẳng của Trung tâm ABC — cùng chính là bảng sẽ được dùng lại ở mục 1.7 và ở các chương sau.

**Bảng 1.5. Tệp phẳng `HOCVIEN_LOP` của Trung tâm Anh ngữ ABC**

| MAHV | HOTEN | MALOP | TENLOP | GIAOVIEN | SDT_GV |
|---|---|---|---|---|---|
| HV01 | Trần An | A1 | Anh cơ bản 1 | Lê Hoa | 0905111111 |
| HV02 | Lê Bình | A1 | Anh cơ bản 1 | Lê Hoa | 0905111111 |
| HV03 | Phạm Cường | A1 | Anh cơ bản 1 | Lê Hoa | 0905111111 |
| HV04 | Võ Dung | A2 | Anh giao tiếp | Trần Mai | 0905222222 |

Bảng có 4 dòng và 6 cột, tổng cộng 24 ô. Hãy đếm xem bao nhiêu ô trong số đó là **thừa** — hiểu theo nghĩa: nếu xóa đi, ta vẫn khôi phục lại được từ những ô còn lại.

Ba cột `MAHV`, `HOTEN` là dữ liệu riêng của từng học viên, không dòng nào lặp lại dòng nào: **8 ô, không thừa ô nào**. Cột `MALOP` chỉ có hai giá trị phân biệt là A1 và A2, nhưng mã lớp cần thiết để biết học viên nào học lớp nào, nên cũng **không thừa**. Ba cột còn lại thì khác. `TENLOP` phụ thuộc hoàn toàn vào `MALOP`: hễ biết A1 là biết ngay "Anh cơ bản 1". Ba dòng đầu cùng ghi "Anh cơ bản 1" nghĩa là **hai ô thừa**. Tương tự, `GIAOVIEN` và `SDT_GV` đều phụ thuộc vào `MALOP`, mỗi cột thừa hai ô ở ba dòng đầu — tổng cộng **bốn ô thừa** nữa.

Vậy trong 24 ô có **6 ô thừa, chiếm 25%**. Con số này không lớn vì bảng ví dụ chỉ có 4 dòng. Nhưng hãy để ý điều gì xảy ra khi trung tâm phát triển: nếu lớp A1 có 30 học viên thay vì 3, thì riêng thông tin của cô Lê Hoa sẽ bị lặp **30 lần**, và tỷ lệ ô thừa vọt lên xấp xỉ 50%. **Mức dư thừa tăng theo quy mô dữ liệu, trong khi lượng thông tin thật sự thì không đổi** — cô Lê Hoa vẫn chỉ có một số điện thoại duy nhất.

!!! warning "Chú ý"

    Cách nhận diện dư thừa ở đây vẫn dựa vào trực giác — "thấy giá trị lặp lại thì nghi ngờ". Trực giác này đủ dùng cho một bảng 6 cột, nhưng sẽ thất bại với hệ thống hàng chục bảng. Chương 5 sẽ thay trực giác bằng một công cụ toán học chính xác gọi là **phụ thuộc hàm**, và khi đó câu "`TENLOP` phụ thuộc hoàn toàn vào `MALOP`" sẽ được viết gọn thành `MALOP → TENLOP`.

## 1.3.3. Từ dư thừa đến quyết định sai

Bốn hạn chế nêu ở mục 1.3.1 không đứng độc lập; chúng nối với nhau thành một chuỗi nhân quả mà gốc rễ là **dư thừa**.

Dư thừa khiến cùng một sự thật được lưu ở nhiều chỗ. Vì nằm ở nhiều chỗ nên mỗi lần thay đổi phải cập nhật đồng loạt, mà cập nhật đồng loạt thì sớm muộn cũng sót — sinh ra **không nhất quán**. Khi dữ liệu đã mâu thuẫn, mọi báo cáo tổng hợp từ nó đều đáng ngờ: hai bộ phận cùng đếm số học viên đang theo học có thể ra hai con số khác nhau, và không ai biết con số nào đúng. Báo cáo sai dẫn tới **quyết định sai** — trung tâm mở thêm lớp trong khi thực ra đang thừa chỗ, hoặc ngược lại.

Điều đáng lưu ý về mặt quản trị là **chi phí của chuỗi này tăng dần theo từng mắt xích**. Ở mắt xích đầu, dư thừa chỉ tốn ít dung lượng đĩa, gần như miễn phí. Ở mắt xích cuối, một quyết định kinh doanh sai có thể tốn hàng trăm triệu đồng. Nhưng vì tổn thất chỉ bộc lộ ở cuối chuỗi, người ta thường không truy ngược về nguyên nhân gốc, và tiếp tục sống chung với thiết kế tồi.

Đây chính là lý do sâu xa để học phần này tồn tại: **chặn chuỗi nhân quả ngay tại mắt xích đầu tiên, bằng cách thiết kế cơ sở dữ liệu sao cho không có dư thừa ngay từ đầu.**

## 1.3.4. Cách tiếp cận cơ sở dữ liệu khắc phục ra sao

Cách tiếp cận cơ sở dữ liệu giải quyết bốn hạn chế trên bằng hai thay đổi căn bản: **gộp dữ liệu vào một kho dùng chung** và **đặt một phần mềm trung gian kiểm soát mọi truy cập**.

**Bảng 1.6. So sánh hệ thống tệp và cách tiếp cận cơ sở dữ liệu**

| Tiêu chí | Hệ thống tệp | Cách tiếp cận cơ sở dữ liệu |
|---|---|---|
| **Tổ chức dữ liệu** | Mỗi bộ phận một tệp riêng | Một kho dùng chung |
| **Dư thừa** | Cao — dữ liệu lặp ở nhiều tệp | Được kiểm soát, giảm tới mức tối thiểu |
| **Nhất quán** | Khó bảo đảm, phải làm thủ công | Do hệ quản trị bảo đảm tự động |
| **Metadata** | Không có, hoặc chỉ nằm trong đầu người viết chương trình | Lưu ngay trong cơ sở dữ liệu, máy đọc được |
| **Phụ thuộc dữ liệu** | Chương trình gắn chặt với cấu trúc tệp | Được tách rời nhờ kiến trúc ba mức *(mục 1.5)* |
| **Nhiều người truy cập đồng thời** | Không kiểm soát được | Do hệ quản trị điều phối |
| **Phân quyền, an toàn** | Ở mức tệp — cho phép hoặc cấm cả tệp | Chi tiết tới từng bảng, từng cột |
| **Truy vấn tùy ý** | Phải viết chương trình mới | Dùng ngôn ngữ truy vấn có sẵn |

Tuy vậy, cần giữ một cái nhìn cân bằng. Cách tiếp cận cơ sở dữ liệu cũng có **cái giá** của nó: chi phí mua bản quyền hoặc hạ tầng máy chủ, yêu cầu nhân sự có chuyên môn để quản trị, và độ phức tạp cao hơn hẳn khi bắt đầu. Với một cửa hàng nhỏ ghi chép mười khách hàng, dùng bảng tính vẫn là lựa chọn hợp lý. **Cơ sở dữ liệu trở nên đáng giá khi dữ liệu được dùng chung bởi nhiều người, khi tính đúng đắn là bắt buộc, và khi hệ thống còn phải sống lâu dài.** Ba điều kiện ấy đúng với hầu hết hệ thống nghiệp vụ thực tế.

---


---

[← Trang trước](1-2-he-quan-tri-co-so-du-lieu.md) · [Trang sau →](1-4-mo-hinh-du-lieu-luoc-do-va-the-hien.md)
