# Bài tập Chương 1

## Mức A — Nhận biết và tái hiện

**Bài A1.** Với mỗi tình huống sau, cho biết đó là *dữ liệu* hay *thông tin*, và giải thích: (a) dãy số `28, 31, 30, 29`; (b) câu "nhiệt độ trung bình tháng này là 29,5 °C"; (c) ô ghi `0905111111` trong một bảng; (d) câu "80% học viên lớp tối đi học đầy đủ".


??? success "Lời giải bài A1"

    Tiêu chí phân biệt là **có ngữ cảnh và đã qua xử lý hay chưa**.

    | Tình huống | Là gì | Vì sao |
    |---|---|---|
    | (a) `28, 31, 30, 29` | **Dữ liệu** | Bốn con số trần, chưa biết là nhiệt độ, số ngày trong tháng hay sĩ số lớp. Chưa có ngữ cảnh nên chưa nói lên điều gì. |
    | (b) "nhiệt độ trung bình tháng này là 29,5 °C" | **Thông tin** | Có đủ ba yếu tố: dữ liệu là các số đo, ngữ cảnh là *nhiệt độ trong tháng này*, xử lý là *lấy trung bình*. |
    | (c) ô ghi `0905111111` | **Dữ liệu** | Tự thân dãy số chưa nói của ai, cũng chưa chắc là số điện thoại. Chỉ khi biết nó nằm ở cột `SDT` của dòng học viên Trần An thì mới thành thông tin. |
    | (d) "80% học viên lớp tối đi học đầy đủ" | **Thông tin** | Dữ liệu là các bản ghi điểm danh, xử lý là *đếm rồi chia*, ngữ cảnh là *lớp tối*. Kết quả dùng được để ra quyết định. |

    Điểm cần rút ra: ranh giới không nằm ở **hình thức** của con số mà nằm ở chỗ đã gắn
    ngữ cảnh và đã xử lý hay chưa. Cùng dãy `28, 31, 30, 29`, nếu nói thêm "đây là số
    ngày của bốn tháng liên tiếp" thì nó đã thành thông tin.

**Bài A2.** Chọn một bảng dữ liệu quen thuộc trong đời sống của bạn — danh bạ điện thoại, bảng điểm cá nhân, sổ chi tiêu. Lập **bảng metadata** cho bảng đó theo mẫu Bảng 1.5, gồm bốn cột: tên cột, kiểu dữ liệu, bắt buộc hay không, ràng buộc.


??? success "Lời giải bài A2"

    Bài này không có một đáp án duy nhất; dưới đây là một bài làm đạt yêu cầu, lấy ví dụ
    **sổ chi tiêu cá nhân**.

    | Tên cột | Kiểu dữ liệu | Bắt buộc | Ràng buộc |
    |---|---|:--:|---|
    | `MACHI` | Chuỗi, 8 ký tự | Có | Duy nhất, dạng `CHI` + 5 chữ số |
    | `NGAYCHI` | Ngày | Có | Không được lớn hơn ngày hiện tại |
    | `KHOANMUC` | Chuỗi, 30 ký tự | Có | Chỉ nhận: ăn uống, đi lại, học tập, giải trí, khác |
    | `SOTIEN` | Số nguyên | Có | Lớn hơn 0 |
    | `PHUONGTHUC` | Chuỗi, 20 ký tự | Không | Chỉ nhận: tiền mặt, chuyển khoản, thẻ |
    | `GHICHU` | Chuỗi, 200 ký tự | Không | — |

    Bài làm được chấm theo bốn điểm: (1) có đủ bốn cột của mẫu; (2) kiểu dữ liệu hợp lý,
    đặc biệt **`SOTIEN` phải là số chứ không phải chuỗi** — nếu là chuỗi thì không cộng
    được; (3) cột nào bắt buộc, cột nào không, có lập luận; (4) ràng buộc phải **kiểm tra
    được bằng máy**, viết "số tiền phải hợp lý" là chưa đạt vì máy không hiểu.

    Lưu ý bảng trên chính là **metadata** của sổ chi tiêu. Nó mô tả dữ liệu chứ không phải
    là dữ liệu — trong sổ không có dòng nào tên là "Chuỗi, 8 ký tự".

**Bài A3.** Lập bảng đối chiếu hai cột giữa hệ thống tệp và cách tiếp cận cơ sở dữ liệu, theo **năm tiêu chí** do bạn tự chọn trong Bảng 1.12.


??? success "Lời giải bài A3"

    Năm tiêu chí tự chọn; dưới đây là một phương án.

    | Tiêu chí | Hệ thống tệp | Cách tiếp cận cơ sở dữ liệu |
    |---|---|---|
    | **Dư thừa dữ liệu** | Cao — mỗi bộ phận giữ một bản riêng của cùng một sự thật | Thấp — dữ liệu lưu tập trung, dùng chung |
    | **Tính nhất quán** | Khó bảo đảm — sửa một nơi, các nơi khác vẫn giữ giá trị cũ | Được hệ quản trị bảo vệ bằng ràng buộc |
    | **Quan hệ giữa chương trình và dữ liệu** | Phụ thuộc — đổi cấu trúc tệp là phải sửa và biên dịch lại chương trình | Độc lập — kiến trúc ba mức che cấu trúc lưu trữ khỏi ứng dụng |
    | **Chia sẻ đồng thời** | Rất hạn chế — hai người cùng ghi thì dễ hỏng tệp | Có cơ chế giao dịch và khóa, nhiều người dùng cùng lúc |
    | **Kiểm soát truy cập** | Chỉ ở mức quyền của tệp, không phân biệt được từng cột | Phân quyền tới từng bảng, từng cột, từng thao tác |

    Có thể chọn tiêu chí khác — sao lưu và phục hồi, chuẩn hóa kiểu dữ liệu, khả năng
    truy vấn — miễn là mỗi dòng nêu được **sự khác biệt thật**, không phải khen chê chung
    chung kiểu "cơ sở dữ liệu hiện đại hơn".

## Mức B — Vận dụng

**Bài B1.** Cho bảng phẳng sau của một hiệu sách:

| MADH | TENKH | SDT_KH | MASACH | TENSACH | GIA | SOLUONG |
|---|---|---|---|---|---|---|
| DH01 | Trần An | 0905111 | S01 | Lập trình C | 120000 | 2 |
| DH02 | Trần An | 0905111 | S02 | Cơ sở dữ liệu | 150000 | 1 |
| DH03 | Lê Bình | 0905222 | S01 | Lập trình C | 120000 | 3 |

a) Đếm số ô dư thừa và tính tỷ lệ phần trăm.
b) Chỉ ra **ba dị thường** thêm, sửa, xóa bằng ba tình huống cụ thể.
c) Đề xuất cách **tách bảng** và vẽ sơ đồ tương tự Hình 1.11.


??? success "Lời giải bài B1"

    ### (a) Đếm ô dư thừa

    Bảng có 3 dòng × 7 cột = **21 ô**.

    Dữ liệu lặp lại một cách không cần thiết:

    - Khách **Trần An** xuất hiện ở hai đơn `DH01` và `DH02`, nên `TENKH` và `SDT_KH` mỗi
      cái bị lặp thừa **1 ô** → 2 ô.
    - Sách **S01 — Lập trình C** xuất hiện ở hai đơn `DH01` và `DH03`, nên `TENSACH` và
      `GIA` mỗi cái lặp thừa **1 ô** → 2 ô.

    Tổng **4 ô dư thừa / 21 ô ≈ 19%**.

    Cách đếm: với mỗi nhóm giá trị lặp, số ô thừa bằng *(số lần xuất hiện − 1)* nhân với
    *số cột phụ thuộc*. Ở đây mỗi nhóm xuất hiện 2 lần và có 2 cột phụ thuộc, nên
    `(2 − 1) × 2 = 2` ô cho mỗi nhóm.

    ### (b) Ba dị thường

    **Dị thường thêm.** Hiệu sách vừa nhập cuốn *Trí tuệ nhân tạo* mã `S03`, giá 200.000,
    nhưng chưa ai mua. Không có cách nào lưu cuốn sách này vào bảng, vì mọi dòng đều đòi
    phải có `MADH`. Muốn lưu thì phải bịa ra một đơn hàng giả — tức là làm bẩn dữ liệu để
    lách cấu trúc. Tương tự với một khách hàng mới đăng ký nhưng chưa đặt đơn nào.

    **Dị thường sửa.** Trần An đổi số điện thoại thành `0905999`. Số này nằm ở **hai
    dòng** `DH01` và `DH02`, nên phải sửa cả hai. Sửa sót một dòng thì cùng một khách hàng
    có hai số điện thoại khác nhau trong cùng một bảng, và không có cách nào biết số nào
    đúng. Đây đúng là chuỗi **dư thừa → không nhất quán**.

    **Dị thường xóa.** Khách hủy đơn `DH02`. Xóa dòng ấy đi thì hiệu sách **mất luôn**
    thông tin cuốn *Cơ sở dữ liệu* mã `S02` giá 150.000, vì đó là dòng duy nhất còn nhắc
    tới cuốn sách này. Xóa một đơn hàng lại làm mất một cuốn sách — hai sự vật khác nhau
    bị buộc chung số phận chỉ vì nằm chung một bảng.

    ### (c) Tách bảng

    Nguyên tắc: **mỗi loại sự vật một bảng**. Bảng phẳng đang trộn ba loại — khách hàng,
    sách, và đơn hàng.

    ```text
    KHACHHANG(MAKH, TENKH, SDT_KH)
    SACH(MASACH, TENSACH, GIA)
    DONHANG(MADH, MAKH, MASACH, SOLUONG)
    ```

    Sơ đồ liên kết, đọc theo chiều mũi tên là "một bên trái ứng với nhiều bên phải":

    ```text
    KHACHHANG ──1───∞── DONHANG ──∞───1── SACH
       MAKH                MADH             MASACH
    ```

    Ba nhận xét quan trọng:

    1. **Phải sinh thêm `MAKH`.** Bảng phẳng không có mã khách hàng, chỉ có tên. Dùng tên
       làm định danh thì hai người trùng tên sẽ bị nhập làm một. Đây là lần đầu gặp nhu
       cầu *đặt định danh nhân tạo*, và Chương 2 sẽ gọi nó là **khóa thay thế**.
    2. Sau khi tách, mỗi sự thật chỉ nằm **đúng một chỗ**: số điện thoại của Trần An chỉ
       có ở một dòng của `KHACHHANG`, giá sách chỉ có ở một dòng của `SACH`. Cả ba dị
       thường ở câu (b) đều biến mất.
    3. Cách tách này đang giả định **mỗi đơn hàng chỉ mua một cuốn sách**, đúng với dữ
       liệu đang có. Nếu nghiệp vụ cho phép một đơn mua nhiều cuốn thì phải tách tiếp:

        ```text
        DONHANG(MADH, MAKH, NGAYDAT)
        CHITIETDONHANG(MADH, MASACH, SOLUONG)
        ```

        Chương 2 sẽ cho một phương pháp để nhận ra điều này ngay từ đề bài, thay vì đoán.

**Bài B2.** Một trường đại học có phần mềm quản lý điểm đã chạy được tám năm. Nay nhà trường muốn bổ sung cột "điểm rèn luyện" vào hồ sơ sinh viên.
a) Nếu hệ thống được xây bằng **tệp**, hãy liệt kê những việc phải làm và những rủi ro có thể gặp.
b) Nếu hệ thống dùng **cơ sở dữ liệu có kiến trúc ba mức**, việc gì phải làm và vì sao ít rủi ro hơn?
c) Tính chất nào trong mục 1.5.3 được vận dụng ở câu (b)?


??? success "Lời giải bài B2"

    ### (a) Nếu hệ thống xây bằng tệp

    Những việc phải làm:

    1. Sửa **định nghĩa cấu trúc bản ghi** trong mã nguồn — thêm trường điểm rèn luyện.
    2. Tìm **mọi chương trình** có đọc hoặc ghi tệp hồ sơ sinh viên, sửa hết rồi biên dịch
       lại. Sau tám năm, số chương trình này thường không ai còn nhớ hết.
    3. Viết một chương trình **chuyển đổi** để đọc tệp cũ và ghi ra tệp mới theo cấu trúc
       mới, chạy trên toàn bộ dữ liệu lịch sử.
    4. Ngừng hệ thống trong lúc chuyển đổi, và chuẩn bị phương án quay lui.

    Rủi ro:

    - **Sót chương trình.** Một chương trình cũ chưa sửa vẫn đọc theo cấu trúc cũ, nên
      đọc lệch vị trí byte và trả ra dữ liệu rác — mà không báo lỗi gì. Đây là kiểu hỏng
      nguy hiểm nhất vì nó im lặng.
    - Chuyển đổi hỏng giữa chừng, dữ liệu ở trạng thái nửa cũ nửa mới.
    - Bản sao lưu cũ không còn khôi phục được vào hệ thống mới.
    - Chi phí kiểm thử lại toàn bộ, dù thay đổi nghiệp vụ chỉ là **thêm một cột**.

    Gốc rễ của mọi rủi ro trên là **phụ thuộc dữ liệu**: chương trình gắn chặt với cấu
    trúc vật lý của tệp.

    ### (b) Nếu dùng cơ sở dữ liệu có kiến trúc ba mức

    Việc phải làm: khai báo thêm một cột ở **mức quan niệm**. Chỉ một thao tác.

    Vì sao ít rủi ro hơn:

    - Các ứng dụng cũ làm việc qua **khung nhìn ở mức ngoài**. Khung nhìn cũ không nhắc
      tới cột mới nên chúng không nhìn thấy cột mới, và **không cần sửa dòng mã nào**.
    - Hệ quản trị tự lo phần lưu trữ vật lý ở **mức trong** — không ai phải viết chương
      trình chuyển đổi tệp.
    - Cột mới để rỗng cho các bản ghi cũ, hệ thống vẫn chạy bình thường trong lúc phòng
      đào tạo nhập dần dữ liệu.
    - Chỉ ứng dụng nào **thật sự cần** điểm rèn luyện mới phải sửa, và đó là sửa để dùng
      tính năng mới chứ không phải sửa để khỏi hỏng.

    ### (c) Tính chất được vận dụng

    **Độc lập dữ liệu logic** — khả năng thay đổi mô tả ở mức quan niệm mà không phải sửa
    mô tả ở mức ngoài. Đây đúng là tình huống mẫu của khái niệm này: thêm một cột ở mức
    quan niệm, các khung nhìn ở mức ngoài không đổi.

**Bài B3.** Với mỗi thay đổi sau, cho biết nó xảy ra ở **mức nào** của kiến trúc ANSI/SPARC, và loại **độc lập dữ liệu** nào giúp hạn chế ảnh hưởng: (a) tạo thêm chỉ mục trên cột họ tên; (b) thêm một cột mới vào bảng; (c) tạo một khung nhìn mới cho phòng công tác sinh viên; (d) chuyển toàn bộ dữ liệu sang ổ đĩa mới.


??? success "Lời giải bài B3"

    | Thay đổi | Xảy ra ở mức | Loại độc lập dữ liệu giúp hạn chế ảnh hưởng |
    |---|---|---|
    | (a) Tạo thêm chỉ mục trên cột họ tên | **Mức trong** | **Độc lập vật lý** — chỉ mục là chuyện cách lưu trên đĩa; mức quan niệm không đổi nên không ứng dụng nào phải sửa |
    | (b) Thêm một cột mới vào bảng | **Mức quan niệm** | **Độc lập logic** — các khung nhìn cũ không tham chiếu cột mới nên vẫn chạy nguyên |
    | (c) Tạo khung nhìn mới cho phòng công tác sinh viên | **Mức ngoài** | Không cần loại nào — đây là **thêm mới**, không sửa cái đang có. Việc thêm được bao nhiêu khung nhìn tùy ý chính là công dụng của mức ngoài |
    | (d) Chuyển toàn bộ dữ liệu sang ổ đĩa mới | **Mức trong** | **Độc lập vật lý** — đổi thiết bị lưu trữ mà mô tả logic giữ nguyên |

    Mẹo phân loại nhanh: hỏi *"thay đổi này nói về **cách lưu** hay về **có gì**?"*. Nói
    về cách lưu thì ở mức trong, cần độc lập vật lý. Nói về có những dữ liệu gì thì ở mức
    quan niệm, cần độc lập logic. Nói về **ai nhìn thấy phần nào** thì ở mức ngoài.

## Mức C — Nâng cao

**Bài C1.** Có ý kiến cho rằng: *"Dư thừa dữ liệu ngày nay không còn là vấn đề, vì dung lượng lưu trữ rất rẻ."* Hãy phản biện ý kiến này bằng lập luận dựa trên mục 1.3.3, có kèm ví dụ cụ thể.


??? success "Lời giải bài C1"

    Ý kiến này đúng ở **một vế nhỏ** rồi kết luận sai cho toàn bộ vấn đề.

    **Vế đúng.** Chi phí lưu trữ quả thật đã rẻ đi rất nhiều. Nếu dư thừa chỉ gây tốn chỗ
    thì lập luận trên có lý.

    **Chỗ sai.** Mục 1.3.3 chỉ ra rằng tốn chỗ **không phải** là tác hại chính. Chuỗi nhân
    quả thật sự là:

    > Dư thừa → cập nhật phải sửa nhiều nơi → sót một nơi → **không nhất quán** → **dị
    > thường thêm, sửa, xóa**

    Mắt xích gây thiệt hại nằm ở cuối chuỗi, và **không mắt xích nào rẻ đi khi ổ đĩa rẻ
    đi**. Ổ cứng rẻ không làm cho việc sửa sót một dòng bớt sai.

    **Ví dụ cụ thể.** Một ngân hàng lưu địa chỉ khách hàng ở ba nơi: hồ sơ mở tài khoản,
    hồ sơ vay, và hệ thống gửi sao kê. Khách chuyển nhà, giao dịch viên cập nhật ở hai nơi
    đầu và quên nơi thứ ba. Hệ quả: sao kê hằng tháng vẫn gửi về địa chỉ cũ suốt một năm,
    thư đòi nợ tới tay người chủ nhà mới, ngân hàng bị khiếu nại. Thiệt hại ở đây là uy
    tín và pháp lý — vài kilobyte tiết kiệm được không mua lại được.

    **Ba tác hại nữa mà tiền mua ổ đĩa không giải quyết:**

    1. **Không còn nguồn sự thật duy nhất.** Khi hai chỗ ghi khác nhau, không có cách nào
       biết chỗ nào đúng nếu không đi hỏi lại khách hàng.
    2. **Ghi chậm hơn và dễ hỏng hơn.** Mỗi lần cập nhật phải ghi nhiều nơi, giữ nhiều
       khóa, và cơ hội hỏng giữa chừng tăng theo số nơi phải ghi.
    3. **Chi phí đối soát.** Nhiều tổ chức phải nuôi hẳn quy trình định kỳ dò tìm mâu
       thuẫn giữa các bản sao. Chi phí con người ấy lớn hơn chi phí đĩa nhiều lần.

    **Kết luận.** Chuẩn hóa không nhằm tiết kiệm dung lượng — nó nhằm **bảo đảm mỗi sự
    thật chỉ được ghi ở đúng một chỗ**, để không bao giờ có hai câu trả lời cho cùng một
    câu hỏi. Có điều cần nói thêm cho công bằng: dư thừa **có chủ đích và có kiểm soát**
    vẫn hợp lý ở một số hệ thống — xem bài C2.

**Bài C2.** Một trung tâm thương mại điện tử lưu lịch sử đơn hàng của mười năm để phân tích xu hướng mua sắm. Theo phân loại ở mục 1.2.3, hệ thống này thuộc loại nào? Vì sao đối với hệ thống loại này, người ta đôi khi **cố ý** chấp nhận dư thừa dữ liệu?


??? success "Lời giải bài C2"

    **Hệ thống này thuộc loại nào.** Theo tiêu chí **mục đích sử dụng** ở Bảng 1.4, đây là
    **kho dữ liệu** phục vụ phân tích, chứ không phải hệ xử lý giao dịch trực tuyến. Dấu
    hiệu nhận biết nằm ngay trong đề: lưu **lịch sử mười năm** để **phân tích xu hướng** —
    tức là đọc rất nhiều, tổng hợp trên khối lượng lớn, gần như không sửa dữ liệu cũ.

    Xét theo hai tiêu chí còn lại thì đây cũng là hệ **nhiều người dùng** cấp doanh
    nghiệp, và với quy mô thương mại điện tử thì thường là **phân tán**.

    **Vì sao cố ý chấp nhận dư thừa.** Hai lý do, và lý do thứ hai mới là điều kiện khiến
    đánh đổi này hợp lệ:

    1. **Truy vấn phân tích quá đắt nếu dữ liệu tách quá nhỏ.** Một câu hỏi kiểu "doanh
       thu theo tháng, theo nhóm hàng, theo tỉnh, trong mười năm" phải ghép hàng chục
       bảng trên hàng trăm triệu dòng. Gộp sẵn vài cột hay lưu sẵn số liệu tổng hợp giúp
       câu hỏi ấy chạy trong vài giây thay vì vài giờ.

    2. **Nguy cơ không nhất quán gần như bằng không, vì dữ liệu không còn thay đổi.** Đây
       là điểm mấu chốt. Đơn hàng của năm ngoái đã chốt, không ai sửa nữa. Mà chuỗi nhân
       quả ở mục 1.3.3 khởi động từ **thao tác cập nhật**: dư thừa chỉ nguy hiểm khi có
       sửa đổi. Không sửa thì mắt xích đầu tiên không bao giờ được kích hoạt.

    **Điều cần nhớ.** Đây không phải ngoại lệ tùy tiện mà là một đánh đổi có điều kiện:
    *chấp nhận dư thừa để đổi lấy tốc độ đọc, chỉ khi dữ liệu hầu như không còn được cập
    nhật*. Áp đúng công thức ấy vào hệ thống ghi danh hằng ngày của Trung tâm ABC thì hỏng
    ngay, vì ở đó dữ liệu thay đổi liên tục. Chương 5 sẽ gọi tên kỹ thuật này là **phi
    chuẩn hóa** và trình bày điều kiện áp dụng chặt chẽ hơn.

**Bài C3** *(tự chọn).* Tìm hiểu thêm về **mười hai quy tắc của Codd** [3, Chapter 3]. Chọn ba quy tắc bạn thấy thú vị nhất, giải thích bằng lời của mình và cho một ví dụ minh họa cho mỗi quy tắc.

---


??? success "Lời giải bài C3"

    Bài tự chọn, không có đáp án cố định. Dưới đây là ba quy tắc thường được chọn, kèm mức
    diễn giải được coi là đạt.

    **Quy tắc 1 — Quy tắc thông tin.** Mọi thông tin trong cơ sở dữ liệu quan hệ phải được
    biểu diễn **duy nhất bằng giá trị trong các ô của bảng**. Nghĩa là không được giấu
    thông tin ở chỗ khác — chẳng hạn ở thứ tự các dòng, hay ở tên tệp. *Ví dụ:* nếu hệ
    thống ngầm quy ước "dòng đầu tiên của bảng là trưởng nhóm" thì đã vi phạm, vì thông
    tin *ai là trưởng nhóm* nằm ở vị trí dòng chứ không nằm trong một ô. Cách làm đúng là
    thêm hẳn một cột `VAITRO`.

    **Quy tắc 3 — Xử lý giá trị rỗng có hệ thống.** Hệ quản trị phải hỗ trợ giá trị rỗng
    để biểu diễn *chưa biết* hoặc *không áp dụng*, và phải xử lý nhất quán, độc lập với
    kiểu dữ liệu. *Ví dụ:* học viên chưa khai email thì cột `EMAIL` để rỗng — khác hẳn với
    việc điền chuỗi trống hay điền chữ "không có". Nếu dùng chuỗi trống thay cho rỗng thì
    câu hỏi "bao nhiêu học viên chưa khai email" sẽ đếm sai.

    **Quy tắc 12 — Chống lách luật.** Nếu hệ quản trị có giao diện mức thấp để truy cập
    trực tiếp dữ liệu, giao diện ấy **không được dùng để lách các ràng buộc** đã khai báo
    ở mức cao. *Ví dụ:* không thể dùng một công cụ ghi thẳng vào tệp để chèn một dòng học
    viên trùng mã, trong khi ràng buộc khóa chính đang cấm điều đó. Quy tắc này là thứ bảo
    đảm cho toàn bộ Chương 4 có ý nghĩa: đặt ràng buộc ở tầng cơ sở dữ liệu chỉ đáng tin
    khi không ai đi vòng qua được nó.

    Bài làm đạt yêu cầu cần: chọn đúng ba quy tắc trong mười hai, **diễn giải bằng lời của
    mình** chứ không chép nguyên văn, và mỗi quy tắc có một ví dụ **cụ thể, kiểm chứng
    được** — tốt nhất là ví dụ lấy từ một hệ thống bạn từng dùng.
