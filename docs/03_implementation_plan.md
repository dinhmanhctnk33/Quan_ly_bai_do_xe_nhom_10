# Kế hoạch triển khai

**Hệ thống:** Hệ thống Quản lý Bãi đỗ xe - Phiên bản nghiệp vụ cốt lõi
**Tài liệu:** 03 Implementation Plan
**Phiên bản:** 1.0
**Ngày:** 2026-08-29
**Đầu vào:** `docs/01_requirements.md`, `docs/02_design.md` đều có `STATUS: PASS`

## 1. Nguyên tắc lập kế hoạch

- Kế hoạch này chuyển Design ID thành task có thứ tự, dependency, test và Definition of Done; không chứa source code triển khai.
- Áp dụng TDD theo vertical slice: trước mỗi slice xác định public seam, viết test hành vi qua endpoint hoặc interface module, triển khai tối thiểu, rồi refactor sau khi test xanh.
- Giữ ranh giới modular monolith Django hiện có: `apps/authentication`, `apps/users`, `apps/vehicles`, `apps/parking`, `apps/tickets`, `apps/reports`, `apps/core`, `config`, `templates`, `static`.
- MSSQL là database mục tiêu. SQLite chỉ có thể là adapter tạm thời cho test nếu không làm thay đổi hành vi và không thay thế cấu hình MSSQL.
- AI/ALPR, camera, WebSocket, barie, IoT, thanh toán trực tuyến và vé tháng không được triển khai. Các task tương ứng chỉ kiểm tra rằng chúng không xuất hiện trong runtime, đồng thời ghi nhận điều kiện backtrack nếu scope thay đổi.

## 2. Quy ước task và kiểm thử

Mỗi task phải tạo hoặc cập nhật test trước implementation. Test ưu tiên public seam: Django test client/DRF API, service interface đã được chốt trong Design, và giao diện quan sát được. Không kiểm thử chi tiết implementation nội bộ.

Lệnh cơ sở dùng trong kế hoạch:

- `python manage.py check`
- `python manage.py test`
- `pytest`
- `pytest apps/<module>/tests/`
- `python manage.py makemigrations --check --dry-run`
- `python manage.py migrate --plan`
- `ruff check .` hoặc công cụ lint tương đương được nhóm chốt

## 3. Danh sách task triển khai

Định dạng: `Task ID | Requirement ID | Design ID | Objective | Dependencies | Files | Tests | Verification | Definition of Done`.

| Task ID | Requirement ID | Design ID | Objective | Dependencies | Files | Tests | Verification | Definition of Done |
|---|---|---|---|---|---|---|---|---|
| TASK-001 | NFR-TECH-001, NFR-TECH-002, NFR-TECH-003, NFR-SEC-001 | DES-ARCH-001, DES-ARCH-004, DES-ARCH-006 | Chuẩn hóa settings, URL root/API, MSSQL environment, static/template, request id và logging cơ bản. | Không có | `config/settings.py`, `config/urls.py`, `.env.example`, `templates/`, `static/`, `requirements.txt` | Test `/health/`, root `/`, không lộ secret trong response/log; smoke test settings. | `python manage.py check`; `python manage.py test apps.core`; `ruff check config apps/core` | App khởi động qua cấu hình mẫu; `/health/` và `/` đúng route; không có secret thật; test và lint task xanh. |
| TASK-002 | NFR-TECH-002, NFR-DATA-001, FR-VTYPE-002, FR-SPOT-001, FR-PRICE-001, FR-TICKET-001, FR-PAYMENT-001 | DES-DOM-001..006, DES-ARCH-004 | Tạo logical entities và migrations cho loại xe, xe/biển số, vị trí, thẻ/vé, pricing rule, session và payment; áp dụng trạng thái/invariant. | TASK-001 | `apps/vehicles/models.py`, `apps/parking/models.py`, `apps/tickets/models.py`, migrations | Test entity state, mã duy nhất, giá không âm, tham chiếu hợp lệ, transition hợp lệ; test migration. | `python manage.py makemigrations --check --dry-run`; `python manage.py migrate --plan`; `pytest apps/vehicles/tests apps/parking/tests apps/tickets/tests` | Migrations chạy được trên MSSQL; entity có trạng thái đúng Design; test invariant không phụ thuộc implementation; không có schema dành riêng cho AI. |
| TASK-003 | FR-AUTH-001, FR-AUTH-002, NFR-SEC-001 | DES-ARCH-005, DES-SEC-001, DES-SEC-002 | Hoàn thiện đăng nhập/đăng xuất và permission cho ACT-001/ACT-002 ở API và dashboard. | TASK-001, TASK-002 | `apps/authentication/`, `apps/users/`, `config/settings.py`, auth templates/tests | Test đúng/sai credential, session hết hiệu lực sau logout, ACT-001/ACT-002 và anonymous; test CSRF theo cơ chế được chốt. | `pytest apps/authentication/tests apps/users/tests`; `python manage.py check --deploy` khi có cấu hình môi trường kiểm thử | Không thể gọi chức năng trái quyền; lỗi không lộ credential; cơ chế session/JWT và CSRF được ghi trong config/test; test permission xanh. |
| TASK-004 | FR-VTYPE-001, FR-VTYPE-002, FR-SPOT-001, FR-SPOT-002, FR-PRICE-001, FR-LIST-001 | DES-API-002, DES-API-003, DES-API-004, DES-UI-004, DES-UI-005, DES-ARCH-002 | Triển khai CRUD API cho loại xe, vị trí và bảng giá, gồm lọc/phân trang và trạng thái quản trị. | TASK-002, TASK-003 | `apps/vehicles/serializers.py`, `views.py`, `urls.py`; `apps/parking/serializers.py`, `views.py`, `urls.py`; dashboard templates/tests | API contract tests CRUD, mã trùng, loại xe inactive, giá âm, vị trí đang dùng không xóa; filter/pagination; forbidden. | `pytest apps/vehicles/tests apps/parking/tests`; `python manage.py test` | Endpoint đúng method/quyền; lỗi dùng envelope chuẩn; các invariant được giữ; UI quản trị phản ánh API thật và có loading/error/empty state. |
| TASK-005 | FR-PRICE-002, FR-TICKET-004, NFR-DATA-001, NFR-USE-001 | DES-ARCH-003, DES-CTRL-003, DES-DOM-006, DES-API-004 | Tạo PricingService với interface nhận loại xe, thời gian và rule đang áp dụng; chưa chốt công thức thì từ chối rõ ràng. | TASK-002, TASK-004 | `apps/tickets/services.py` hoặc module pricing trong `apps/parking/`; tests | Test giá bằng 0, loại xe hợp lệ, thiếu rule, rule inactive, thời gian không hợp lệ, kết quả ổn định; property test nếu phù hợp. | `pytest apps/parking/tests apps/tickets/tests -k pricing`; kiểm tra coverage module theo ngưỡng nhóm chốt | PricingService không nhận amount tin từ client; mọi kết quả được test qua interface; `OQ-001` được biểu diễn là cấu hình/điều kiện chờ, không tự thêm công thức. |
| TASK-006 | FR-TICKET-001..005, FR-PAYMENT-001, NFR-DATA-001, NFR-USE-001 | DES-ARCH-003, DES-API-005..007, DES-CTRL-001..005, DES-DOM-002..005, DES-UI-002/003/007 | Triển khai vertical slice check-in -> tra cứu -> tính phí -> thanh toán tại bãi -> check-out, transaction nguyên tử và xử lý mất thẻ/quá hạn. | TASK-002, TASK-003, TASK-005 | `apps/tickets/services.py`, `serializers.py`, `views.py`, `urls.py`, models/migrations, ticket UI/tests | API integration: check-in thành công; thiếu/sai mã; biển số/thẻ trùng; hết chỗ; check-out không tìm thấy; thời gian ra trước vào; payment success/failure; rollback; báo mất; cảnh báo quá hạn; concurrency hai request chiếm cùng spot/ticket. | `pytest apps/tickets/tests`; `python manage.py test apps.tickets`; chạy test MSSQL integration khi môi trường có DB | Luồng thành công cập nhật session, spot, ticket, payment trong transaction; lỗi không để trạng thái dở dang; amount lấy server; UI khóa submit khi loading và hiển thị lỗi có thể xử lý. |
| TASK-007 | FR-HISTORY-001, FR-REPORT-001, FR-REPORT-002, FR-LIST-001 | DES-API-005, DES-API-008, DES-UI-001, DES-UI-006, DES-ARCH-002 | Triển khai truy vấn lịch sử và summary dashboard theo thời gian, loại xe, biển số; tính doanh thu từ payment thành công. | TASK-002, TASK-006 | `apps/reports/services.py`, `views.py`, `urls.py`, templates/static/tests | Test bộ lọc, phân trang, dữ liệu rỗng, timezone/ngày hiện tại, session mở, lượt ra, payment failed không cộng doanh thu, summary chỗ. | `pytest apps/reports/tests`; gọi `GET /api/reports/summary`; kiểm tra query trên dữ liệu seed | Kết quả khớp fixture; không đếm payment thất bại; summary và lịch sử có quyền đúng; dashboard có loading/error/empty state và không dùng dữ liệu giả. |
| TASK-008 | NFR-TECH-003, NFR-TECH-004, NFR-USE-001 | DES-UI-001..007, DES-ARCH-001/002, DES-API-002..008 | Hoàn thiện dashboard Django Bootstrap 5: tổng quan, xe vào, xe ra/thanh toán, vị trí, lịch sử/báo cáo, loại xe/bảng giá, thẻ/vé/tài khoản. | TASK-003, TASK-004, TASK-006, TASK-007 | `templates/`, `static/css/`, `static/js/`, `frontend/` nếu được chọn, UI tests | Browser/API smoke qua Django test client; test form validation, forbidden, loading/error/empty/success, double-submit, keyboard labels; CRUD gọi API thật. | `python manage.py test`; kiểm tra asset Bootstrap 5; nếu frontend scaffold được bật thì lệnh package script tương ứng | Các màn hình trong Design hiển thị đúng dữ liệu API; responsive/accessibility cơ bản; không có camera, AI review, barie hoặc vé tháng giả trong UI. |
| TASK-009 | NFR-SEC-001, NFR-DATA-001, FR-AUTH-002 | DES-ARCH-006, DES-SEC-003..008, DES-CTRL-006 | Security hardening, error envelope, audit/log filtering, secret scan, PII handling và amount integrity. | TASK-003, TASK-006, TASK-007, TASK-008 | `config/`, middleware/logging, serializers/views/services, `.env.example`, security tests/docs | Test input whitelist, lỗi không có stack/SQL/token/password, unauthorized access, CSRF, amount client giả, secret/PII không xuất hiện trong log; dependency scan. | `python manage.py check --deploy`; `ruff check .`; secret scanner và dependency audit theo công cụ nhóm chốt; `pytest -k security` | Không còn BLOCKER/CRITICAL đã biết; log có request id nhưng loại trừ dữ liệu nhạy cảm; secret chỉ từ environment; security test và checklist được lưu. |
| TASK-010 | FR-API-001, NFR-TECH-001, NFR-TECH-002 | DES-API-001..009, DES-ARCH-001..006 | Contract verification cho endpoint bắt buộc, seed development và tính tương thích MSSQL. | TASK-001..TASK-009 | `apps/*/urls.py`, API tests, README nếu cần | Contract tests health, CRUD, check-in/check-out, summary, seed; method/status/error envelope; seed bị chặn ngoài development. | `python manage.py test`; `pytest tests/api`; `python manage.py migrate --plan` trên MSSQL | Tất cả endpoint bắt buộc có test; seed không hoạt động production; API cùng origin; tài liệu vận hành khớp route thực tế. |
| TASK-011 | NFR-TECH-004, NFR-USE-001 | DES-UI-001..007, DES-ARCH-002 | Verification-only cho scaffold `frontend/` nếu nhóm chọn React/Vue; bảo đảm không tạo mock CRUD. | TASK-004, TASK-006, TASK-007, TASK-008 | `frontend/`, package manifest/tests | Test build và browser smoke; kiểm tra các mutation gọi endpoint thật; accessibility smoke. | `npm test`/`npm run build` theo scaffold; browser test qua công cụ đã chọn | Nếu frontend được bật, build thành công và CRUD đồng bộ với API; nếu không bật, scope được ghi rõ và Django dashboard là UI thực thi. |
| TASK-012 | SRC-002, NFR-SEC-001 | DES-AI-001..004 | Scope guard cho AI/ALPR, inference log, camera RTSP, WebSocket, barie, IoT và vé tháng; không triển khai runtime. | TASK-001, TASK-008, TASK-009 | Scope tests/docs; không tạo `apps/ai_services` hoặc camera runtime | Negative tests/assertion: không có route AI/camera/WebSocket/barie; UI không có nút tương ứng; không có AI model/image table; tài liệu xác nhận disabled. | `pytest -k "scope or disabled or out_of_scope"`; tìm route/config/model cấm; review artifact | Các capability ngoài scope không xuất hiện trong endpoint, model, UI hoặc dependency bắt buộc; mọi thay đổi scope tạo backtrack về requirements/design trước khi code. |
| TASK-013 | Tất cả MUST và SHOULD đã chọn | Tất cả DES-ARCH, DES-DOM, DES-API, DES-UI, DES-CTRL, DES-SEC; không áp dụng DES-AI runtime | Regression, integration, E2E và bàn giao tài liệu. | TASK-001..TASK-012 | `tests/`, `README.md`, tài liệu test/release | Full unit/integration/API/E2E; luồng xe vào -> xe ra -> phí; quyền; rollback; summary; MSSQL smoke; no-scope tests. | `python manage.py check`; `python manage.py test`; `pytest`; lint; migration check; build frontend nếu có | Tất cả test bắt buộc xanh hoặc có defect được chấp thuận; traceability test result cập nhật; README hướng dẫn chạy; không còn BLOCKER/CRITICAL mở. |

## 4. Dependency Matrix

| Task ID | Depends On | Reason | Can Run In Parallel | Blocking Risk |
|---|---|---|---|---|
| TASK-001 | - | Nền tảng settings/routes trước mọi app. | Không | MSSQL/secret config sai chặn toàn bộ. |
| TASK-002 | TASK-001 | Model/migration cần settings và database. | Không | Entity/state sai làm hỏng mọi slice sau. |
| TASK-003 | TASK-001, TASK-002 | Permission cần user/config; có thể test độc lập một phần. | Với TASK-004 sau khi API seam mock được | Cấu hình auth/CSRF chưa chốt. |
| TASK-004 | TASK-002, TASK-003 | CRUD cần model và permission. | Với TASK-005 | API field/state không ổn định ảnh hưởng UI. |
| TASK-005 | TASK-002, TASK-004 | Pricing cần model/rule API và quyết định OQ-001. | Với TASK-004 | OQ-001 chưa chốt sẽ chặn công thức production. |
| TASK-006 | TASK-002, TASK-003, TASK-005 | Ticket orchestration cần entity, quyền, pricing. | Không | Transaction/concurrency sai gây sai dữ liệu vận hành. |
| TASK-007 | TASK-002, TASK-006 | Report cần dữ liệu session/payment thật. | Với TASK-008 sau khi API contract ổn định | Query sai làm sai doanh thu/sức chứa. |
| TASK-008 | TASK-003, TASK-004, TASK-006, TASK-007 | UI cần API và permission ổn định. | Với TASK-009, TASK-011 | UI dùng mock hoặc lệch error contract. |
| TASK-009 | TASK-003, TASK-006, TASK-007, TASK-008 | Security review cần các đường đi đã có. | Với TASK-007/TASK-008 theo module | Lộ secret/PII hoặc amount tampering. |
| TASK-010 | TASK-001..TASK-009 | Contract verification cần toàn bộ route. | Không | Endpoint thiếu hoặc seed bật sai môi trường. |
| TASK-011 | TASK-004, TASK-006, TASK-007, TASK-008 | Chỉ cần chạy khi scaffold được chọn. | Với TASK-009 | Build/toolchain frontend không sẵn sàng. |
| TASK-012 | TASK-001, TASK-008, TASK-009 | Scope guard cần kiểm tra route/UI/config cuối. | Với TASK-010 | Vô tình thêm dependency AI/hardware ngoài scope. |
| TASK-013 | TASK-001..TASK-012 | Regression và handoff sau các slice. | Không | Test chưa đủ hoặc còn blocker. |

## 5. Lộ trình triển khai

1. **Project Setup & Environment Config:** TASK-001; xác nhận Django, MSSQL, environment, health/root và logging.
2. **Database Models & Migrations:** TASK-002; chạy migration trên MSSQL, kiểm tra state/invariant.
3. **Identity và CRUD nền:** TASK-003, TASK-004; có thể song song một phần sau khi model seam ổn định.
4. **Core Business Logic & Pricing Engine:** TASK-005 rồi TASK-006; công thức cụ thể chỉ code hóa sau khi OQ-001 được chốt.
5. **Reports và Dashboard/UI:** TASK-007, TASK-008; UI chỉ dùng API thật, bao phủ các màn hình đã thiết kế. Vé tháng vẫn là placeholder bị khóa, không code nghiệp vụ.
6. **Security & Scope Guard:** TASK-009, TASK-012; review PII, secrets, transaction và bảo đảm không có AI/camera/barie runtime.
7. **Integration/E2E và Documentation:** TASK-010, TASK-011, TASK-013; đóng traceability và handoff.

Redis, Celery, OpenCV, PyTorch, event bus và WebSocket không nằm trong lộ trình thực thi phiên bản này. Chỉ bổ sung khi requirements/design được cập nhật và quality gate quay lại đạt PASS.

## 6. Test Plan

| Test ID | Phạm vi | Loại | Public seam | Điều kiện đạt |
|---|---|---|---|---|
| TEST-001 | Khởi động, root, health, MSSQL | Smoke/integration | HTTP `GET /`, `GET /health/`, Django checks | Route đúng, service healthy, không lộ config. |
| TEST-002 | Auth và permission | API/integration | Login/logout endpoint và protected endpoint | Đúng quyền hoạt động, sai quyền `FORBIDDEN`, logout vô hiệu phiên. |
| TEST-003 | VehicleType/ParkingSpot/PricingRule CRUD | API/contract | REST endpoints | CRUD, validation, status, filter/pagination đúng. |
| TEST-004 | Pricing | Unit/service | `PricingService` interface | Không âm, đúng rule, thiếu rule báo lỗi, không nhận amount từ client. |
| TEST-005 | Check-in | API/integration | `POST /api/tickets/check-in` | Tạo lượt mở và đồng bộ spot/ticket; lỗi không ghi dở dang. |
| TEST-006 | Check-out/payment | API/integration | `POST /api/tickets/check-out` | Tính phí trước xác nhận; payment success giải phóng; failure rollback. |
| TEST-007 | Ngoại lệ | API/service | Error envelope và trạng thái | Sai mã loại xe, mất thẻ, xe quá hạn, không có lượt, giờ sai, hết chỗ đều rõ và an toàn. |
| TEST-008 | History/reports | API/integration | `GET /api/tickets`, `GET /api/reports/summary` | Bộ lọc đúng; doanh thu chỉ payment success; số liệu khớp fixtures. |
| TEST-009 | Dashboard/accessibility | Browser/smoke | Form, bảng, keyboard và visible states | Bootstrap 5, label, loading/error/empty/success; mutation gọi API thật. |
| TEST-010 | Security/privacy | Security/integration | Protected API, logs, error response, config | Không secret/PII nhạy cảm trong log/error; CSRF/permission/amount integrity đạt. |
| TEST-011 | AI/hardware scope guard | Negative/verification | Route/model/UI/dependency inventory | Không có AI model, ảnh, camera, WebSocket, barie, IoT, vé tháng runtime. |
| TEST-012 | Full regression | E2E | Luồng người dùng xe vào -> xe ra | Full path và rollback xanh trên dữ liệu test; artifact test result cập nhật. |

### 6.1. AI mock tests và giới hạn phạm vi

Prompt planning yêu cầu AI pipeline mock tests, nhưng `docs/01_requirements.md` và `docs/02_design.md` xác nhận AI/ALPR ngoài phạm vi. Vì vậy không tạo sample image, model, inference worker hay test latency/accuracy. `TEST-011` chỉ là negative/scope test chứng minh pipeline không được kích hoạt. Nếu nhóm muốn tích hợp AI, phải mở `OQ` mới, cập nhật requirements (bước 01), design (bước 02), rồi lập plan lại; không dùng mock test để hợp thức hóa tính năng chưa được duyệt.

## 7. Definition of Done chung

- Task có test hành vi qua public seam và lệnh verification chạy được.
- Requirement/Design/Task/Test được truy vết; không có task không có requirement hoặc constraint.
- Code, nếu được viết ở bước kế tiếp, tuân thủ PEP8, không secret thật, không source code sinh ra trong artifact kế hoạch.
- Migration và integration test xác nhận MSSQL; transaction giữ invariant session/spot/ticket/payment.
- UI có trạng thái loading, success, validation error, business error, empty, forbidden; CRUD dùng API thật.
- Không bổ sung AI, camera, WebSocket, barie, IoT, thanh toán trực tuyến hoặc vé tháng ngoài scope.
- README và kết quả test được cập nhật trước handoff.

## 8. Rule backtrack

- Nếu phát hiện thiếu/mâu thuẫn về actor, phạm vi, mã loại xe, trạng thái, công thức phí, mất thẻ, quá hạn, vé tháng hoặc acceptance criteria: dừng task, ghi issue và quay lại `prompts/01_requirements.md`; chỉ tiếp tục sau khi `docs/01_requirements.md` đạt `STATUS: PASS`.
- Nếu requirements đủ nhưng module boundary, entity relationship, API contract, transaction, permission hoặc UI flow không triển khai được: dừng task và quay lại `prompts/02_design.md`; không tự sửa design trong lúc code.
- Nếu chỉ thiếu chi tiết implementation nhưng không đổi behavior/contract: ghi decision trong task/README và giữ trong bước implementation, không backtrack.
- Riêng công thức giá (`OQ-001`), chính sách mất thẻ/quá hạn (`OQ-002..003`), vé tháng (`OQ-005`), audit log (`OQ-008`) và SLA (`OQ-009`) là blocker tương ứng cho phần triển khai chúng; không tự suy đoán.

## 9. Traceability Matrix

| Requirement ID | Design ID | Task ID | Test Strategy |
|---|---|---|---|
| `FR-AUTH-001` | DES-ARCH-005, DES-SEC-002 | TASK-003, TASK-010 | TEST-002, TEST-010 qua auth seam. |
| `FR-AUTH-002` | DES-ARCH-005, DES-SEC-001 | TASK-003, TASK-009 | TEST-002, TEST-010 forbidden/no mutation. |
| `FR-VTYPE-001..002` | DES-DOM-001, DES-API-002, DES-UI-005 | TASK-002, TASK-004 | TEST-003. |
| `FR-SPOT-001..002` | DES-DOM-002, DES-API-003, DES-UI-004 | TASK-002, TASK-004, TASK-006 | TEST-003, TEST-005, TEST-008. |
| `FR-PRICE-001..002` | DES-DOM-006, DES-API-004, DES-CTRL-003 | TASK-002, TASK-004, TASK-005 | TEST-003, TEST-004, TEST-006. |
| `FR-TICKET-001..005` | DES-ARCH-003, DES-API-005..007, DES-DOM-003/004, DES-CTRL-001..005, DES-UI-002/003/007 | TASK-002, TASK-006, TASK-008 | TEST-005, TEST-006, TEST-007, TEST-012. |
| `FR-PAYMENT-001` | DES-DOM-005, DES-CTRL-004, DES-SEC-008 | TASK-002, TASK-006, TASK-009 | TEST-006, TEST-010. |
| `FR-HISTORY-001` | DES-API-005, DES-UI-006 | TASK-007, TASK-008 | TEST-008, TEST-009. |
| `FR-REPORT-001..002` | DES-API-008, DES-UI-001/006 | TASK-007, TASK-010 | TEST-008, TEST-012. |
| `FR-LIST-001` | DES-ARCH-002, DES-API-002..005, DES-UI-004..006 | TASK-004, TASK-007, TASK-008 | TEST-003, TEST-008, TEST-009. |
| `FR-API-001` | DES-ARCH-001/002, DES-API-001..009 | TASK-001, TASK-004, TASK-006, TASK-007, TASK-010 | TEST-001, TEST-003, TEST-005, TEST-006, TEST-008. |
| `NFR-TECH-001` | DES-ARCH-001..004 | TASK-001..TASK-013 | `manage.py check`, lint, full test. |
| `NFR-TECH-002` | DES-ARCH-004, DES-CTRL-002/004 | TASK-001, TASK-002, TASK-006, TASK-013 | MSSQL migration/integration smoke. |
| `NFR-TECH-003` | DES-ARCH-001/002, DES-UI-001 | TASK-001, TASK-008 | TEST-001, TEST-009 same-origin smoke. |
| `NFR-TECH-004` | DES-ARCH-002, DES-UI-002..006 | TASK-008, TASK-011 | TEST-009 frontend/browser build. |
| `NFR-SEC-001` | DES-ARCH-006, DES-SEC-002/003/007 | TASK-001, TASK-003, TASK-009, TASK-010 | TEST-002, TEST-010, secret scan. |
| `NFR-DATA-001` | DES-CTRL-002/004, DES-DOM-002..005 | TASK-002, TASK-005, TASK-006, TASK-009 | TEST-004..007, TEST-012 rollback/concurrency. |
| `NFR-PERF-001` | DES-ARCH-003, DES-CTRL-002, DES-UI-001/003/006 | TASK-005, TASK-006, TASK-007, TASK-013 | TEST-004, TEST-006, TEST-008; đo theo ngưỡng chốt sau OQ-009. |
| `NFR-USE-001` | DES-API-002, DES-UI-002/003, DES-CTRL-005 | TASK-004, TASK-006, TASK-008 | TEST-007, TEST-009. |
| Scope constraints for AI/hardware | DES-AI-001..004, DES-SEC-006 | TASK-008, TASK-012, TASK-013 | TEST-011 negative/scope guard. |

## 10. Design coverage và review

| Design group | Task coverage |
|---|---|
| DES-ARCH-001..006 | TASK-001, TASK-003, TASK-009, TASK-010, TASK-013 |
| DES-DOM-001..006 | TASK-002, TASK-005, TASK-006 |
| DES-AI-001..004 | TASK-012, TASK-013, chỉ verification vì `DISABLED` |
| DES-API-001..009 | TASK-001, TASK-004, TASK-006, TASK-007, TASK-010 |
| DES-UI-001..007 | TASK-004, TASK-006, TASK-007, TASK-008, TASK-011 |
| DES-CTRL-001..006 | TASK-005, TASK-006, TASK-009, TASK-013 |
| DES-SEC-001..008 | TASK-003, TASK-006, TASK-009, TASK-010, TASK-012 |

Đã kiểm tra dependency theo thứ tự Model -> Business Logic -> UI; task UI có thể chạy song song một phần sau khi API seam ổn định. Không có design component thực thi nào không gắn với requirement/constraint; các task kiểm soát AI/hardware gắn với constraint ngoài phạm vi.

## 11. Skills.sh Evidence

| Skill | Nhiệm vụ áp dụng | Đầu ra đã dùng | Vị trí bằng chứng |
|---|---|---|---|
| `tdd` | Lập kế hoạch test-first, vertical slice, test qua public seam và red-green-refactor. | Quy ước TDD, task-specific test, Test Plan và full regression. | Mục 1, 2, 3 và 6. |
| `django-expert` | Lập thứ tự settings, app, model/migration, service, serializer/view, URL và transaction Django. | Django app mapping trong task files, dependencies TASK-001 -> TASK-006 và verification commands. | Mục 3, 4 và 5. Skill không có trang công khai xác định được tại `skills.sh`, nên áp dụng theo nhiệm vụ prompt. |
| `codebase-design` | Giữ module boundary, interface sâu và dependency rõ giữa presentation, domain service, persistence adapter. | Task phân theo `config`, apps miền, services, API presentation, persistence và scope guard. | Mục 1, 3, 4 và 9. |
| `frontend-design` | Lập task UI theo workflow, state management, accessibility và API thật. | TASK-008/TASK-011, màn hình và state trong Test Plan. | Mục 3, 5 và 6. Skill không có trang công khai xác định được tại `skills.sh`, nên áp dụng theo nhiệm vụ prompt. |
| `django-security` | Lập security task về CSRF/JWT/session, PII, logging, secrets, amount integrity và verification. | TASK-003, TASK-009, security tests và secret scan. | Mục 3, 6 và 8. Skill không có trang công khai xác định được tại `skills.sh`, nên áp dụng theo nhiệm vụ prompt. |

## 12. Quality Gate và Handoff

- Đã xác nhận `docs/01_requirements.md` có `STATUS: PASS` và `NEXT_PROMPT: prompts/02_design.md`.
- Đã xác nhận `docs/02_design.md` có `STATUS: PASS` và `NEXT_PROMPT: prompts/03_implementation_plan.md`.
- Mỗi MUST requirement có ít nhất một task và test strategy; requirement ngoài scope AI/barie được xử lý bằng negative/scope verification, không triển khai giả.
- Tất cả nhóm Design ID đều có task triển khai hoặc verification tương ứng.
- Mỗi task có dependency, file scope, test, verification command và DoD.
- Không có source code hoàn chỉnh trong tài liệu; chỉ có command, interface/seam mô tả và bảng kế hoạch.
- Không có BLOCKER/CRITICAL mới; các OQ được bảo vệ bằng rule backtrack.

STATUS: PASS
NEXT_INPUT: docs/03_implementation_plan.md
NEXT_PROMPT: prompts/04_implementation.md
TRACEABILITY_MATRIX_UPDATED: YES
