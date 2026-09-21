# Báo cáo Review và Testing

**Hệ thống:** Hệ thống Quản lý Bãi đỗ xe - Phiên bản nghiệp vụ cốt lõi
**Tài liệu:** 05 Review Testing
**Ngày:** 2026-08-29
**Đầu vào:** `docs/01_requirements.md`, `docs/02_design.md`, `docs/03_implementation_plan.md`, `docs/04_implementation.md`

## 1. Kết luận review

Đã review source Django, model/migration, service, API, dashboard và test. Không phát hiện `BLOCKER` hoặc `CRITICAL`. Các defect cấu hình security phát hiện trong review đã được sửa và retest PASS.

AI/ALPR, camera RTSP, WebSocket realtime, barie, IoT, thanh toán trực tuyến và vé tháng là `DISABLED`/ngoài phạm vi theo requirements và design. Vì vậy không chạy accuracy/latency ALPR, camera stream, WebSocket payload hoặc barie test; thay vào đó đã kiểm tra scope guard bằng việc xác nhận không có runtime route/model/dependency tương ứng.

## 2. Verification result

| Test/command | Kết quả |
|---|---|
| `python manage.py check` | PASS |
| `python manage.py check --deploy` | PASS, không còn warning |
| `python manage.py makemigrations --check --dry-run` | PASS |
| `python manage.py test` | PASS, 17 tests |
| Pricing và transaction tests | PASS |
| Authentication/permission tests | PASS |
| AI/camera/WebSocket/barie | NOT APPLICABLE, đã bị khóa ngoài scope; scope guard PASS |
| MSSQL integration | DEFERRED, cần credentials/môi trường MSSQL; cấu hình MSSQL đã có |

## 3. Issue Table

| Issue ID | Severity | File | Line | Evidence | Problem | Impact | Recommendation | Status |
|---|---|---|---|---|---|---|---|---|
| REV-001 | MAJOR | `config/settings.py` | 8-10 | `check --deploy` cảnh báo secret/debug/host | Cấu hình mặc định ban đầu không an toàn cho deployment. | Có thể lộ secret hoặc cho phép host/debug không phù hợp. | Dùng environment, debug mặc định tắt, host cấu hình qua environment. | FIXED |
| REV-002 | MAJOR | `config/settings.py` | middleware/security settings | `check --deploy` cảnh báo clickjacking, cookie và HSTS | Thiếu một số security control Django. | Tăng rủi ro session hijacking/clickjacking khi triển khai. | Bổ sung XFrameOptions, secure cookie, SSL redirect và HSTS; tắt redirect riêng trong test mode. | FIXED |
| REV-003 | MAJOR | `apps/reports/views.py` | summary view | Review permission surface | Summary có thể bị gọi mà không qua authentication. | Người chưa đăng nhập có thể xem số liệu vận hành. | Bọc endpoint bằng `IsAuthenticated` và thêm test authenticated flow. | FIXED |
| REV-004 | MINOR | `apps/tickets/api_tests.py`, `apps/parking/api_tests.py` | toàn file | Django test discovery | Hai file phụ trợ không có hậu tố `tests.py` nên không tự được Django discovery chạy. | Có thể bỏ sót test nếu chỉ chạy `manage.py test`. | Test chính đã được đưa vào `tests.py`; giữ file phụ trợ để tham khảo, không dùng làm nguồn kiểm thử chính. | ACCEPTED |
| REV-005 | MINOR | môi trường kiểm thử | - | Không có DB credentials | Chưa chạy integration thật trên MSSQL. | Chưa xác nhận driver/network/schema trên MSSQL thật. | Chạy MSSQL smoke khi có credentials ngoài repository. | DEFERRED, không blocker |

## 4. Fix Log

| Issue ID | Root Cause | Files Changed | Fix Summary | Retest Command | Retest Result |
|---|---|---|---|---|---|
| REV-001 | `DEBUG=True`, `ALLOWED_HOSTS=*`, fallback secret ngắn | `config/settings.py`, `.env.example` | Debug mặc định tắt; secret/host lấy environment; bổ sung biến mẫu. | `python manage.py check --deploy` | PASS |
| REV-002 | Thiếu middleware và security settings | `config/settings.py` | Thêm clickjacking middleware, secure cookies, SSL redirect, HSTS và cờ test mode. | `python manage.py check --deploy`; `python manage.py test` | PASS |
| REV-003 | Summary dùng Django view thường không có permission decorator | `apps/reports/views.py`, `apps/tickets/tests.py` | Thêm `api_view` và `IsAuthenticated`; test gọi summary bằng user xác thực. | `python manage.py test` | PASS |

## 5. Coverage Table

| Requirement ID | Implementation Evidence | Test Case ID | Test Type | Test Result | Notes |
|---|---|---|---|---|---|
| FR-AUTH-001 | `apps/authentication/views.py` login/logout/me | TEST-AUTH-001 | Integration | PASS | Session authentication. |
| FR-AUTH-002 | `apps/permissions.py`, viewset permissions | TEST-AUTH-002 | Security/API | PASS | Nhân viên đọc, admin ghi. |
| FR-VTYPE-001 | `apps/vehicles/views.py` CRUD | TEST-CRUD-001 | API | PASS | Admin CRUD. |
| FR-VTYPE-002 | `VehicleType.code unique` | TEST-MODEL-001 | Model | PASS | Mã loại xe duy nhất. |
| FR-SPOT-001 | `apps/parking/models.py`, views | TEST-CRUD-002 | API/model | PASS | Trạng thái vị trí. |
| FR-SPOT-002 | `apps/reports/views.py` spots summary | TEST-REPORT-001 | Integration | PASS | Summary theo trạng thái. |
| FR-PRICE-001 | `PricingRule` serializer/model | TEST-MODEL-002 | Model/API | PASS | Giá không âm. |
| FR-PRICE-002 | `calculate_fee` | TEST-PRICE-001 | Service | PASS | Rule active theo loại xe. |
| FR-TICKET-001 | `check_in_vehicle`, check-in API | TEST-TICKET-001 | Integration | PASS | Đồng bộ session/spot/ticket. |
| FR-TICKET-002 | sessions API | TEST-TICKET-002 | API | PASS | Tra cứu lượt mở. |
| FR-TICKET-003 | `check_out_vehicle` | TEST-TICKET-003 | Integration | PASS | Thời gian ra hợp lệ. |
| FR-TICKET-004 | PricingService trong check-out | TEST-PRICE-001, TEST-TICKET-003 | Service/integration | PASS | Tính tiền server-side. |
| FR-TICKET-005 | Ticket status trong service | TEST-TICKET-001, TEST-TICKET-003 | Integration | PASS | Sẵn sàng/đang dùng. |
| FR-PAYMENT-001 | PaymentTransaction và atomic checkout | TEST-PAYMENT-001 | Integration | PASS | Failure giữ session active. |
| FR-HISTORY-001 | sessions query endpoint | TEST-TICKET-002 | API | PASS | Endpoint tồn tại; filter mở rộng theo kế hoạch. |
| FR-REPORT-001 | summary endpoint | TEST-REPORT-001 | Integration | PASS | Được bảo vệ authentication. |
| FR-REPORT-002 | revenue aggregation | TEST-REPORT-001 | Integration | PASS | Chỉ payment success. |
| FR-LIST-001 | DRF pagination mặc định | TEST-CRUD-001 | API | PASS | Page size 20. |
| FR-API-001 | `config/urls.py` và app URLs | TEST-API-001 | Contract/smoke | PASS | Health, auth, CRUD, ticket, summary. |
| NFR-TECH-001 | Django/Python settings và apps | TEST-SYSTEM-001 | Static/check | PASS | `check`, test suite. |
| NFR-TECH-002 | `DB_ENGINE` environment, migrations | TEST-SYSTEM-002 | Migration | PASS local | MSSQL smoke deferred do thiếu credentials. |
| NFR-TECH-003 | Django root + Bootstrap dashboard | TEST-UI-001 | Smoke | PASS | Root render, cùng-origin fetch. |
| NFR-TECH-004 | Dashboard gọi JSON API thật | TEST-UI-001 | Smoke | PASS | Không dùng mock CRUD. |
| NFR-SEC-001 | Settings, error envelope, auth | TEST-SEC-001 | Security | PASS | `check --deploy` và credential test. |
| NFR-DATA-001 | Atomic services và constraints | TEST-PAYMENT-001, TEST-TICKET-001 | Integration | PASS | Không trạng thái dở dang. |
| NFR-PERF-001 | Query/service seam | TEST-SMOKE-001 | Smoke | PASS local | SLA cụ thể vẫn chờ OQ-009. |
| NFR-USE-001 | Error response và dashboard states | TEST-TICKET-004 | API/UI | PASS | Lỗi nghiệp vụ có message rõ. |

## 6. Scope guard và test gaps

- Không có AI model, ảnh inference, camera stream, WebSocket route, barie controller hoặc IoT dependency trong runtime; đây là kết quả đúng scope, không phải thiếu chức năng đã cam kết.
- Chưa đo ALPR accuracy/latency và chưa chạy mock-image pipeline vì AI/ALPR bị loại khỏi phiên bản hiện tại. Khi scope được phê duyệt, phải quay lại requirements/design trước khi thêm test.
- MSSQL integration cần chạy riêng trong môi trường có credentials; không commit secret vào repository.
- `FR-HISTORY-001` hiện có endpoint tra cứu cơ bản; filter thời gian/loại xe đầy đủ là phần cần mở rộng tiếp theo nếu thực thi plan chi tiết hơn, nhưng không phát hiện lỗi blocker trong slice hiện tại.

## 7. Skills.sh Evidence

| Skill | Nhiệm vụ áp dụng | Bằng chứng |
|---|---|---|
| `code-review` | Review bug, regression và lệch requirements/design. | Issue Table, Coverage Table, Fix Log trong mục 3-5. Skill không có trang công khai xác định được tại `skills.sh`, áp dụng theo nhiệm vụ prompt. |
| `django-security` | Kiểm tra CSRF, secret, cookie, host, debug, permission và lỗi lộ dữ liệu. | REV-001..003, `check --deploy`, TEST-SEC-001. Skill không có trang công khai xác định được tại `skills.sh`, áp dụng theo nhiệm vụ prompt. |
| `django-expert` | Review cấu trúc app, ORM, migration, routing và test discovery. | Model/API review, REV-004, migration check. Skill không có trang công khai xác định được tại `skills.sh`, áp dụng theo nhiệm vụ prompt. |
| `diagnosing-bugs` | Tìm root cause và retest defect. | Fix Log cho REV-001..003. Skill không có trang công khai xác định được tại `skills.sh`, áp dụng theo nhiệm vụ prompt. |
| `tdd` | Bổ sung regression test qua public seam sau mỗi defect. | Authentication, permission, pricing, transaction và API tests; 17/17 PASS. |

## 8. Quality Gate và Handoff

- Không còn `BLOCKER` hoặc `CRITICAL`.
- Các issue `MAJOR` đã được sửa và retest PASS.
- Django check, deployment security check, migration check và 17 test đều PASS.
- Coverage Table đã ánh xạ từng Requirement ID sang source/test/result.
- Các capability ngoài phạm vi được scope guard, không bị giả định thành runtime feature.

STATUS: PASS
NEXT_INPUT: reviewed source code, tests, docs/05_review_testing.md
NEXT_PROMPT: prompts/06_final_delivery.md
TRACEABILITY_MATRIX_UPDATED: YES
BACKTRACK_REQUIRED: NONE
