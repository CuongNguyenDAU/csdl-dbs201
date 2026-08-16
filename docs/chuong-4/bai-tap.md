# Bài tập Chương 4

## Mức A — Nhận biết và tái hiện

**Bài A1.** Phân loại mỗi ràng buộc sau vào một trong sáu loại: (a) *"điểm thi từ 0 đến 10"*; (b) *"ngày trả không sớm hơn ngày mượn"*; (c) *"mỗi số thẻ độc giả là duy nhất"*; (d) *"mã sách trong phiếu mượn phải có trong danh mục sách"*; (e) *"ngày mượn không sớm hơn ngày cấp thẻ"*; (f) *"mỗi độc giả mượn không quá 5 cuốn cùng lúc"*.


??? success "Lời giải bài A1"

    Đi lần lượt qua hai chiều phân loại: **bối cảnh** một hay nhiều quan hệ, rồi **phạm vi** một ô, nhiều ô cùng dòng, hay nhiều dòng.

    | Ràng buộc | Loại | Bối cảnh | Vì sao |
    |---|---|:--:|---|
    | (a) *điểm thi từ 0 đến 10* | **Miền giá trị** | 1 QH | Chỉ xét **một ô**, không cần nhìn ô nào khác |
    | (b) *ngày trả không sớm hơn ngày mượn* | **Liên thuộc tính** | 1 QH | Hai ô **cùng một dòng** của phiếu mượn |
    | (c) *mỗi số thẻ độc giả là duy nhất* | **Liên bộ** | 1 QH | Phải so dòng này với **mọi dòng khác** cùng bảng |
    | (d) *mã sách trong phiếu mượn phải có trong danh mục sách* | **Khóa ngoại** | 2 QH | Nói về **sự tồn tại của giá trị khóa** ở bảng khác |
    | (e) *ngày mượn không sớm hơn ngày cấp thẻ* | **Liên thuộc tính liên quan hệ** | 2 QH | Hai ô ở **hai bảng khác nhau**: `MUON.NGAYMUON` và `DOCGIA.NGAYCAPTHE` |
    | (f) *mỗi độc giả mượn không quá 5 cuốn cùng lúc* | **Liên bộ liên quan hệ** | 2 QH | Phải **đếm nhiều dòng** ở `MUON` ứng với một dòng `DOCGIA` |

    Sáu câu này cố ý phủ đúng sáu loại. Hai chỗ dễ nhầm:

    - **(c) không phải miền giá trị.** Xét riêng một ô thì mọi số thẻ đều hợp lệ; cái sai chỉ lộ ra khi so với các dòng khác.
    - **(e) không phải khóa ngoại.** Khóa ngoại nói về *sự tồn tại* của mã độc giả; (e) nói về *quan hệ giữa hai giá trị ngày*. Một phiếu mượn có thể có mã độc giả tồn tại đàng hoàng mà ngày mượn vẫn sớm hơn ngày cấp thẻ.

**Bài A2.** Viết bằng ký hiệu logic ba ràng buộc: (a) mọi giáo viên phải có bằng cấp thuộc tập {Cử nhân, Thạc sĩ, Tiến sĩ}; (b) ngày ghi danh không muộn hơn ngày khai giảng của lớp; (c) không hai lớp nào trùng mã.


??? success "Lời giải bài A2"

    ### (a) Bằng cấp giáo viên thuộc tập cho trước

    ```text
    ∀t ∈ GIAOVIEN : t.BANGCAP ∈ {'Cử nhân', 'Thạc sĩ', 'Tiến sĩ'}
    ```

    Loại **miền giá trị**, bối cảnh 1 quan hệ. Khai báo được bằng `CHECK (BANGCAP IN (...))`.

    ### (b) Ngày ghi danh không muộn hơn ngày khai giảng

    ```text
    ∀g ∈ GHIDANH, ∀l ∈ LOP : (g.MALOP = l.MALOP) ⇒ (g.NGAYGHIDANH ≤ l.NGAYKG)
    ```

    Loại **liên thuộc tính liên quan hệ**, bối cảnh 2 quan hệ. Chú ý phần `⇒` — chỉ so sánh khi hai dòng **thật sự ứng với nhau** qua `MALOP`; thiếu vế điều kiện này thì công thức đòi mọi lượt ghi danh phải sớm hơn mọi lớp, sai hẳn ý định.

    ### (c) Không hai lớp nào trùng mã

    ```text
    ∀t₁, t₂ ∈ LOP : t₁ ≠ t₂ ⇒ t₁.MALOP ≠ t₂.MALOP
    ```

    Loại **liên bộ**, bối cảnh 1 quan hệ. Đây chính là ràng buộc khóa chính, hệ quản trị tự bảo đảm khi khai `PRIMARY KEY`.

**Bài A3.** Đọc đoạn khai báo sau và **phát biểu bằng lời** từng ràng buộc mà nó diễn đạt:

```sql
CREATE TABLE LOP (
    MALOP    VARCHAR(10)  NOT NULL PRIMARY KEY,
    TENLOP   NVARCHAR(50) NOT NULL,
    NGAYKG   DATE         NOT NULL,
    NGAYKT   DATE         NOT NULL,
    SUCCHUA  INT          CHECK (SUCCHUA BETWEEN 5 AND 40),
    MAGV     VARCHAR(10)  NULL,
    CONSTRAINT ck_ngay CHECK (NGAYKT >= NGAYKG),
    CONSTRAINT fk_lop_gv FOREIGN KEY (MAGV)
        REFERENCES GIAOVIEN(MAGV) ON DELETE SET NULL
);
```


??? success "Lời giải bài A3"

    Đoạn khai báo diễn đạt **tám** ràng buộc.

    | # | Khai báo | Phát biểu bằng lời | Loại |
    |:--:|---|---|---|
    | 1 | `MALOP … PRIMARY KEY` | Mỗi lớp có mã duy nhất, không hai lớp trùng mã | Liên bộ |
    | 2 | `MALOP … NOT NULL` | Mã lớp không được bỏ trống | Miền giá trị *(toàn vẹn thực thể)* |
    | 3 | `TENLOP … NOT NULL` | Mọi lớp đều phải có tên | Miền giá trị |
    | 4 | `NGAYKG … NOT NULL` | Mọi lớp đều phải có ngày khai giảng | Miền giá trị |
    | 5 | `NGAYKT … NOT NULL` | Mọi lớp đều phải có ngày kết thúc | Miền giá trị |
    | 6 | `CHECK (SUCCHUA BETWEEN 5 AND 40)` | Sức chứa của lớp từ 5 đến 40 chỗ | Miền giá trị |
    | 7 | `CONSTRAINT ck_ngay CHECK (NGAYKT >= NGAYKG)` | Ngày kết thúc không sớm hơn ngày khai giảng | **Liên thuộc tính** |
    | 8 | `FOREIGN KEY (MAGV) REFERENCES GIAOVIEN(MAGV)` | Nếu lớp có ghi giáo viên thì mã ấy phải tồn tại trong `GIAOVIEN` | **Khóa ngoại** |

    Ngoài tám ràng buộc trên, đoạn khai báo còn nói **hai điều nữa** không phải ràng buộc mà là quyết định thiết kế:

    - **`MAGV … NULL`** — lớp **được phép** tạm chưa có giáo viên. Đây chính là **tham gia tùy chọn** phía `LOP` đã xác định từ Chương 2, giờ hiện ra dưới dạng khóa ngoại cho phép rỗng.
    - **`ON DELETE SET NULL`** — **hành động khi vi phạm**: xóa một giáo viên thì các lớp người đó phụ trách chuyển sang trạng thái *chưa có người phụ trách* thay vì bị chặn hoặc bị xóa theo. Chiều lan truyền luôn đi từ **cha sang con**.

    Điểm đáng chú ý: `SUCCHUA` **không** có `NOT NULL`, nên nó được phép rỗng — nghĩa là *chưa xác định sức chứa*. Ràng buộc `CHECK` chỉ kiểm tra khi giá trị khác rỗng.

## Mức B — Vận dụng

**Bài B1.** Dùng lược đồ quan hệ **thư viện** đã ánh xạ ở Bài B1 Chương 3, hãy phát hiện **đầy đủ ít nhất 8 ràng buộc toàn vẹn**, phủ **đủ cả sáu loại**. Với mỗi ràng buộc, ghi: mã, phát biểu bằng lời, biểu thức hình thức, loại, bối cảnh.


??? success "Lời giải bài B1"

    Lược đồ thư viện từ Bài B1 Chương 3:

    ```text
    THELOAI(MATL, TENTL)
    DAUSACH(MADS, TENSACH, NAMXB, MATL)
    TACGIA(MATG, HOTEN_TG)
    VIET(MADS, MATG)
    BANSAO(MABS, TINHTRANG, MADS)
    DOCGIA(MADG, HOTEN, NGAYSINH, NGAYCAPTHE)
    MUON(MADG, MABS, NGAYMUON, NGAYHENTRA, NGAYTRA)
    ```

    *(Bổ sung `NGAYCAPTHE` và `NGAYTRA` để có đủ chất liệu cho sáu loại.)*

    | Mã | Phát biểu | Biểu thức | Loại | Bối cảnh |
    |:--:|---|---|---|:--:|
    | **R1** | Năm xuất bản không muộn hơn năm hiện tại | `∀d ∈ DAUSACH : d.NAMXB ≤ NAM_HIENTAI` | Miền giá trị | 1 QH |
    | **R2** | Tình trạng bản sao thuộc tập cho trước | `∀b ∈ BANSAO : b.TINHTRANG ∈ {'tốt','hỏng','mất'}` | Miền giá trị | 1 QH |
    | **R3** | Ngày hẹn trả không sớm hơn ngày mượn | `∀m ∈ MUON : m.NGAYHENTRA ≥ m.NGAYMUON` | Liên thuộc tính | 1 QH |
    | **R4** | Nếu đã trả thì ngày trả không sớm hơn ngày mượn | `∀m ∈ MUON : m.NGAYTRA ≠ null ⇒ m.NGAYTRA ≥ m.NGAYMUON` | Liên thuộc tính | 1 QH |
    | **R5** | Không hai độc giả trùng mã thẻ | `∀t₁ ≠ t₂ ∈ DOCGIA : t₁.MADG ≠ t₂.MADG` | Liên bộ | 1 QH |
    | **R6** | Mã đầu sách trong `BANSAO` phải tồn tại | `∀b ∈ BANSAO, ∃d ∈ DAUSACH : b.MADS = d.MADS` | Khóa ngoại | 2 QH |
    | **R7** | Mã độc giả trong `MUON` phải tồn tại | `∀m ∈ MUON, ∃g ∈ DOCGIA : m.MADG = g.MADG` | Khóa ngoại | 2 QH |
    | **R8** | Ngày mượn không sớm hơn ngày cấp thẻ | `∀m ∈ MUON, ∀g ∈ DOCGIA : (m.MADG = g.MADG) ⇒ (m.NGAYMUON ≥ g.NGAYCAPTHE)` | Liên thuộc tính liên QH | 2 QH |
    | **R9** | Mỗi độc giả mượn không quá 5 cuốn cùng lúc | `∀g ∈ DOCGIA : \|{m ∈ MUON : m.MADG = g.MADG ∧ m.NGAYTRA = null}\| ≤ 5` | Liên bộ liên QH | 2 QH |

    **Chín ràng buộc, phủ đủ sáu loại** — vượt yêu cầu tối thiểu tám. Cách làm để không bỏ sót: đi lần lượt sáu dòng của Bảng 4.3 và tự hỏi *bài này có ràng buộc loại đó không*, thay vì nghĩ tự do rồi đếm lại.

**Bài B2.** Chọn **ba ràng buộc** trong Bài B1 — một loại dễ, một loại trung bình, một loại khó — và lập **bảng tầm ảnh hưởng** đầy đủ cho từng ràng buộc, kèm **suy luận từng ô** theo mẫu Bảng 4.4.


??? success "Lời giải bài B2"

    ### Loại dễ — R2, ràng buộc miền giá trị

    Bối cảnh chỉ có `BANSAO`.

    | Ô cần xét | Suy luận | Kết quả |
    |---|---|:--:|
    | Thêm vào `BANSAO` | Nhập dòng mới với `TINHTRANG = 'rách bìa'` không thuộc tập hợp lệ | **+** |
    | Xóa khỏi `BANSAO` | Bớt một dòng là bớt một thứ cần kiểm | **−** |
    | Sửa `TINHTRANG` | Đổi sang giá trị ngoài tập hợp lệ | **+** *(TINHTRANG)* |

    | Quan hệ | Thêm | Xóa | Sửa |
    |---|:--:|:--:|:--:|
    | `BANSAO` | **+** | − | **+** *(TINHTRANG)* |

    **Hai điểm kiểm tra.** Đây là dạng dễ nhất: ràng buộc miền giá trị luôn có bảng dạng `+ − +`, và `CHECK` xử lý trọn vẹn.

    ### Loại trung bình — R7, ràng buộc khóa ngoại

    Bối cảnh gồm `DOCGIA` *(cha)* và `MUON` *(con)*.

    | Ô cần xét | Suy luận | Kết quả |
    |---|---|:--:|
    | Thêm vào `MUON` | Nhập phiếu với `MADG` chưa tồn tại → trỏ vào hư vô | **+** |
    | Xóa khỏi `MUON` | Bớt một tham chiếu cần kiểm | **−** |
    | Sửa `MADG` ở `MUON` | Đổi sang mã lạ | **+** *(MADG)* |
    | Thêm vào `DOCGIA` | Có thêm độc giả; không tham chiếu nào đang có bị ảnh hưởng | **−** |
    | Xóa khỏi `DOCGIA` | Xóa độc giả trong khi `MUON` còn phiếu trỏ tới → tham chiếu treo | **+** |
    | Sửa `MADG` ở `DOCGIA` | Đổi khóa chính → mọi phiếu con bị lệch | **+** *(MADG)* |

    | Quan hệ | Thêm | Xóa | Sửa |
    |---|:--:|:--:|:--:|
    | `DOCGIA` *(cha)* | − | **+** | **+** *(MADG)* |
    | `MUON` *(con)* | **+** | − | **+** *(MADG)* |

    **Bốn điểm kiểm tra**, đúng dạng đối xứng chéo của câu thần chú **"Thêm ở con, Xóa ở cha"**. Hệ quản trị lo trọn khi khai `FOREIGN KEY`.

    ### Loại khó — R9, ràng buộc liên bộ liên quan hệ

    Bối cảnh gồm `DOCGIA` và `MUON`.

    | Ô cần xét | Suy luận | Kết quả |
    |---|---|:--:|
    | Thêm vào `MUON` | Cho mượn cuốn thứ 6 khi độc giả đang giữ 5 cuốn | **+** |
    | Xóa khỏi `MUON` | Bớt một phiếu đang mượn → số đếm giảm, càng an toàn | **−** |
    | Sửa `MADG` ở `MUON` | Chuyển phiếu sang độc giả khác → người nhận có thể vượt 5 | **+** *(MADG)* |
    | Sửa `NGAYTRA` ở `MUON` | Đổi từ có ngày trả sang rỗng → phiếu **quay lại** trạng thái đang mượn, số đếm tăng | **+** *(NGAYTRA)* |
    | Thêm vào `DOCGIA` | Độc giả mới chưa mượn gì, số đếm bằng 0 | **−** |
    | Xóa khỏi `DOCGIA` | Bớt một độc giả cần kiểm | **−** |
    | Sửa `DOCGIA` | Không thuộc tính nào của `DOCGIA` tham gia điều kiện | **−** |

    | Quan hệ | Thêm | Xóa | Sửa |
    |---|:--:|:--:|:--:|
    | `DOCGIA` | − | − | − |
    | `MUON` | **+** | − | **+** *(MADG, NGAYTRA)* |

    **Hai ô `+` nhưng ô sửa có tới hai thuộc tính** cần theo dõi, trong đó `NGAYTRA` là chỗ **rất dễ bỏ sót**: người ta thường chỉ nghĩ tới lúc cho mượn mà quên rằng hủy một lần trả cũng làm số đếm tăng. `CHECK` không diễn tả nổi loại này, phải dùng **trigger**.

**Bài B3.** Với mọi khóa ngoại trong lược đồ thư viện, đề xuất **hành động khi xóa bản ghi cha**, kèm **lý do nghiệp vụ** cho từng lựa chọn. Chỉ ra ít nhất một trường hợp mà dùng lan truyền sẽ là **thảm họa**.


??? success "Lời giải bài B3"

    | Khóa ngoại | Hành động khi xóa bản ghi cha | Lý do nghiệp vụ |
    |---|---|---|
    | `DAUSACH.MATL` → `THELOAI` | **Gán rỗng** | Xóa một thể loại không có nghĩa là sách biến mất; sách chuyển sang *chưa xếp thể loại*, thủ thư phân loại lại sau |
    | `BANSAO.MADS` → `DAUSACH` | **Từ chối** | Không thể xóa một đầu sách khi kho còn bản sao vật lý; phải thanh lý bản sao trước |
    | `VIET.MADS` → `DAUSACH` | **Lan truyền** | Xóa đầu sách thì các bản ghi *ai viết cuốn đó* mất hết ý nghĩa; đây là bảng nối thuần túy |
    | `VIET.MATG` → `TACGIA` | **Lan truyền** | Cùng lý do trên |
    | `MUON.MADG` → `DOCGIA` | **Từ chối** | Lịch sử mượn là chứng từ, không được bốc hơi theo độc giả. Nếu cần xóa thì phải lưu trữ lịch sử trước |
    | `MUON.MABS` → `BANSAO` | **Từ chối** | Cùng lý do — phiếu mượn là bằng chứng cuốn sách từng được ai giữ |

    ### Trường hợp lan truyền là thảm họa

    **`MUON.MADG` → `DOCGIA` với `ON DELETE CASCADE`.**

    Kịch bản: thủ thư dọn danh sách độc giả hết hạn thẻ, xóa 200 người không gia hạn trong ba năm.

    Hậu quả nếu đặt lan truyền:

    - **Toàn bộ lịch sử mượn của 200 người biến mất** cùng lúc, im lặng, không một cảnh báo. Một câu lệnh xóa 200 dòng làm mất hàng chục nghìn dòng lịch sử.
    - Thư viện **mất luôn bằng chứng** về những cuốn sách chưa được trả. Nếu trong số đó có người đang giữ sách quá hạn thì không còn cách nào truy ra.
    - Báo cáo thống kê lượt mượn theo năm **đổi kết quả hồi tố** — số liệu năm ngoái hôm nay khác hôm qua, mà không ai biết vì sao.
    - Không hoàn tác được, trừ khi khôi phục từ bản sao lưu và mất mọi thay đổi sau đó.

    **Nguyên tắc rút ra:** lan truyền chỉ an toàn khi bản ghi con **hoàn toàn vô nghĩa** nếu thiếu bản ghi cha — như bảng nối `VIET`, hay các số điện thoại của một học viên. Với dữ liệu mang tính **chứng từ, lịch sử, giao dịch**, mặc định phải là **từ chối**.

**Bài B4.** Ràng buộc *"mỗi độc giả mượn không quá 5 cuốn cùng lúc"*:
a) Thuộc loại nào? Bối cảnh gồm những quan hệ nào?
b) Lập bảng tầm ảnh hưởng.
c) Viết **mã giả** cho trigger thực thi ràng buộc này.
d) Từ bảng tầm ảnh hưởng, cho biết cần **bao nhiêu** điểm kiểm tra.


??? success "Lời giải bài B4"

    Ràng buộc R9: *mỗi độc giả mượn không quá 5 cuốn cùng lúc*.

    ### (a) Loại và bối cảnh

    **Liên bộ liên quan hệ.** Điều kiện phải **đếm nhiều dòng** của `MUON` — nên là *liên bộ*; các dòng ấy nằm ở bảng khác với `DOCGIA` — nên là *liên quan hệ*.

    Bối cảnh: **`DOCGIA` và `MUON`**, hai quan hệ.

    Biểu thức:

    ```text
    ∀g ∈ DOCGIA : |{ m ∈ MUON : m.MADG = g.MADG ∧ m.NGAYTRA = null }| ≤ 5
    ```

    Chú ý điều kiện `NGAYTRA = null` — ràng buộc nói *cùng lúc*, tức chỉ đếm phiếu **chưa trả**, không đếm toàn bộ lịch sử.

    ### (b) Bảng tầm ảnh hưởng

    | Quan hệ | Thêm | Xóa | Sửa |
    |---|:--:|:--:|:--:|
    | `DOCGIA` | − | − | − |
    | `MUON` | **+** | − | **+** *(MADG, NGAYTRA)* |

    Đã suy luận từng ô ở Bài B2 phần "loại khó".

    ### (c) Mã giả cho trigger

    ```text
    TRIGGER kiem_tra_gioi_han_muon
    TRÊN bảng MUON
    KHI  THÊM hoặc SỬA
    BẮT ĐẦU
        -- xác định độc giả bị ảnh hưởng bởi thao tác vừa rồi
        ds_docgia ← tập MADG của các dòng vừa thêm hoặc vừa sửa

        VỚI MỖI g TRONG ds_docgia:
            dang_muon ← ĐẾM dòng trong MUON
                        NƠI  MADG = g VÀ NGAYTRA LÀ RỖNG

            NẾU dang_muon > 5 THÌ
                HỦY thao tác
                BÁO LỖI 'Độc giả ' + g + ' đang mượn ' + dang_muon
                         + ' cuốn, vượt giới hạn 5 cuốn.'
            HẾT NẾU
        HẾT VỚI MỖI
    KẾT THÚC
    ```

    Ba điểm đáng lưu ý khi viết trigger này:

    1. **Phải xử lý theo tập, không theo từng dòng.** Một lệnh nhập hàng loạt có thể thêm nhiều phiếu cùng lúc; trigger chỉ kiểm dòng đầu tiên sẽ để lọt.
    2. **Sửa `NGAYTRA` từ có giá trị về rỗng cũng phải kiểm** — đây là chỗ dễ quên nhất, vì trực giác chỉ nghĩ tới lúc cho mượn.
    3. **Chạy sau khi thay đổi rồi mới đếm**, và hủy nếu vi phạm. Đếm trước khi thay đổi sẽ lệch một đơn vị.

    ### (d) Số điểm kiểm tra cần thiết

    Từ bảng tầm ảnh hưởng: **hai ô `+`**, nhưng ô *sửa* theo dõi **hai thuộc tính** khác nhau. Vậy cần:

    - **1 điểm kiểm** khi **thêm** vào `MUON`
    - **1 điểm kiểm** khi **sửa `MADG`** ở `MUON`
    - **1 điểm kiểm** khi **sửa `NGAYTRA`** ở `MUON`

    Tổng **ba điểm kiểm tra**. Trong thực tế, một trigger duy nhất khai `KHI THÊM hoặc SỬA` phủ được cả ba, nhưng khi rà soát vẫn phải liệt kê đủ ba để không bỏ sót tình huống nào lúc kiểm thử.

    Bốn ô `−` là phần **tiết kiệm được**: không cần đặt bất kỳ kiểm tra nào ở `DOCGIA`, và không cần kiểm khi xóa phiếu mượn. Đó chính là giá trị của bảng tầm ảnh hưởng — nó thu hẹp phạm vi thay vì bắt kiểm tra khắp nơi.

## Mức C — Nâng cao

**Bài C1.** Có ý kiến: *"Đặt ràng buộc ở tầng cơ sở dữ liệu làm hệ thống chạy chậm, nên tốt nhất là để ứng dụng kiểm tra hết."* Hãy phản biện, dựa vào mục 4.1.4, kèm một tình huống cụ thể minh họa hậu quả.


??? success "Lời giải bài C1"

    Ý kiến *"ràng buộc ở cơ sở dữ liệu làm chậm, để ứng dụng kiểm hết"* nhầm ở cả tiền đề lẫn kết luận.

    **Về tiền đề — chi phí không nằm ở chỗ họ tưởng.** Ràng buộc miền giá trị và liên thuộc tính chỉ đọc dữ liệu **trong chính dòng đang ghi**, chi phí gần như bằng không. Ràng buộc khóa ngoại có tốn hơn, nhưng hệ quản trị dùng chỉ mục nên vẫn rất nhanh — và bản thân ứng dụng nếu tự kiểm cũng phải chạy đúng câu truy vấn ấy, thậm chí còn thêm một vòng đi về qua mạng. Đưa việc kiểm tra lên ứng dụng thường **chậm hơn**, không nhanh hơn.

    **Về kết luận — nó bỏ qua điều quan trọng nhất: dữ liệu vào bằng nhiều đường.** Ứng dụng chính chỉ là một trong số đó. Còn có nhập hàng loạt từ tệp, khôi phục từ bản sao lưu, công cụ quản trị chạy lệnh trực tiếp, tác vụ đồng bộ định kỳ, và các ứng dụng viết sau bởi người khác. Ràng buộc đặt trong ứng dụng chỉ canh đúng một cửa, trong khi ngôi nhà có sáu cửa.

    **Tình huống cụ thể.** Trung tâm ABC đặt toàn bộ kiểm tra ở phần mềm ghi danh, trong đó có quy định *học phí phải lớn hơn 0*. Chạy ổn hai năm.

    Sang năm thứ ba, trung tâm ký hợp tác với một công ty và nhận danh sách 500 học viên dưới dạng tệp Excel. Nhân viên kỹ thuật viết một đoạn nhập liệu ghi thẳng vào bảng `GHIDANH` — không đi qua phần mềm ghi danh, vì phần mềm không có chức năng nhập hàng loạt.

    Trong tệp có 12 dòng ghi học phí là `0` (học viên được tài trợ toàn phần) và 3 dòng bị lỗi dấu, thành số âm.

    Hậu quả dây chuyền:

    - Cơ sở dữ liệu nhận trọn 15 dòng sai, **không một cảnh báo nào**, vì hàng rào duy nhất nằm ở phần mềm mà dữ liệu không đi qua.
    - Báo cáo doanh thu quý bị lệch, và sai theo hướng khó phát hiện: tổng vẫn là một con số trông hợp lý.
    - Sáu tháng sau kế toán phát hiện chênh lệch khi đối chiếu sổ quỹ. Lúc này phải rà lại toàn bộ 500 dòng để tìm 15 dòng sai, và **không còn cách nào biết chắc** dòng nào là tài trợ thật, dòng nào là lỗi nhập.
    - Chi phí truy tìm và đối soát lớn hơn nhiều lần khoản thời gian mà việc bỏ ràng buộc tiết kiệm được.

    **Kết luận đúng.** Ràng buộc ở cơ sở dữ liệu là **hàng rào cuối cùng**, và giá trị của nó nằm ở chỗ **không thể đi vòng qua**. Ứng dụng vẫn nên kiểm tra sớm để báo lỗi thân thiện cho người dùng — nhưng đó là kiểm tra **bổ sung**, không phải thay thế. Đúng như quy tắc thứ 10 của Codd: ràng buộc toàn vẹn phải khai báo được trong chính cơ sở dữ liệu, không nằm rải rác trong mã ứng dụng.

**Bài C2.** Thư viện muốn lưu thêm cột `SOCUONDANGMUON` trong bảng `DOCGIA` để biết ngay mỗi độc giả đang mượn bao nhiêu cuốn.
a) Lập bảng tầm ảnh hưởng cho ràng buộc *"`SOCUONDANGMUON` bằng số phiếu mượn chưa trả"*.
b) Đếm số ô `+`. Đây có phải **cờ đỏ thiết kế** không?
c) Đề xuất **đơn thuốc** và cho biết ràng buộc nào biến mất sau khi sửa.


??? success "Lời giải bài C2"

    ### (a) Bảng tầm ảnh hưởng

    Ràng buộc: `∀g ∈ DOCGIA : g.SOCUONDANGMUON = |{m ∈ MUON : m.MADG = g.MADG ∧ m.NGAYTRA = null}|`

    | Ô cần xét | Suy luận | Kết quả |
    |---|---|:--:|
    | Thêm vào `MUON` | Cho mượn thêm một cuốn → số thật tăng, cột lưu không đổi → lệch | **+** |
    | Xóa khỏi `MUON` | Hủy một phiếu → số thật giảm → lệch | **+** |
    | Sửa `MADG` ở `MUON` | Chuyển phiếu sang người khác → **cả hai** độc giả đều lệch | **+** |
    | Sửa `NGAYTRA` ở `MUON` | Ghi nhận trả sách → số thật giảm → lệch | **+** |
    | Thêm vào `DOCGIA` | Độc giả mới; nếu khởi tạo cột khác 0 thì lệch ngay | **+** |
    | Xóa khỏi `DOCGIA` | Bớt một dòng cần kiểm | **−** |
    | Sửa `SOCUONDANGMUON` | Sửa tay con số → lệch với thực tế | **+** |

    | Quan hệ | Thêm | Xóa | Sửa |
    |---|:--:|:--:|:--:|
    | `DOCGIA` | **+** | − | **+** *(SOCUONDANGMUON)* |
    | `MUON` | **+** | **+** | **+** *(MADG, NGAYTRA)* |

    ### (b) Đếm ô `+` — có phải cờ đỏ thiết kế không

    **Năm trên sáu ô là `+`.** Đây là **cờ đỏ thiết kế**, rõ ràng.

    Ba dấu hiệu cùng chỉ về một hướng:

    1. **Mật độ `+` gần như tối đa.** So sánh: ràng buộc miền giá trị có 2 ô `+`, khóa ngoại có 4 ô, còn cái này có 5 và ô *sửa* ở `MUON` còn theo dõi hai thuộc tính.
    2. **Không cơ chế khai báo nào phủ nổi** — `CHECK` và `FOREIGN KEY` đều bó tay, buộc phải viết trigger cho từng ô, và mỗi trigger là một chỗ có thể sai.
    3. **Bản chất là một thuộc tính dẫn xuất được lưu lại** — đúng thứ Chương 2 đã cảnh báo ở mục 2.2.5, và Chương 1 gọi tên là **dư thừa**.

    ### (c) Đơn thuốc

    **Bỏ hẳn cột `SOCUONDANGMUON`.** Khi cần con số ấy thì tính lại bằng phép đếm:

    ```text
    π_MADG, ĐẾM(*) ( σ_(NGAYTRA = null) (MUON) )
    ```

    **Ràng buộc nào biến mất.** Ràng buộc *"cột này bằng số phiếu chưa trả"* **không còn tồn tại** — không phải vì ta thực thi nó giỏi hơn, mà vì **không còn hai nguồn sự thật để mà lệch nhau**. Năm ô `+` biến mất cùng nó.

    **Ràng buộc nào ở lại.** R9 *"mỗi độc giả mượn không quá 5 cuốn"* vẫn còn, vì đó là quy định nghiệp vụ thật chứ không phải hệ quả của thiết kế. Nhưng nó chỉ có **2 ô `+`** thay vì 5, và trigger cho nó đơn giản hơn hẳn.

    **Khi nào thì được phép giữ cột.** Nếu thư viện có hàng triệu phiếu mượn và màn hình tra cứu phải hiện con số ấy liên tục, phép đếm mỗi lần sẽ quá đắt. Khi ấy chấp nhận lưu — nhưng **phải kèm cơ chế bảo đảm luôn khớp**, và phải ý thức rằng mình đang trả giá bằng năm điểm kiểm tra. Chương 5 gọi lựa chọn có cân nhắc này là **phi chuẩn hóa**, và nhấn mạnh rằng nó chỉ hợp lý khi đo được lợi ích cụ thể.

**Bài C3.** Mục 3.7.3 dạy dùng kết ngoài để **phát hiện** khóa ngoại mồ côi; mục 4.4.3 dạy dùng khai báo để **ngăn chặn**. Giả sử bạn tiếp quản một cơ sở dữ liệu cũ chưa khai báo ràng buộc nào và đang có dữ liệu mồ côi.
a) Vì sao **không thể** khai báo khóa ngoại ngay?
b) Nêu quy trình từng bước để dọn dẹp rồi khai báo được.


??? success "Lời giải bài C3"

    ### (a) Vì sao không thể khai báo khóa ngoại ngay

    Khi thực thi lệnh thêm ràng buộc, hệ quản trị **kiểm tra toàn bộ dữ liệu đang có** trước khi bật. Logic rất đơn giản: một ràng buộc có nghĩa là điều kiện phải đúng ở **mọi thời điểm**, kể cả thời điểm hiện tại. Nếu trong bảng còn dòng vi phạm thì bật ràng buộc lên là tự mâu thuẫn.

    Kết quả: lệnh khai báo **bị từ chối**, kèm thông báo đại ý *không thể tạo ràng buộc vì dữ liệu hiện có vi phạm*. Bảng giữ nguyên trạng thái cũ, không ràng buộc nào được thêm.

    Đây thật ra là hành vi đúng đắn. Nếu hệ quản trị cho bật ràng buộc mà bỏ qua dữ liệu cũ, ta sẽ có một cơ sở dữ liệu tuyên bố *đã có ràng buộc* trong khi vẫn chứa dữ liệu vi phạm — tình huống nguy hiểm hơn cả việc không có ràng buộc nào, vì nó tạo cảm giác an toàn giả.

    ### (b) Quy trình từng bước

    **Bước 1 — Phát hiện toàn bộ dòng mồ côi.** Dùng đúng kỹ thuật đã học ở Chương 3:

    ```text
    π_MADG (MUON) − π_MADG (DOCGIA)
    ```

    hoặc lấy trọn dòng lỗi bằng kết ngoài rồi lọc dòng có rỗng ở phần bảng cha. Làm cho **từng khóa ngoại** dự định khai báo, và **ghi lại kết quả ra một bảng tạm** — đây là hồ sơ để đối chiếu về sau.

    **Bước 2 — Phân loại nguyên nhân.** Không phải mọi dòng mồ côi đều xử lý giống nhau. Ba nhóm thường gặp:

    - **Sai chính tả hoặc lệch định dạng** — mã `HV01` với `HV1`, hoặc có khoảng trắng thừa. Nhóm này **sửa được**.
    - **Bản ghi cha đã bị xóa** — độc giả bị xóa khỏi hệ thống nhưng phiếu mượn còn. Cần quyết định: khôi phục bản ghi cha, hay chấp nhận mất tham chiếu.
    - **Dữ liệu rác từ nhập liệu hỏng** — mã không có nghĩa gì. Nhóm này thường xóa.

    Bước này **bắt buộc có người hiểu nghiệp vụ tham gia**, không thể tự động hóa. Xóa nhầm một phiếu mượn hợp lệ là mất chứng từ.

    **Bước 3 — Xử lý theo từng nhóm.**

    - Sửa các mã sai về giá trị đúng.
    - Với dòng không cứu được: **gán rỗng** nếu khóa ngoại cho phép rỗng và việc mất tham chiếu chấp nhận được; **xóa** nếu dòng ấy thật sự là rác; hoặc **tạo bản ghi cha thay thế** dạng *(không xác định)* nếu cần giữ lại lịch sử.
    - Với khóa ngoại nằm trong khóa chính thì không gán rỗng được, chỉ còn hai lựa chọn kia.

    **Bước 4 — Kiểm tra lại cho tới khi tập rỗng.** Chạy lại biểu thức ở Bước 1. Chỉ khi kết quả **rỗng hoàn toàn** mới đi tiếp.

    **Bước 5 — Khai báo ràng buộc.** Giờ lệnh thêm khóa ngoại sẽ chạy được. Đồng thời chọn **hành động khi vi phạm** phù hợp nghiệp vụ, đừng để mặc định.

    **Bước 6 — Chốt cửa còn lại.** Ràng buộc mới chỉ chặn từ nay về sau. Cần rà thêm: có đường nhập liệu nào đang tắt kiểm tra khóa ngoại không, có tác vụ đồng bộ nào ghi thẳng vào bảng không. Bịt nốt những cửa ấy, nếu không dữ liệu mồ côi sẽ quay lại.

    **Thứ tự quan trọng nhất là Bước 1 trước Bước 3.** Cám dỗ thường gặp là xóa ngay cho nhanh; nhưng xóa trước khi phân loại là mất luôn khả năng phân biệt dữ liệu cứu được với dữ liệu rác.

**Bài C4** *(tự chọn).* Tìm hiểu về **assertion** — cơ chế khai báo ràng buộc trên nhiều bảng trong chuẩn SQL. Vì sao hầu hết hệ quản trị thương mại **không hỗ trợ** cơ chế này, và người ta dùng gì để thay thế?

---


??? success "Lời giải bài C4"

    Bài tự chọn. Dưới đây là mức trả lời được coi là đạt.

    **Assertion là gì.** Chuẩn SQL định nghĩa `CREATE ASSERTION` — một ràng buộc **không gắn với bảng nào cụ thể**, phát biểu một điều kiện phải luôn đúng trên **toàn bộ cơ sở dữ liệu**. Ví dụ đúng ý định của R9:

    ```sql
    CREATE ASSERTION gioi_han_muon CHECK (
        NOT EXISTS (
            SELECT MADG FROM MUON WHERE NGAYTRA IS NULL
            GROUP BY MADG HAVING COUNT(*) > 5
        )
    );
    ```

    Ưu điểm rất rõ: khai báo **một lần**, đúng như phát biểu bằng lời, không phải nghĩ xem đặt trigger ở bảng nào và trên thao tác nào. Đây chính là thứ mà bảng tầm ảnh hưởng đang phải làm thủ công.

    **Vì sao hầu hết hệ quản trị thương mại không hỗ trợ.** Lý do nằm ở **chi phí kiểm tra**.

    Ràng buộc gắn với bảng thì hệ quản trị biết chính xác thao tác nào có thể phá vỡ nó — đúng thông tin mà bảng tầm ảnh hưởng nắm giữ. Còn assertion không gắn với bảng nào, nên về nguyên tắc **mọi thao tác trên mọi bảng** đều có thể làm nó sai. Cài đặt đúng theo chuẩn thì sau **mỗi** câu lệnh thay đổi dữ liệu, hệ quản trị phải chạy lại **toàn bộ** các assertion đang có. Với cơ sở dữ liệu lớn thì chi phí này không chấp nhận được.

    Về lý thuyết có thể phân tích tĩnh để suy ra assertion nào phụ thuộc bảng nào — tức là để máy tự lập bảng tầm ảnh hưởng. Nhưng với câu điều kiện phức tạp thì bài toán ấy rất khó, và các hãng chọn không làm.

    **Người ta dùng gì thay thế.**

    | Cách thay thế | Ưu | Nhược |
    |---|---|---|
    | **Trigger** | Chạy được mọi thứ; kiểm soát được đúng thao tác cần kiểm | Phải tự xác định đặt ở đâu — chính là công việc lập bảng tầm ảnh hưởng; khó gỡ lỗi |
    | **`CHECK` mở rộng** *(một số hệ cho phép truy vấn con)* | Gần với assertion nhất | Không chuẩn, mỗi hệ một kiểu; nhiều hệ chỉ cho biểu thức trên cùng dòng |
    | **Sửa thiết kế cho ràng buộc biến mất** | Rẻ nhất và bền nhất | Không phải ràng buộc nào cũng khử được bằng thiết kế |
    | **Kiểm tra định kỳ ngoài giờ** | Không ảnh hưởng hiệu năng lúc chạy | Chỉ **phát hiện** chứ không **ngăn chặn**; dữ liệu sai đã tồn tại một thời gian |

    **Điều đáng rút ra.** Việc assertion không được hỗ trợ chính là lý do Chương 4 phải dạy **bảng tầm ảnh hưởng**. Nếu mọi hệ quản trị đều chạy được assertion thì người thiết kế chỉ cần phát biểu điều kiện là xong. Thực tế thì phần việc *xác định thao tác nào có thể phá vỡ điều kiện* vẫn thuộc về con người — và bảng tầm ảnh hưởng là công cụ để làm việc ấy cho có hệ thống.
