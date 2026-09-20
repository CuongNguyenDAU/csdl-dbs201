# Bài tập Chương 2

## Mức A — Nhận biết và tái hiện

**Bài A1.** Với mỗi phát biểu sau, cho biết nó tương ứng với thành phần nào của lược đồ ER *(thực thể, thuộc tính, liên kết, kết nối, tham gia, thuộc tính đa trị)*: (a) *"mỗi cuốn sách có một tên và một năm xuất bản"*; (b) *"độc giả mượn sách"*; (c) *"một độc giả có thể mượn nhiều cuốn cùng lúc"*; (d) *"độc giả có thể chưa mượn cuốn nào"*; (e) *"mỗi tác giả có thể có nhiều bút danh"*.


??? success "Lời giải bài A1"

    | Phát biểu | Thành phần ER | Vì sao |
    |---|---|---|
    | (a) *mỗi cuốn sách có một tên và một năm xuất bản* | **Thuộc tính** | Hai danh từ *tên*, *năm xuất bản* là **đặc điểm** của sách, không phải sự vật độc lập |
    | (b) *độc giả mượn sách* | **Liên kết** | Động từ **mượn** nối hai danh từ chỉ sự vật |
    | (c) *một độc giả có thể mượn nhiều cuốn cùng lúc* | **Kết nối** | Từ chỉ số lượng **nhiều** cho biết loại liên kết ở chiều này |
    | (d) *độc giả có thể chưa mượn cuốn nào* | **Tham gia tùy chọn** | Cụm **có thể chưa** báo hiệu `min = 0` |
    | (e) *mỗi tác giả có thể có nhiều bút danh* | **Thuộc tính đa trị** | Chữ **nhiều** đứng trước một **đặc điểm** của tác giả, không phải trước một sự vật |

    Điểm dễ nhầm là (c) và (e): cả hai đều có chữ *nhiều*, nhưng (c) nói về số lượng **sự vật** ở đầu kia của liên kết, còn (e) nói về số lượng **giá trị** của một đặc điểm. Mẹo phân biệt: hỏi *"nhiều cái gì?"* — nhiều **cuốn sách** là sự vật nên ra kết nối; nhiều **bút danh** là đặc điểm của tác giả nên ra thuộc tính đa trị.

**Bài A2.** Phân loại các thuộc tính sau theo **cả bốn cặp tiêu chí** ở Bảng 2.3: `HOTEN`, `DIACHI`, `NGAYSINH`, `TUOI`, `SODIENTHOAI` *(một người có nhiều số)*, `EMAIL` *(có thể không có)*.


??? success "Lời giải bài A2"

    Mỗi thuộc tính mang **bốn nhãn cùng lúc**, mỗi cặp tiêu chí một nhãn.

    | Thuộc tính | Cấu trúc | Số giá trị | Nguồn gốc | Bắt buộc |
    |---|---|---|---|---|
    | `HOTEN` | Đơn *(hoặc phức hợp nếu tách họ / tên lót / tên)* | Đơn trị | Lưu trữ | Bắt buộc |
    | `DIACHI` | **Phức hợp** — số nhà, đường, quận, tỉnh | Đơn trị | Lưu trữ | Thường tùy chọn |
    | `NGAYSINH` | Đơn | Đơn trị | Lưu trữ | Bắt buộc |
    | `TUOI` | Đơn | Đơn trị | **Dẫn xuất** — tính từ `NGAYSINH` | Bắt buộc *(vì suy ra được)* |
    | `SODIENTHOAI` | Đơn | **Đa trị** | Lưu trữ | Thường tùy chọn |
    | `EMAIL` | Đơn | Đơn trị | Lưu trữ | **Tùy chọn** |

    Hai hệ quả thiết kế rút ra ngay:

    - `SODIENTHOAI` **bắt buộc phải tách** thành thực thể riêng — đây là ca duy nhất trong bảng không cho phép lựa chọn.
    - `TUOI` **không nên lưu**, vì lưu lại là tạo dư thừa và số liệu sai ngay sau sinh nhật. Vẫn vẽ nó ra trong lược đồ Chen bằng oval nét đứt để ghi nhận nhu cầu nghiệp vụ.

    `HOTEN` có thể xếp vào *đơn* hay *phức hợp* tùy nghiệp vụ: nếu cần sắp xếp danh sách theo tên riêng thì phải tách, nếu chỉ in ra thì để nguyên. Bài làm nêu được lý do là đạt.

**Bài A3.** Vẽ lại Hình 2.21 *(quy trình năm bước)* từ trí nhớ, và với mỗi bước nêu **một sai lầm thường gặp**.


??? success "Lời giải bài A3"

    Quy trình năm bước và sai lầm thường gặp ở từng bước:

    | Bước | Nội dung | Sai lầm thường gặp |
    |:--:|---|---|
    | **1** | Xác định thực thể — gạch chân danh từ | Biến **mọi** danh từ thành thực thể, kể cả danh từ chỉ có một đặc điểm hoặc chỉ có một cá thể |
    | **2** | Xác định thuộc tính và thuộc tính khóa | **Tách luôn thuộc tính đa trị tại chỗ** thay vì chỉ đánh dấu — làm rối và bỏ sót |
    | **3** | Xác định liên kết bằng hỏi hai chiều | Chỉ hỏi **một chiều** rồi kết luận; bỏ quên tính tham gia của từng chiều |
    | **4** | Xử lý ca đặc biệt | Quên **đặt tên khác nhau cho hai cột** của liên kết đệ quy M:N |
    | **5** | Vẽ và kiểm tra | Chỉ vẽ cho đẹp mà **không đối chiếu ngược** từng quy tắc nghiệp vụ với lược đồ |

    Mũi tên nét đứt quay từ Bước 5 về Bước 1 không phải trang trí: thiết kế là quá trình **lặp**, và người có kinh nghiệm coi việc lặp hai đến ba vòng là bình thường. Sai lầm ngầm thứ sáu là tưởng làm một lượt là xong rồi nản khi phải quay lại.

## Mức B — Vận dụng

**Bài B1.** Một **thư viện** hoạt động theo các quy tắc sau:

1. Mỗi **đầu sách** có mã, tên sách, năm xuất bản, và **nhiều tác giả**.
2. Thư viện có **nhiều bản sao** của mỗi đầu sách; mỗi bản sao có số hiệu riêng và tình trạng.
3. Mỗi **độc giả** có mã thẻ, họ tên, ngày sinh.
4. Một độc giả **mượn nhiều** bản sao; một bản sao được **nhiều** độc giả mượn qua các lần khác nhau. Mỗi lượt mượn ghi nhận **ngày mượn** và **ngày hẹn trả**.
5. Mỗi đầu sách thuộc **một thể loại**; một thể loại có **nhiều** đầu sách.

Yêu cầu: (a) lập **bảng hỏi hai chiều** cho mọi cặp thực thể; (b) chỉ ra các **ca đặc biệt** phải xử lý ở Bước 4; (c) vẽ **lược đồ ER hoàn chỉnh**; (d) **đối chiếu ngược** từng quy tắc với lược đồ.


??? success "Lời giải bài B1"

    ### (a) Bảng hỏi hai chiều

    Bốn thực thể ban đầu: `DAUSACH`, `BANSAO`, `DOCGIA`, `THELOAI`.

    | Cặp thực thể | Chiều thứ nhất | Chiều thứ hai | Kết luận |
    |---|---|---|:--:|
    | `THELOAI` – `DAUSACH` | Một thể loại có bao nhiêu đầu sách? **Nhiều** | Một đầu sách thuộc bao nhiêu thể loại? **Một** | **1:M** |
    | `DAUSACH` – `BANSAO` | Một đầu sách có bao nhiêu bản sao? **Nhiều** | Một bản sao thuộc bao nhiêu đầu sách? **Một** | **1:M** |
    | `DAUSACH` – tác giả | Một đầu sách có bao nhiêu tác giả? **Nhiều** | Một tác giả viết bao nhiêu đầu sách? **Nhiều** | **M:N** |
    | `DOCGIA` – `BANSAO` | Một độc giả mượn bao nhiêu bản sao? **Nhiều** | Một bản sao được bao nhiêu độc giả mượn? **Nhiều** | **M:N** |

    Dòng thứ ba cần một bước suy nghĩ: đề chỉ nói *"mỗi đầu sách có nhiều tác giả"*, tức là mới cho một chiều. Người thiết kế **phải hỏi lại chiều kia** — một tác giả có viết nhiều đầu sách không. Câu trả lời hợp lý với thư viện là có, nên kết luận M:N. Nếu thư viện chỉ cần lưu tên tác giả dưới dạng chuỗi thì đây chỉ là **thuộc tính đa trị**, và lược đồ sẽ khác — đây là chỗ phải hỏi khách hàng chứ không tự quyết.

    ### (b) Các ca đặc biệt phải xử lý ở Bước 4

    | Ca | Xuất phát từ | Cách xử lý |
    |---|---|---|
    | **Thuộc tính đa trị** | *nhiều tác giả* của một đầu sách | Tách thành thực thể `TACGIA`, nối M:N *(hoặc thực thể yếu nếu chỉ lưu tên)* |
    | **Liên kết M:N có thuộc tính** | *mỗi lượt mượn có ngày mượn và ngày hẹn trả* | Tách thành thực thể kết hợp `MUON` |
    | **Liên kết M:N không thuộc tính** | đầu sách ↔ tác giả | Vẫn phải tách thành `VIET(MADS, MATG)` |

    Ca thứ hai là ca nặng nhất: `NGAYMUON` không thuộc `DOCGIA` (cùng người mượn nhiều lần, nhiều ngày khác nhau) cũng không thuộc `BANSAO` (cùng cuốn được mượn nhiều lần), nên nó thuộc về **lượt mượn** — một sự vật chưa được đặt tên. Áp **phép thử tờ phiếu**: mỗi lần cho mượn, thư viện có ghi một phiếu mượn — tờ phiếu ấy chính là thực thể.

    ### (c) Lược đồ ER hoàn chỉnh

    Sau Bước 4, mọi liên kết còn lại đều là 1:M:

    ```text
    THELOAI(MATL, TENTL)
    DAUSACH(MADS, TENSACH, NAMXB, MATL)
    TACGIA(MATG, HOTEN_TG)
    VIET(MADS, MATG)                                  ← tách M:N đầu sách ↔ tác giả
    BANSAO(MABS, TINHTRANG, MADS)
    DOCGIA(MADG, HOTEN, NGAYSINH)
    MUON(MADG, MABS, NGAYMUON, NGAYHENTRA)            ← thực thể kết hợp
    ```

    Sơ đồ liên kết, đọc theo chiều mũi tên là *"một bên trái ứng với nhiều bên phải"*:

    ```text
    THELOAI ──1──∞── DAUSACH ──1──∞── BANSAO ──1──∞── MUON ──∞──1── DOCGIA
                        │
                        1
                        │
                        ∞
                      VIET ──∞──1── TACGIA
    ```

    Bốn thực thể ban đầu đã thành **bảy**. Ba thực thể mới — `TACGIA`, `VIET`, `MUON` — đều không lộ ra dưới dạng danh từ khi đọc lướt đề bài.

    !!! warning "Chú ý về khóa của `MUON`"

        Khóa `(MADG, MABS)` chỉ đúng nếu **một độc giả không mượn lại cùng một bản sao lần thứ hai**. Đề nói *"qua các lần khác nhau"*, nên nghiêm ngặt thì phải thêm `NGAYMUON` vào khóa: `(MADG, MABS, NGAYMUON)`. Đây chính là loại chi tiết mà Bước 5 — đối chiếu ngược — sẽ phát hiện ra.

    ### (d) Đối chiếu ngược từng quy tắc

    | Quy tắc | Tìm thấy ở đâu trong lược đồ |
    |:--:|---|
    | 1 | `DAUSACH(MADS, TENSACH, NAMXB)` + `TACGIA` + `VIET` — phần *nhiều tác giả* đã tách |
    | 2 | `BANSAO(MABS, TINHTRANG)` và liên kết 1:M từ `DAUSACH` |
    | 3 | `DOCGIA(MADG, HOTEN, NGAYSINH)` |
    | 4 | `MUON(MADG, MABS, NGAYMUON, NGAYHENTRA)` — hai liên kết 1:M thay cho một M:N |
    | 5 | `THELOAI` và cột `MATL` trong `DAUSACH`, liên kết 1:M |

    Cả năm quy tắc đều tìm được chỗ ⇒ lược đồ đầy đủ. Quy tắc nào không tìm được chỗ nghĩa là còn thiếu sót và phải quay lại bước trước.

**Bài B2.** Với lược đồ vừa vẽ ở Bài B1, xác định **tính tham gia** cho từng chiều của mỗi liên kết, kèm lý do nghiệp vụ.


??? success "Lời giải bài B2"

    | Liên kết | Chiều | Tham gia | Lý do nghiệp vụ |
    |---|---|:--:|---|
    | `THELOAI` – `DAUSACH` | từ `DAUSACH` | **Bắt buộc** | Đề nói *mỗi đầu sách thuộc một thể loại*, không có sách vô thể loại |
    | | từ `THELOAI` | **Tùy chọn** | Thư viện có thể tạo sẵn thể loại rồi mới nhập sách sau |
    | `DAUSACH` – `BANSAO` | từ `BANSAO` | **Bắt buộc** | Một bản sao vật lý luôn là bản sao **của** một đầu sách nào đó |
    | | từ `DAUSACH` | **Tùy chọn** | Thư viện có thể ghi nhận đầu sách đang đặt mua, chưa có bản sao nào về kho |
    | `DOCGIA` – `MUON` | từ `MUON` | **Bắt buộc** | Một lượt mượn không thể tồn tại mà không có độc giả |
    | | từ `DOCGIA` | **Tùy chọn** | Độc giả mới làm thẻ, chưa mượn cuốn nào, vẫn phải có trong hệ thống |
    | `BANSAO` – `MUON` | từ `MUON` | **Bắt buộc** | Một lượt mượn luôn gắn với một bản sao cụ thể |
    | | từ `BANSAO` | **Tùy chọn** | Sách mới nhập chưa ai mượn |
    | `DAUSACH` – `VIET` | từ `VIET` | **Bắt buộc** | Bản ghi *viết* vô nghĩa nếu thiếu một trong hai đầu |
    | | từ `DAUSACH` | **Bắt buộc** | Đề nói mỗi đầu sách **có** tác giả, nên không có sách khuyết danh |

    Nhận xét đáng rút ra: **các thực thể sinh ra từ Bước 4 luôn tham gia bắt buộc ở cả hai chiều nối về thực thể gốc** — vì bản thân chúng chỉ tồn tại nhờ cặp ấy. Còn chiều ngược lại, từ thực thể gốc nhìn ra, hầu như luôn tùy chọn. Dòng cuối là ngoại lệ do đề bài quy định, và nếu thư viện có sách khuyết danh thì phải sửa thành tùy chọn.

**Bài B3.** Một bệnh viện quản lý **nhân viên y tế** gồm **bác sĩ** *(có chuyên khoa, số chứng chỉ hành nghề)* và **điều dưỡng** *(có khoa công tác, ca trực)*. Cả hai đều có mã, họ tên, ngày sinh, ngày vào làm.
a) Vẽ phân cấp cha–con theo EER.
b) Xác định **hai ràng buộc** *(rời nhau/chồng lấn, đầy đủ/không đầy đủ)* và nêu quy tắc nghiệp vụ tương ứng cho lựa chọn của bạn.
c) Nếu bệnh viện còn có nhân viên hành chính chưa được mô hình hóa, ràng buộc thứ hai thay đổi thế nào?


??? success "Lời giải bài B3"

    ### (a) Phân cấp cha–con

    ```text
    NHANVIENYTE(MANV, HOTEN, NGAYSINH, NGAYVAOLAM)     ← thực thể cha
       ├── BACSI(MANV, CHUYENKHOA, SOCHUNGCHI)          ← thực thể con
       └── DIEUDUONG(MANV, KHOACONGTAC, CATRUC)         ← thực thể con
    ```

    Bốn thuộc tính chung khai báo **đúng một lần** ở thực thể cha. Hai thực thể con chỉ khai thuộc tính riêng và **dùng chung khóa `MANV`** với cha — không sinh mã mới, vì một bác sĩ **là một** nhân viên y tế, hai bên nói về cùng một cá thể.

    Phép thử để chắc đây là cha–con chứ không phải liên kết thường: *"Bác sĩ **là một** nhân viên y tế"* nghe xuôi. Nếu phải nói *"có một"* thì đã là liên kết thông thường.

    ### (b) Hai ràng buộc

    Tách thành hai câu hỏi độc lập.

    **Câu hỏi 1 — một người có thể thuộc mấy nhóm con?** Đề không nói tới kiêm nhiệm, và trên thực tế một người không thể vừa là bác sĩ vừa là điều dưỡng vì hai vị trí đòi hai loại chứng chỉ hành nghề khác nhau. ⇒ **Rời nhau (d)**.

    *Quy tắc nghiệp vụ tương ứng:* “Mỗi nhân viên y tế được tuyển vào đúng một vị trí chuyên môn, hoặc bác sĩ hoặc điều dưỡng.”

    **Câu hỏi 2 — mọi người có buộc thuộc một nhóm con không?** Với phạm vi đề bài chỉ có hai nhóm ấy, mọi nhân viên y tế đều rơi vào một trong hai. ⇒ **Đầy đủ**.

    *Quy tắc nghiệp vụ tương ứng:* “Nhân viên y tế của bệnh viện chỉ gồm bác sĩ và điều dưỡng.”

    Kết luận: **rời nhau + đầy đủ**.

    ### (c) Nếu còn nhân viên hành chính chưa được mô hình hóa

    **Ràng buộc thứ hai đổi từ đầy đủ sang không đầy đủ.** Khi ấy tồn tại thể hiện của thực thể cha không thuộc con nào — nhân viên hành chính vẫn có mã, họ tên, ngày sinh, ngày vào làm nên vẫn là `NHANVIENYTE`, nhưng không phải bác sĩ cũng không phải điều dưỡng.

    Ràng buộc thứ nhất **không đổi**, vẫn là rời nhau — thêm một nhóm đứng ngoài không làm cho hai nhóm đang có chồng lấn lên nhau. Đây là bằng chứng cho thấy hai câu hỏi ràng buộc thật sự **độc lập**.

    Về mặt cài đặt, khác biệt rất cụ thể: với ràng buộc đầy đủ, hệ thống có thể bắt buộc mọi bản ghi cha phải có bản ghi con tương ứng; với không đầy đủ thì không được phép đặt ràng buộc ấy. Đặt sai là hệ thống từ chối nhập nhân viên hành chính.

## Mức C — Nâng cao

**Bài C1.** Cho quy tắc: *"Mỗi nhân viên có đúng một người quản lý trực tiếp, trừ giám đốc là người không có quản lý. Một người quản lý phụ trách nhiều nhân viên."*
a) Đây là liên kết loại gì, bậc mấy?
b) Xác định tính tham gia cho từng chiều.
c) Vì sao tình huống *"giám đốc không có quản lý"* lại là một thông tin thiết kế quan trọng chứ không phải chi tiết vụn vặt?


??? success "Lời giải bài C1"

    ### (a) Loại và bậc của liên kết

    **Liên kết đệ quy, bậc một, kết nối 1:M.**

    Chỉ có **một** loại sự vật tham gia là nhân viên, nên bậc bằng một. Sai lầm phổ biến là tách `QUANLY` thành một thực thể riêng — nhưng người quản lý cũng là một nhân viên, có đủ mã, họ tên, ngày sinh như mọi nhân viên khác. Tách ra là nhân đôi cùng một loại sự vật.

    Hỏi hai chiều: một nhân viên có **nhiều nhất một** người quản lý trực tiếp; một người quản lý phụ trách **nhiều** nhân viên. Nhiều ghép với một ⇒ **1:M**.

    Về ký pháp, Chen không cần thêm ký hiệu mới: vẫn một hình thoi ghi động từ *quản lý*, chỉ khác ở chỗ **cả hai cạnh cùng nối về một hình chữ nhật**.

    ### (b) Tính tham gia từng chiều

    | Chiều | Tham gia | Lý do |
    |---|:--:|---|
    | Từ phía **nhân viên cấp dưới** — "có quản lý" | **Tùy chọn**, `(0, 1)` | Giám đốc không có quản lý nào |
    | Từ phía **người quản lý** — "phụ trách" | **Tùy chọn**, `(0, N)` | Nhân viên thường không phụ trách ai cả |

    Cả hai chiều đều tùy chọn — một tình huống ít gặp nhưng hoàn toàn hợp lệ.

    ### (c) Vì sao "giám đốc không có quản lý" là thông tin thiết kế quan trọng

    Ba lý do, xếp theo mức độ thiệt hại nếu bỏ qua.

    **Thứ nhất, nó quyết định một ràng buộc cài đặt cụ thể.** Nếu bỏ qua chi tiết này, người thiết kế sẽ đặt tham gia là bắt buộc, và ở Chương 3 điều đó thành ràng buộc *khóa ngoại không được rỗng*. Hệ quả: **không nhập được giám đốc vào hệ thống** — nhân viên đầu tiên của công ty không có ai để trỏ tới. Đây là lỗi chỉ lộ ra khi đưa vào chạy thật, lúc sửa đã tốn kém.

    **Thứ hai, nó là trường hợp biên của toàn bộ cấu trúc.** Quan hệ quản lý tạo thành một cây, và mọi cây đều phải có gốc. Câu *"trừ giám đốc"* chính là cách đề bài mô tả cái gốc ấy. Không có nó thì cấu trúc thành một vòng tròn — ai cũng có quản lý — và mọi thuật toán duyệt cây sẽ chạy vô hạn.

    **Thứ ba, nó là ví dụ mẫu cho một thói quen nghề nghiệp.** Những cụm từ như *trừ*, *có thể*, *chưa có*, *không nhất thiết* trông như lời văn thừa nhưng luôn mang thông tin thiết kế. Người đọc đề cần tập phản xạ khoanh tròn chúng ngay từ lượt đọc đầu, đúng như Bảng 2.12 hướng dẫn.

**Bài C2.** Có ý kiến: *"Cứ dùng khóa thay thế cho mọi thực thể là an toàn nhất, khỏi phải suy nghĩ."* Hãy phản biện, dựa vào phần Chú ý ở mục 2.3.2, kèm một tình huống cụ thể cho thấy hậu quả.


??? success "Lời giải bài C2"

    Ý kiến này đúng một nửa rồi rút ra kết luận sai từ nửa còn lại.

    **Vế đúng.** Khóa thay thế quả thật nên được ưu tiên làm khóa chính, và mục 2.3.2 khuyến nghị đúng như vậy. Lý do là **tính ổn định**: khóa chính là thứ mọi bảng khác tham chiếu tới, nếu nó đổi thì toàn bộ tham chiếu phải sửa theo, mà thuộc tính nghiệp vụ thì luôn có khả năng đổi.

    **Chỗ sai nằm ở cụm "khỏi phải suy nghĩ".** Gán một mã tự sinh cho mọi thực thể là việc dễ, mất vài giây. Nhưng nếu không đồng thời xác định đâu là **tổ hợp thuộc tính thật sự phân biệt các cá thể**, thì công việc phân tích chưa xong. Khóa thay thế thay thế cho khóa chính, **không thay thế cho việc phân tích**.

    **Tình huống cụ thể.** Trung tâm ABC dùng `MAHV` tự sinh làm khóa chính của `HOCVIEN` và không khai báo thêm ràng buộc nào. Học viên Trần Văn An đăng ký khóa Anh cơ bản tháng 3, được cấp `HV001`. Tháng 9 anh quay lại đăng ký khóa giao tiếp, nhân viên tiếp tân không tra cứu mà nhập mới, hệ thống vui vẻ cấp `HV257`.

    Hậu quả:

    - Hệ thống có **hai học viên** trong khi thực tế chỉ có một người. Không ràng buộc nào bị vi phạm, vì hai mã khác nhau.
    - Lịch sử học tập bị chia đôi, trung tâm không biết đây là học viên cũ nên không áp được chính sách ưu đãi.
    - Thống kê *số học viên đã học từ hai khóa trở lên* cho ra con số sai, và không ai phát hiện được vì dữ liệu trông vẫn sạch.
    - Khi phát hiện ra sau hai năm, việc gộp hai bản ghi rất tốn kém: phải rà mọi bảng có tham chiếu tới `MAHV`.

    **Cách làm đúng** gộp ưu điểm của cả hai: dùng khóa thay thế `MAHV` làm khóa chính để tham chiếu, **đồng thời** khai báo số căn cước công dân là **ràng buộc duy nhất**. Khi ấy hệ quản trị tự chặn ngay lần nhập trùng thứ hai. Vẫn phải suy nghĩ xem cái gì thật sự phân biệt các cá thể — chỉ là kết quả của việc suy nghĩ ấy được đặt ở chỗ khác, không phải ở khóa chính.

**Bài C3.** So sánh hai phương án thiết kế cho tình huống ở mục 2.7.1 — *tạo hai thực thể riêng* và *gộp thành một thực thể* — với phương án EER. Với mỗi phương án, nêu **một tình huống thay đổi nghiệp vụ** và cho biết phương án nào chịu đựng tốt nhất.


??? success "Lời giải bài C3"

    Ba phương án cho tình huống nhân sự gồm giáo viên và nhân viên hành chính.

    | | Phương án 1 — hai thực thể riêng | Phương án 2 — gộp một thực thể | Phương án 3 — EER |
    |---|---|---|---|
    | **Thuộc tính chung** | Khai báo **hai lần** | Khai báo một lần | Khai báo một lần ở cha |
    | **Ô rỗng** | Không có | **Đầy ô rỗng** ở các cột riêng | Không có |
    | **Ngăn điền nhầm** | Được | **Không** — có thể điền bộ phận công tác cho giáo viên | Được |
    | **Liên kết riêng của một nhóm** | Diễn tả được | **Không diễn tả được** | Diễn tả được |
    | **Truy vấn toàn bộ nhân sự** | Phải ghép hai bảng | Rất dễ | Dễ — đọc bảng cha |

    ### Ba tình huống thay đổi nghiệp vụ

    **Tình huống 1 — bổ sung trường "email công vụ" cho mọi nhân sự.**

    - Phương án 1: phải sửa **hai chỗ**; quên một chỗ là hai nhóm có cấu trúc lệch nhau. Chịu đựng kém nhất.
    - Phương án 2: sửa một chỗ. Tốt.
    - Phương án 3: sửa một chỗ ở thực thể cha, hai con tự kế thừa. Tốt.

    **Tình huống 2 — chỉ giáo viên mới được phân công phụ trách lớp.**

    - Phương án 1: diễn tả được, vì liên kết gắn thẳng vào `GIAOVIEN`.
    - Phương án 2: **không diễn tả được**. Bảng gộp không phân biệt được hai nhóm, nên không có cách nào ngăn việc phân lớp cho một nhân viên hành chính. Chịu đựng kém nhất.
    - Phương án 3: diễn tả được, và đây chính là ưu điểm lớn nhất của EER — liên kết riêng của con **không lan lên cha**.

    **Tình huống 3 — thêm nhóm thứ ba là nhân viên bảo vệ.**

    - Phương án 1: tạo bảng thứ ba, lại khai báo năm thuộc tính chung **lần thứ ba**.
    - Phương án 2: thêm cột riêng cho nhóm mới, bảng càng thêm ô rỗng.
    - Phương án 3: thêm một thực thể con, khai đúng thuộc tính riêng. **Chịu đựng tốt nhất**, và chỉ cần đổi ràng buộc thứ hai từ *không đầy đủ* sang *đầy đủ* nếu ba nhóm đã phủ hết.

    ### Kết luận

    **Phương án EER chịu đựng tốt nhất ở cả ba tình huống.** Nhưng cần nhắc lại giới hạn ở mục 2.7.6: EER chỉ đáng dùng khi các nhóm con khác nhau **từ ba thuộc tính trở lên**, hoặc có **liên kết riêng**, hoặc nghiệp vụ **thật sự phân biệt** các nhóm. Nếu hai nhóm chỉ khác nhau đúng một thuộc tính thì thêm một cột phân loại vào phương án 2 là đủ và đơn giản hơn nhiều — dùng EER lúc đó là lạm dụng.

**Bài C4** *(tự chọn).* Tìm hiểu thêm về **bẫy thiết kế** *(design traps)* trong [3, Ch.4], đặc biệt là *fan trap*. Mô tả bằng lời của mình một tình huống fan trap và cách khắc phục.

---


??? success "Lời giải bài C4"

    Bài tự chọn. Dưới đây là mức trả lời được coi là đạt.

    **Fan trap là gì.** Bẫy quạt xảy ra khi một thực thể ở giữa nối tới **hai thực thể khác bằng hai liên kết một–nhiều cùng tỏa ra từ nó**, và người đọc lược đồ tưởng rằng có thể suy ra mối liên hệ trực tiếp giữa hai thực thể ngoài cùng. Thực tế thì không — đường đi qua thực thể giữa là **mơ hồ**, cho ra nhiều tổ hợp trong khi sự thật chỉ có một.

    **Tình huống cụ thể.** Một trung tâm mô tả nghiệp vụ như sau:

    ```text
    GIAOVIEN ──1──∞── CHINHANH ──1──∞── LOP
    ```

    Đọc là: một chi nhánh có nhiều giáo viên, và một chi nhánh mở nhiều lớp.

    Câu hỏi nghiệp vụ đặt ra: *"Giáo viên Lê Hoa phụ trách những lớp nào?"*

    Lược đồ trên **không trả lời được**. Từ Lê Hoa ta đi lên chi nhánh Hải Châu, rồi từ Hải Châu đi xuống được **tất cả** các lớp của chi nhánh ấy — kể cả những lớp do người khác dạy. Hình vẽ trông như có đường nối nhưng đường ấy không mang đúng thông tin, giống một chiếc quạt xòe ra từ chi nhánh.

    **Cách khắc phục.** Thêm liên kết **trực tiếp** giữa hai thực thể thật sự có quan hệ nghiệp vụ:

    ```text
    GIAOVIEN ──1──∞── LOP          ← liên kết phụ trách, bổ sung
    GIAOVIEN ──∞──1── CHINHANH
    LOP      ──∞──1── CHINHANH
    ```

    Giờ câu hỏi trên trả lời được bằng liên kết *phụ trách*, còn chi nhánh vẫn giữ vai trò riêng của nó.

    **Cách phát hiện sớm.** Bẫy quạt luôn lộ ra ở **Bước 5 — đối chiếu ngược**: lấy từng quy tắc nghiệp vụ và hỏi lược đồ có trả lời được không. Quy tắc *"mỗi lớp do một giáo viên phụ trách"* không tìm được chỗ của nó trong lược đồ đầu, và đó chính là tín hiệu. Đây là lý do Bước 5 không được làm qua loa — nó là bước duy nhất phát hiện được cái mình đã quên.
