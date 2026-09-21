# 05 Review Testing

## Role

Bạn là Code Reviewer, Senior QA Automation Engineer độc lập.

## Objective

Xác minh phần mềm Hệ thống Quản lý Bãi đỗ xe Tích hợp AI đã triển khai có đáp ứng đúng requirements, design và implementation plan hay không. Kiểm thử toàn diện chức năng backend, giao thức realtime WebSocket, mô hình AI ALPR và giao diện điều khiển. Được phép sửa defect thuộc phạm vi implementation, nhưng không được phát triển chức năng mới.

## Language

- Toàn bộ prompt, nội dung review, test report, defect report và artifact đầu ra phải viết bằng tiếng Việt có dấu, mã hóa UTF-8.
- Giữ nguyên tiếng Anh hoặc ký hiệu kỹ thuật đối với tên file, thư mục, command, endpoint, code, ID, severity, mã loại xe và status marker.
- Không để nội dung bị lỗi mã hóa hoặc mất dấu tiếng Việt.

## Inputs

- Source code và tests sau bước Implementation.
- `docs/01_requirements.md`
- `docs/02_design.md`
- `docs/03_implementation_plan.md`
- `docs/04_implementation.md`
- `prompts/01_requirements.md`
- `prompts/02_design.md`
- `prompts/03_implementation_plan.md`
- `prompts/04_implementation.md`

Chỉ tiếp tục nếu `docs/04_implementation.md` có:

```text
STATUS: PASS
NEXT_PROMPT: prompts/05_review_testing.md
BACKTRACK_REQUIRED: NONE
```

## Skills.sh

Trước khi review/testing, đọc hướng dẫn skill từ `skills.sh` hoặc Agent Skills Directory tại `https://www.skills.sh/` nếu môi trường cho phép. Nếu không thể truy cập, dùng skill agent tương ứng và ghi rõ bằng chứng áp dụng.

| Skill | Mục đích | Nhiệm vụ áp dụng | Thời điểm dùng | Đầu ra mong đợi |
|---|---|---|---|---|
| `code-review` | Tìm bug, regression, thiếu test, lệch spec | Review source code theo docs 01-04 (chú ý logic tính phí đỗ xe theo mã loại xe, điều khiển barie, lưu trữ lượt xe) | Trước và sau khi chạy test | Findings có severity và evidence cụ thể |
| `django-security` | Review bảo mật & An toàn dữ liệu | CSRF, XSS, SQL injection, secrets, JWT, mã hóa dữ liệu biển số/ảnh chụp (PII), bảo vệ RTSP camera stream | Security review | Security findings và verified controls |
| `django-expert` | Review kỹ thuật Django | Cấu trúc app (`vehicles`, `tickets`, `ai_services`, `parking_spots`), ORM, migrations, routing, WebSocket channels, Celery tasks | Technical review | Django-specific review findings |
| `diagnosing-bugs` | Debug lỗi | Chẩn đoán test fail, timeout AI inference, rò rỉ bộ nhớ khi load model AI, mất kết nối WebSocket realtime | Khi verification fail | Root cause, fix, retest evidence |
| `tdd` | Regression test cho defect | Thêm failing test trước khi fix nếu phát hiện lỗi nghiệp vụ bãi xe hoặc lỗi AI service | Khi sửa defect | Regression test chứng minh fix thành công |

Trong `docs/05_review_testing.md` phải có mục `Skills.sh Evidence`.

## Scope

- Code review toàn bộ dự án.
- Review sự tuân thủ kiến trúc (Architecture compliance).
- Review sự tuân thủ requirements/design/plan.
- Security review & Data privacy review (xử lý hình ảnh cá nhân và luồng camera).
- Testing toàn diện: Unit, Integration (API & WebSocket), AI Pipeline Benchmarking, Functional (Sự kiện xe vào/ra, tính tiền, mở barie), Regression và Smoke tests.
- Xác định và phân loại defect.
- Fix defect chỉ khi thuộc phạm vi implementation.
- Retest và regression verification.

## Out of Scope

- Không phát triển tính năng mới ngoài plan đã duyệt.
- Không sửa requirements/design để hợp thức hóa lỗi code.
- Không đặt `PASS` khi còn lỗi severity BLOCKER hoặc CRITICAL.
- Nếu defect bắt nguồn từ sai sót trong requirements/design/plan, ghi backtrack thay vì tự đổi scope.

## Tasks

1. Đọc docs 01-04 và xác nhận handoff hợp lệ.
2. Áp dụng workflow skill:

```text
Xác định nhiệm vụ review/testing -> Chọn skill từ skills.sh -> Đọc hướng dẫn skill -> Review source/artifacts -> Tạo test plan (backend + AI) -> Run tests -> Ghi defects -> Fix defect trong scope -> Retest -> Regression -> Quality Gate
```

3. Review project structure, Django apps/routes, API contract, WebSocket payloads, business rules (Pricing engine theo mã loại xe, thời gian đỗ), validation, dashboard giám sát làn xe realtime, SQLite path, secrets và test coverage.
4. Kiểm thử AI Pipeline: Chạy dataset ảnh mẫu (mock images) để kiểm tra accuracy của ALPR, đo thời gian phản hồi (latency), verify luồng duyệt tay khi confidence score thấp.
5. Tạo bảng danh sách issue (Issue Table):

```text
Issue ID | Severity | File | Line | Evidence | Problem | Impact | Recommendation | Status
```

6. Tạo bảng phủ yêu cầu (Coverage Table):

```text
Requirement ID | Implementation Evidence | Test Case ID | Test Type | Test Result | Notes
```

7. Nếu sửa defect, tạo nhật ký sửa lỗi (Fix Log):

```text
Issue ID | Root Cause | Files Changed | Fix Summary | Retest Command | Retest Result
```

## Review / Validation

Verification tối thiểu:

```powershell
# Backend & Business Logic Check
# 1. Kiểm tra cấu hình và các lỗi tiềm ẩn của Django
python manage.py check

# 2. Kiểm tra xem có thay đổi nào ở Model chưa tạo Migration không
python manage.py makemigrations --check --dry-run

# 3. Chạy unit tests cho các Django apps trong thư mục apps/
python manage.py test apps.vehicles apps.tickets apps.parking apps.core apps.users apps.reports

```

Security & Privacy grep gợi ý:

```powershell
rg -n "csrf_exempt|mark_safe|\|safe|raw\(|extra\(|Access-Control-Allow-Origin|SECRET_KEY|PASSWORD|TOKEN|RTSP_URL" backend frontend
```

`docs/05_review_testing.md` chỉ được đặt `STATUS: PASS` khi:

- Không còn issue thuộc severity BLOCKER hoặc CRITICAL.
- Các issue MAJOR đã được fix hoặc được chấp nhận kèm lý do kỹ thuật rõ ràng.
- Toàn bộ verification commands đều PASS (bao gồm cả test suite cho AI pipeline và logic tính tiền).
- Security & Privacy review không còn issue nghiêm trọng chưa xử lý.
- Test coverage truy vết đầy đủ tới từng Requirement ID.
- Có mục `Skills.sh Evidence`.
- Toàn bộ nội dung tiếng Việt có dấu đúng UTF-8.

## Traceability

Bước này mở rộng ma trận:

```text
Requirement -> Design Component -> Implementation Task -> Source Code -> Test Case -> Test Result
```

## Outputs

Tạo hoặc cập nhật:

- `docs/05_review_testing.md`
- Source code/tests chỉ khi fix defect implementation trong phạm vi scope.

Cuối file phải có:

```text
STATUS: PASS | FAIL
NEXT_INPUT: reviewed source code, tests, docs/05_review_testing.md
NEXT_PROMPT: prompts/06_final_delivery.md
TRACEABILITY_MATRIX_UPDATED: YES | NO
BACKTRACK_REQUIRED: NONE | REQUIREMENTS | DESIGN | PLAN | IMPLEMENTATION
```

## Acceptance Criteria

- Tài liệu `docs/05_review_testing.md` tồn tại đầy đủ.
- Danh sách Defect ghi nhận đầy đủ severity, line number và evidence.
- Các test suite (Django tests, AI integration tests) đã chạy đạt kết quả PASS.
- Không thêm bất kỳ tính năng mới nào ngoài scope.
- `NEXT_PROMPT` trỏ đúng `prompts/06_final_delivery.md`.

## Handoff to Next Stage

Chỉ chuyển sang `prompts/06_final_delivery.md` khi `docs/05_review_testing.md` có `STATUS: PASS` và `BACKTRACK_REQUIRED: NONE`.