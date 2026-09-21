# Đặc tả yêu cầu phần mềm

**Hệ thống:** Hệ thống Quản lý Bãi đỗ xe - Phiên bản nghiệp vụ cốt lõi
**Tài liệu:** 01 Requirements
**Phiên bản:** 1.0
**Ngôn ngữ:** Tiếng Việt (UTF-8)
**Ngày rà soát:** 2026-08-28

## 1. Mục đích và nguyên tắc

Tài liệu xác định hành vi nghiệp vụ cần có của hệ thống quản lý một bãi đỗ xe: quản lý loại xe, bảng giá, vị trí đỗ, lượt xe vào/ra, thẻ/vé, phí gửi xe và báo cáo cơ bản. Đây là đầu vào cho bước Design.

Các yêu cầu trong tài liệu này không mô tả kiến trúc chi tiết, schema cơ sở dữ liệu vật lý, hợp đồng API chi tiết, bố cục UI hoặc kế hoạch triển khai. AI/ALPR không phải chức năng của phiên bản này; biển số và mã thẻ/vé được nhập hoặc mô phỏng thủ công.

## 2. Nguồn và truy vết

| Source ID | Nguồn | Nội dung dùng để đặc tả |
|---|---|---|
| SRC-001 | `prompts/00_project.md`, phần bối cảnh và vấn đề nghiệp vụ | Nhu cầu thay sổ sách thủ công, giảm nhầm lẫn, kiểm soát lượt xe, chỗ đỗ, phí và doanh thu. |
| SRC-002 | `prompts/00_project.md`, phần mục tiêu, phạm vi và ngoài phạm vi | Phạm vi nghiệp vụ cốt lõi; xác nhận chưa tích hợp AI, phần cứng, thanh toán trực tuyến và multi-site. |
| SRC-003 | `prompts/00_project.md`, phần actors và quy trình xe vào/ra | Vai trò người dùng và trình tự check-in/check-out. |
| SRC-004 | `prompts/00_project.md`, phần business rules và dữ liệu nghiệp vụ | Mã loại xe, thẻ/vé, thời gian, vị trí, tính phí và xử lý ngoại lệ. |
| SRC-005 | `prompts/00_project.md`, phần technology constraints và Project Structure | Django/Python, MSSQL, Bootstrap 5, JSON API cùng origin, các endpoint và cấu trúc app bắt buộc. |

## 3. Stakeholder và actor

| Mã | Stakeholder/actor | Mục tiêu và quyền trong phiên bản này |
|---|---|---|
| ACT-001 | Bảo vệ/Nhân viên vận hành làn xe | Ghi nhận xe vào, xe ra, thẻ/vé, vị trí và thanh toán theo quyền được cấp. |
| ACT-002 | Quản trị viên/Quản lý bãi đỗ | Quản lý loại xe, bảng giá, vị trí, người dùng/quyền và xem báo cáo. |
| ACT-003 | Khách gửi xe | Stakeholder cung cấp thông tin xe/thẻ và thanh toán thông qua nhân viên; chưa phải người dùng đăng nhập trực tiếp. |
| STK-001 | Nhóm phát triển và Tester | Sử dụng yêu cầu, truy vết và tiêu chí chấp nhận để thiết kế, triển khai và kiểm thử. |

## 4. Phạm vi

### 4.1. Trong phạm vi

- CRUD loại xe và trạng thái hoạt động/ngừng hoạt động.
- CRUD vị trí đỗ; trạng thái `Trống`, `Đang đỗ`, `Bảo trì`.
- CRUD bảng giá theo mã loại xe và cấu hình cách tính được phê duyệt.
- Ghi nhận xe vào bằng nhập tay biển số, mã loại xe, mã thẻ/vé, thời gian vào và vị trí.
- Tra cứu lượt đang đỗ; ghi nhận xe ra; tính phí; ghi nhận thanh toán.
- Cấp phát, thu hồi, báo mất và thay đổi trạng thái thẻ/vé.
- Tra cứu lịch sử theo thời gian, mã loại xe, biển số; dashboard số xe, lượt vào/ra và doanh thu ước tính.
- Tìm kiếm, lọc và phân trang các danh sách khi danh sách có hỗ trợ tương ứng.
- Xác thực, phân quyền ở mức cần thiết để bảo vệ các nghiệp vụ quản trị và vận hành.

### 4.2. Ngoài phạm vi

- Mọi mô hình AI/ALPR, nhận diện biển số, khuôn mặt, loại xe hoặc dự báo.
- Camera RTSP, RFID vật lý, barie, cảm biến, Serial/IoT và phần cứng khác.
- Thanh toán trực tuyến qua MOMO, VNPay, ZaloPay hoặc cổng bên thứ ba.
- Vé tháng/dài hạn phức tạp nếu chưa có quyết định nghiệp vụ riêng.
- Quản lý nhiều cơ sở bãi đỗ (multi-site).
- Kiến trúc chi tiết, schema cơ sở dữ liệu vật lý, API contract chi tiết, UI layout và kế hoạch triển khai.

## 5. Thuật ngữ miền

| Thuật ngữ | Định nghĩa chuẩn dùng trong tài liệu |
|---|---|
| Loại xe | Nhóm phương tiện có mã duy nhất, ví dụ `MOTORBIKE`, `CAR_4SEAT`, `TRUCK`. |
| Mã loại xe | Mã định danh dùng để chọn quy tắc giá; bắt buộc khi tạo lượt xe vào. |
| Thẻ/vé | Mã nhận diện lượt gửi, có trạng thái `Sẵn sàng`, `Đang sử dụng`, `Bị mất`, `Thu hồi`. |
| Lượt gửi xe | Bản ghi từ lúc check-in đến khi check-out; còn mở khi xe đang trong bãi. |
| Lượt xe vào (check-in) | Nghiệp vụ tạo lượt gửi, gắn thẻ/vé và chiếm một vị trí đỗ. |
| Lượt xe ra (check-out) | Nghiệp vụ xác định lượt mở, tính phí, ghi nhận thanh toán và giải phóng vị trí. |
| Vị trí đỗ | Một chỗ cụ thể trong bãi, có trạng thái và có thể được gán cho tối đa một lượt mở. |
| Bảng giá/quy tắc giá | Quy tắc tính phí theo loại xe và đơn vị thời gian/hình thức đã được phê duyệt. |
| Lượt mở | Lượt gửi có thời gian vào nhưng chưa hoàn tất xe ra. |
| Doanh thu | Tổng số tiền của các lượt đã hoàn tất và thanh toán thành công trong khoảng thời gian được chọn. |

## 6. Quy tắc nghiệp vụ và validation

| Mã | Quy tắc |
|---|---|
| BR-001 | Biển số và mã thẻ/vé là bắt buộc khi check-in; giá trị phải có định dạng hợp lệ theo quy định được cấu hình. |
| BR-002 | Mã loại xe phải tồn tại và đang hoạt động khi check-in hoặc cấu hình giá; mã không hợp lệ phải bị từ chối. |
| BR-003 | Một thẻ/vé đang hoạt động chỉ được gắn với một lượt mở tại một thời điểm. |
| BR-004 | Một biển số không được có đồng thời hai lượt mở. |
| BR-005 | Vị trí `Đang đỗ` hoặc `Bảo trì` không được gán cho lượt mới; một vị trí chỉ có tối đa một lượt mở. |
| BR-006 | Check-in hợp lệ phải ghi thời gian vào, gán vị trí, lưu mã thẻ/vé và chuyển vị trí sang `Đang đỗ`. |
| BR-007 | Xe chỉ được check-out khi tìm thấy một lượt mở hợp lệ theo mã thẻ/vé hoặc biển số. |
| BR-008 | Thời gian ra phải lớn hơn hoặc bằng thời gian vào; dữ liệu vi phạm bị từ chối. |
| BR-009 | Mức giá phải lớn hơn hoặc bằng 0. Quy tắc giá áp dụng phải khớp mã loại xe và thời điểm/hình thức gửi đã cấu hình. |
| BR-010 | Hệ thống phải tính và hiển thị số tiền phải trả trước khi xác nhận xe ra; không tự suy đoán quy tắc giá chưa được phê duyệt. |
| BR-011 | Thanh toán phải được ghi nhận thành công trước khi hoàn tất lượt xe ra theo quy định hiện tại. Thanh toán thất bại không giải phóng vị trí. |
| BR-012 | Khi xe ra và thanh toán thành công, lượt chuyển `Đã hoàn tất`, vị trí chuyển `Trống`, thẻ/vé chuyển `Sẵn sàng` nếu không bị mất/thu hồi. |
| BR-013 | Lượt hoàn tất và thanh toán phải được lưu để tra cứu và thống kê; không được tạo bản ghi một phần khi thao tác nghiệp vụ thất bại. |
| BR-014 | Báo mất thẻ/vé phải chuyển thẻ sang `Bị mất`, ngăn cấp lại/ghép với lượt mới cho đến khi được xử lý theo quy trình được phê duyệt. |
| BR-015 | Xe quá hạn theo quy định vận hành phải được đánh dấu/cảnh báo khi tra cứu hoặc check-out; cách tính phụ phí và xử lý tiếp theo là câu hỏi mở. Không tự áp dụng phạt. |
| BR-016 | Chỉ người dùng có quyền phù hợp mới được thực hiện thao tác quản trị, vận hành hoặc xem báo cáo. |

## 7. Yêu cầu chức năng

Định dạng: `Requirement ID | Type | Source ID | Priority | Status | Requirement | Acceptance Criteria`.

| Requirement ID | Type | Source ID | Priority | Status | Requirement | Acceptance Criteria |
|---|---|---|---|---|---|---|
| FR-AUTH-001 | Functional | SRC-003, SRC-005 | MUST | Confirmed | Hệ thống phải cho phép người dùng đăng nhập và đăng xuất theo quyền được cấp. | Đăng nhập đúng tạo phiên hợp lệ; sai thông tin bị từ chối; đăng xuất làm phiên hiện tại không còn truy cập nghiệp vụ bảo vệ. |
| FR-AUTH-002 | Functional | SRC-003, SRC-005 | MUST | Confirmed | Hệ thống phải kiểm soát quyền của Bảo vệ/Nhân viên và Quản trị viên. | Người không đủ quyền nhận lỗi từ chối và không làm thay đổi dữ liệu; người đủ quyền thực hiện được chức năng được cấp. |
| FR-VTYPE-001 | Functional | SRC-002, SRC-004, SRC-005 | MUST | Confirmed | Quản trị viên phải xem, thêm, sửa, xóa/ngừng hoạt động loại xe. | CRUD thành công với mã duy nhất; loại xe ngừng hoạt động không được dùng cho lượt mới; lỗi dữ liệu hiển thị rõ. |
| FR-VTYPE-002 | Functional | SRC-004 | MUST | Confirmed | Hệ thống phải quản lý mã loại xe, tên và mô tả. | Thiếu mã hoặc trùng mã bị từ chối; mã hợp lệ được lưu và tra cứu đúng. |
| FR-SPOT-001 | Functional | SRC-002, SRC-004, SRC-005 | MUST | Confirmed | Quản trị viên phải CRUD vị trí đỗ và trạng thái `Trống`, `Đang đỗ`, `Bảo trì`. | Tạo/sửa/xem/xóa vị trí hợp lệ thành công; vị trí đang có lượt mở không bị xóa hoặc làm mất liên kết. |
| FR-SPOT-002 | Functional | SRC-001, SRC-002, SRC-004 | MUST | Confirmed | Hệ thống phải hiển thị số vị trí trống và trạng thái vị trí. | Kết quả phản ánh đúng các vị trí theo trạng thái tại thời điểm truy vấn. |
| FR-PRICE-001 | Functional | SRC-002, SRC-004, SRC-005 | MUST | Confirmed | Quản trị viên phải CRUD quy tắc giá gắn với mã loại xe. | Quy tắc có giá không âm, loại xe tồn tại và trạng thái áp dụng; dữ liệu hợp lệ được lưu/hiển thị. |
| FR-PRICE-002 | Functional | SRC-002, SRC-004 | MUST | Confirmed | Hệ thống phải chọn quy tắc giá phù hợp khi tính phí theo mã loại xe và cấu hình thời gian/hình thức đã phê duyệt. | Với quy tắc đang áp dụng, cùng đầu vào cho cùng số tiền; không có quy tắc phù hợp thì từ chối check-out và nêu nguyên nhân. |
| FR-TICKET-001 | Functional | SRC-002, SRC-003, SRC-004, SRC-005 | MUST | Confirmed | Nhân viên phải ghi nhận xe vào bằng biển số, mã loại xe, mã thẻ/vé và vị trí/thời gian vào. | Dữ liệu bắt buộc hợp lệ tạo một lượt mở; vị trí thành `Đang đỗ`; thẻ/vé thành `Đang sử dụng`. |
| FR-TICKET-002 | Functional | SRC-003, SRC-004, SRC-005 | MUST | Confirmed | Hệ thống phải tìm lượt mở theo mã thẻ/vé hoặc biển số. | Tìm đúng lượt mở; nếu không tồn tại hoặc có dữ liệu trùng không hợp lệ thì không cho check-out và trả lỗi rõ ràng. |
| FR-TICKET-003 | Functional | SRC-002, SRC-003, SRC-004, SRC-005 | MUST | Confirmed | Nhân viên phải ghi nhận xe ra và thời gian ra cho lượt mở hợp lệ. | Thời gian ra không nhỏ hơn thời gian vào; dữ liệu hợp lệ chuyển lượt sang `Đã hoàn tất` sau thanh toán thành công. |
| FR-TICKET-004 | Functional | SRC-001, SRC-002, SRC-004 | MUST | Confirmed | Hệ thống phải tính và hiển thị phí đỗ xe trước khi hoàn tất xe ra. | Kết quả dùng đúng mã loại xe, thời lượng và quy tắc giá đang áp dụng; giá trị được lưu cùng lượt. |
| FR-TICKET-005 | Functional | SRC-002, SRC-004 | MUST | Confirmed | Hệ thống phải quản lý cấp phát, thu hồi và báo mất thẻ/vé. | Thẻ/vé được chuyển đúng trạng thái; thẻ `Bị mất`/`Thu hồi` không được gán cho lượt mới; thao tác báo mất được truy vấn lại được. |
| FR-PAYMENT-001 | Functional | SRC-002, SRC-004 | MUST | Confirmed | Hệ thống phải ghi nhận thanh toán của lượt xe ra và trạng thái thành công/thất bại. | Thanh toán thành công gắn đúng lượt và số tiền; thanh toán thất bại không hoàn tất lượt hoặc giải phóng vị trí. |
| FR-HISTORY-001 | Functional | SRC-001, SRC-002, SRC-004, SRC-005 | MUST | Confirmed | Người có quyền phải tra cứu lịch sử lượt gửi theo thời gian, mã loại xe và biển số. | Bộ lọc trả về đúng bản ghi; lượt đã hoàn tất vẫn truy vấn được; kết quả rỗng không báo lỗi hệ thống. |
| FR-REPORT-001 | Functional | SRC-001, SRC-002, SRC-005 | MUST | Confirmed | Dashboard/API phải cung cấp số xe đang trong bãi, lượt vào/ra trong ngày và số chỗ theo trạng thái. | Số liệu khớp các lượt mở, lượt có thời gian vào/ra và trạng thái vị trí tại thời điểm truy vấn. |
| FR-REPORT-002 | Functional | SRC-001, SRC-002, SRC-004 | SHOULD | Confirmed | Hệ thống nên cung cấp doanh thu theo khoảng thời gian. | Khoảng thời gian hợp lệ chỉ cộng các lượt thanh toán thành công và hiển thị tổng tiền cùng phạm vi thời gian. |
| FR-LIST-001 | Functional | SRC-002, SRC-005 | SHOULD | Confirmed | Các danh sách quản trị và lịch sử phải hỗ trợ tìm kiếm, lọc và phân trang phù hợp. | Tham số lọc/tìm kiếm hợp lệ giới hạn đúng kết quả; phân trang không lặp hoặc bỏ bản ghi giữa các trang. |
| FR-API-001 | Functional | SRC-005 | MUST | Confirmed | Hệ thống phải cung cấp các endpoint nghiệp vụ ở mức requirement: `GET /health/`, CRUD `/api/vehicle-types`, CRUD `/api/parking-spots`, CRUD `/api/pricing-rules`, check-in/check-out dưới `/api/tickets`, `GET /api/reports/summary`, `POST /api/dev/seed`. | Mỗi endpoint đúng HTTP method và phạm vi; endpoint health trả trạng thái; seed chỉ phục vụ dữ liệu phát triển và không thay thế nghiệp vụ thật. |

## 8. Yêu cầu phi chức năng và ràng buộc

| Requirement ID | Type | Source ID | Priority | Status | Requirement | Acceptance Criteria |
|---|---|---|---|---|---|---|
| NFR-TECH-001 | Constraint | SRC-005 | MUST | Confirmed | Backend phải dùng Django/Python và tuân thủ PEP8. | Cấu trúc và mã nguồn ở các bước sau dùng Django/Python; kiểm tra định dạng/lint không phát hiện vi phạm mới thuộc phạm vi triển khai. |
| NFR-TECH-002 | Constraint | SRC-005 | MUST | Confirmed | Cơ sở dữ liệu mặc định là Microsoft SQL Server theo cấu hình `database/db.msSQL`; không tự đổi sang SQLite. | Thiết kế/triển khai giữ tương thích với cấu hình MSSQL được dự án cung cấp; secret không nằm trong repository. |
| NFR-TECH-003 | Constraint | SRC-005 | MUST | Confirmed | Dashboard được Django render tại `/`, dùng Bootstrap 5 và gọi JSON API cùng origin. | Truy cập `/` trả dashboard; giao diện dùng Bootstrap 5; request API không yêu cầu khác origin trong môi trường mục tiêu. |
| NFR-TECH-004 | Constraint | SRC-005 | SHOULD | Confirmed | `frontend/` là scaffold Vue/React; nếu triển khai trong phạm vi này thì CRUD phải gọi API thật. | Không dùng dữ liệu giả cho luồng CRUD đã triển khai; thao tác tạo/sửa/xóa phản ánh lại từ API. |
| NFR-SEC-001 | Non-functional | SRC-002, SRC-005 | MUST | Confirmed | Không commit secret thật và không đưa thông tin xác thực nhạy cảm vào thông báo lỗi. | Quét cấu hình không có secret thật; lỗi phía người dùng không chứa mật khẩu, token hoặc thông tin kết nối. |
| NFR-DATA-001 | Non-functional | SRC-004 | MUST | Confirmed | Dữ liệu nghiệp vụ phải nhất quán khi thao tác thành công hoặc thất bại. | Check-in/check-out thất bại không để lại trạng thái dở dang giữa lượt, thẻ/vé và vị trí; thao tác thành công cập nhật các trạng thái liên quan. |
| NFR-PERF-001 | Non-functional | SRC-001 | SHOULD | Confirmed | Các thao tác nghiệp vụ chính phải phản hồi trong thời gian phù hợp với quy mô đồ án. | Trong môi trường kiểm thử của đồ án, check-in, check-out, tra cứu và summary hoàn thành trong ngưỡng được chốt ở Design/Test; chưa tự gán số mili-giây. |
| NFR-USE-001 | Non-functional | SRC-001, SRC-003 | SHOULD | Confirmed | Luồng xe vào, xe ra và thanh toán phải cung cấp thông báo lỗi rõ để nhân viên xử lý. | Người dùng biết trường nào sai, lý do không thể tiếp tục và trạng thái hiện tại; không cần suy đoán từ lỗi kỹ thuật. |

## 9. Use case chính

### UC-001 - Xe vào bãi

**Actor chính:** ACT-001. **Tiền điều kiện:** Người dùng đã đăng nhập, có loại xe hoạt động, thẻ/vé sẵn sàng và vị trí trống.

1. Nhân viên nhập biển số, chọn mã loại xe và nhập/quét mô phỏng mã thẻ/vé.
2. Hệ thống kiểm tra bắt buộc, trùng lượt mở, loại xe, thẻ/vé và vị trí.
3. Nhân viên chọn hoặc hệ thống đề xuất vị trí trống.
4. Hệ thống tạo lượt mở, ghi thời gian vào, chuyển vị trí thành `Đang đỗ` và thẻ/vé thành `Đang sử dụng`.
5. Hệ thống trả xác nhận lượt xe vào.

Ngoại lệ: thiếu/sai dữ liệu, không còn chỗ, thẻ đang dùng/bị mất/thu hồi, biển số đã có lượt mở thì từ chối và không thay đổi dữ liệu.

### UC-002 - Xe ra bãi

**Actor chính:** ACT-001. **Tiền điều kiện:** Có lượt mở và quy tắc giá phù hợp.

1. Nhân viên tra cứu bằng mã thẻ/vé hoặc biển số.
2. Hệ thống hiển thị lượt, thời gian vào và phí dự kiến theo quy tắc giá.
3. Nhân viên xác nhận số tiền và ghi nhận thanh toán.
4. Khi thanh toán thành công, hệ thống ghi thời gian ra, hoàn tất lượt, giải phóng vị trí và đưa thẻ/vé về `Sẵn sàng` nếu phù hợp.

Ngoại lệ: không tìm thấy lượt, thời gian ra sai, xe quá hạn hoặc mất thẻ, không có giá áp dụng, thanh toán thất bại. Các trường hợp chưa có quy định xử lý cuối cùng phải được cảnh báo và giữ lượt chưa hoàn tất.

### UC-003 - Cấu hình bảng giá

**Actor chính:** ACT-002. **Tiền điều kiện:** Người dùng có quyền quản trị.

1. Quản trị viên tạo/sửa quy tắc với mã loại xe, giá, đơn vị thời gian/hình thức và trạng thái áp dụng.
2. Hệ thống kiểm tra loại xe tồn tại, giá không âm và dữ liệu bắt buộc.
3. Hệ thống lưu quy tắc hợp lệ để nghiệp vụ tính phí sử dụng.

Ngoại lệ: mã loại xe không tồn tại, giá âm, dữ liệu trùng/xung đột hoặc thiếu quy tắc; hệ thống từ chối và không làm hỏng quy tắc đang dùng.

### UC-004 - Tra cứu lịch sử và báo cáo

**Actor chính:** ACT-001 hoặc ACT-002 theo quyền.

1. Người dùng chọn khoảng thời gian và tùy chọn mã loại xe/biển số.
2. Hệ thống trả lịch sử lượt gửi, trạng thái và phí; hỗ trợ tìm kiếm/lọc/phân trang.
3. Dashboard summary hiển thị xe đang trong bãi, lượt vào/ra trong ngày, trạng thái chỗ và doanh thu theo phạm vi được hỗ trợ.

## 10. Assumptions

| Mã | Giả định | Ảnh hưởng |
|---|---|---|
| ASM-001 | Phiên bản hiện tại quản lý một bãi đỗ; multi-site ngoài phạm vi. | Không đặc tả mã cơ sở hay luồng liên cơ sở. |
| ASM-002 | Nhân viên nhập tay hoặc dùng dữ liệu mô phỏng cho biển số/mã thẻ; không có AI/phần cứng. | Chỉ yêu cầu kiểm tra dữ liệu nhập và nghiệp vụ trạng thái. |
| ASM-003 | Thanh toán trong phạm vi là ghi nhận tại bãi, chưa có cổng trực tuyến. | Không yêu cầu tích hợp nhà cung cấp thanh toán. |
| ASM-004 | Thẻ/vé là định danh nghiệp vụ của lượt gửi, nhưng hình thức vật lý chưa được chốt. | Chỉ đặc tả trạng thái và mã; không đặc tả thiết bị đọc. |
| ASM-005 | MSSQL là ràng buộc đã chốt theo `SRC-005`; nội dung cũ nói SQLite được xem là không còn áp dụng. | Các bước Design/Implementation phải giữ MSSQL. |
| ASM-006 | Báo cáo doanh thu chỉ tính thanh toán thành công; đây là cách diễn giải vận hành tối thiểu. | Doanh thu chưa thanh toán không được cộng. |

## 11. Open questions và điểm mơ hồ cần xử lý trước khi đặc tả chi tiết

| Mã | Câu hỏi/điểm cần chốt | Trạng thái | Không được tự suy đoán thành |
|---|---|---|---|
| OQ-001 | Tính phí theo block giờ, ca ngày/đêm, lượt/ngày hay kết hợp? Quy tắc làm tròn thời lượng là gì? | Chưa chốt | Công thức giá cụ thể. |
| OQ-002 | Xe quá hạn được hiểu theo mốc nào và có phụ phí/khóa check-out không? | Chưa chốt | Mức phạt hoặc hành động tự động. |
| OQ-003 | Mất thẻ cần xác minh chủ xe, phạt, khóa biển số hay cấp thẻ thay thế như thế nào? | Chưa chốt | Quy trình phạt/xác minh cụ thể. |
| OQ-004 | Vị trí có giới hạn cứng theo loại xe hay cho phép đỗ linh hoạt? | Chưa chốt | Quy tắc phân bổ theo loại xe. |
| OQ-005 | Có triển khai vé tháng/dài hạn trong phiên bản này không? | Chưa chốt | Module vé tháng. |
| OQ-006 | Có bao nhiêu khu vực và có cần quản lý khu vực ngoài vị trí cụ thể không? | Chưa chốt | Mô hình khu vực chi tiết. |
| OQ-007 | Phương thức thanh toán tại bãi và có cần quản lý doanh thu theo ca nhân viên không? | Chưa chốt | Tích hợp thanh toán trực tuyến hoặc đối soát ca. |
| OQ-008 | Có cần lưu audit log người thực hiện các thao tác quan trọng không? | Chưa chốt | Yêu cầu audit bắt buộc. |
| OQ-009 | Ngưỡng hiệu năng cụ thể cho các thao tác chính là bao nhiêu? | Chưa chốt | Con số SLA trong tài liệu yêu cầu. |

## 12. Skills.sh Evidence

| Skill | Nhiệm vụ áp dụng | Đầu ra đã dùng | Vị trí bằng chứng |
|---|---|---|---|
| `software-requirements` | Chuẩn hóa ID, source, priority, status, acceptance criteria và truy vết. | Bảng yêu cầu chức năng/phi chức năng và ma trận `Source -> Requirement`. | Mục 2, 7 và 8. Tên skill không còn truy cập được tại URL tra cứu, nên áp dụng theo mục tiêu đã nêu trong prompt. |
| `domain-modeling` | Làm rõ thuật ngữ và ranh giới khái niệm của miền bãi xe. | Glossary phân biệt loại xe, thẻ/vé, lượt mở, vị trí và quy tắc giá. | Mục 5; các mã thuật ngữ được dùng nhất quán trong mục 6-9. |
| `brainstorming` | Rà soát điểm mơ hồ, giả định, mâu thuẫn và kịch bản ngoại lệ. | Tách assumptions/open questions; xử lý mất thẻ, xe quá hạn, thanh toán lỗi, sai mã loại xe. | Mục 6, 10 và 11. Skill `brainstorming` không còn được công bố tại URL tra cứu, nên áp dụng tương đương theo nhiệm vụ trong prompt. |

## 13. Quality gate và traceability

- Đã rà soát trùng lặp: các yêu cầu về check-in/check-out, giá, vị trí và thanh toán được tách theo hành vi; không có yêu cầu quan trọng không có ID.
- Đã rà soát mâu thuẫn: MSSQL trong `SRC-005` được giữ làm ràng buộc; SQLite trong tài liệu cũ không được chuyển thành yêu cầu. AI được xác nhận ngoài phạm vi.
- Các MUST requirement đều có source ID và tiêu chí chấp nhận có thể kiểm thử.
- Open questions không được dùng làm điều kiện bắt buộc để thiết kế công thức giá, phạt hoặc vé tháng.
- Ma trận hiện tại khởi tạo truy vết `Source -> Requirement`. Các bước sau phải mở rộng thành `Requirement -> Design Component -> Implementation Task -> Source Code -> Test Case -> Test Result -> Final Delivery`.

STATUS: PASS
NEXT_INPUT: docs/01_requirements.md
NEXT_PROMPT: prompts/02_design.md
TRACEABILITY_MATRIX_UPDATED: YES
