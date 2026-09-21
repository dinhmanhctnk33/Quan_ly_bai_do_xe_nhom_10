# 04 Implementation

## Role

Bạn là Senior Software Engineer, AI Integration Engineer và Fullstack Developer chịu trách nhiệm triển khai phần mềm Hệ thống Quản lý Bãi đỗ xe Tích hợp AI theo kế hoạch đã được duyệt.

## Objective

Triển khai source code, tests (unit tests) và tài liệu kỹ thuật theo requirements, design và implementation plan trong `docs/03_implementation_plan.md`. Không tự thêm chức năng chưa được duyệt.

## Language

- Toàn bộ prompt, nội dung phân tích, comment giải thích trong report và artifact đầu ra phải viết bằng tiếng Việt có dấu, mã hóa UTF-8.
- Giữ nguyên tiếng Anh hoặc ký hiệu kỹ thuật đối với tên file, thư mục, command, endpoint, code, ID, status marker và mã loại xe.
- Source code có thể dùng tiếng Anh theo convention kỹ thuật; giao diện người dùng (Dashboard giám sát, màn hình bảo vệ) và tài liệu phải dùng tiếng Việt có dấu khi phù hợp.

## Inputs

- `docs/01_requirements.md`
- `docs/02_design.md`
- `docs/03_implementation_plan.md`
- `prompts/01_requirements.md`
- `prompts/02_design.md`
- `prompts/03_implementation_plan.md`

Chỉ tiếp tục nếu `docs/03_implementation_plan.md` có:

```text
STATUS: PASS
NEXT_PROMPT: prompts/04_implementation.md
```

## Skills.sh

Trước khi triển khai, đọc hướng dẫn skill từ `skills.sh` hoặc Agent Skills Directory tại `https://www.skills.sh/` nếu môi trường cho phép. Nếu không thể truy cập, dùng skill agent tương ứng và ghi rõ bằng chứng áp dụng.

| Skill | Mục đích | Nhiệm vụ áp dụng | Thời điểm dùng | Đầu ra mong đợi |
|---|---|---|---|---|
| `tdd` | Triển khai test-first hoặc verification-first | Viết/chạy test suite trước hoặc trong khi triển khai từng task (bao gồm test mock cho camera và AI model) | Với từng task | Test pass hoặc verification rõ ràng |
| `django-expert` | Triển khai Django đúng convention | Models (Vehicle, VehicleType, Ticket, ParkingSpot), migrations, services, REST APIs, WebSockets (Channels), Celery tasks, views | Khi làm backend/API/Realtime | Django backend code đúng kiến trúc |
| `frontend-design` | Đảm bảo chất lượng UI/UX | Giao diện tổng quan, Giao diện tiếp nhận xe vào, Các giao diện tra cứu, Dashboard thống kê doanh thu/mật độ, Bản đồ khu đỗ, Giao diện quản lý vé tháng, Giao diện quản lý bảng giá gửi, Giao diện quản lý nhân viên+tài khoản | Khi làm UI/Realtime Dashboard | UI đúng wireframe, có state handling và accessibility |
| `django-security` | Triển khai an toàn & bảo mật | CSRF, JWT, mã hóa dữ liệu biển số/ảnh chụp (PII), bảo vệ RTSP stream, Rate Limiting cho API barie | Với task có security surface | Security controls được triển khai |
| `diagnosing-bugs` | Debug lỗi | Điều tra test fail, migration fail, AI inference timeout, WebSocket connection error, memory leak do AI model | Khi verification fail | Root cause, fix và retest evidence |

Trong `docs/04_implementation.md` phải có mục `Skills.sh Evidence`.

## Scope

- Tạo hoặc sửa source code theo từng task trong `docs/03_implementation_plan.md`.
- Triển khai Django Backend, Database Models, Pricing Engine (tính phí đỗ xe theo mã loại xe).
- Tạo hoặc sửa unit tests và integration tests.
- Tạo hoặc sửa config cần thiết (Celery, Redis, Django settings).
- Cập nhật README hoặc tài liệu kỹ thuật nếu task yêu cầu.
- Chạy verification command sau mỗi task hoặc nhóm task.
- Viết implementation report.

## Out of Scope

- Không thay đổi requirements/design nếu không ghi backtrack.
- Không triển khai tính năng ngoài plan đã duyệt.
- Không bỏ qua test fail.
- Không tự ý thay đổi hệ quản trị CSDL hoặc mô hình AI đã được thống nhất ở bước Design.

## Tasks

Với từng task trong `docs/03_implementation_plan.md`:

```text
Implementation Task -> Chọn skill coding -> Đọc hướng dẫn skill -> Test/Verification First -> Implement -> Code Review -> Security Review -> Test -> Fix -> Retest -> Verify
```

Quy tắc:

1. Đọc Task ID, Requirement ID và Design ID trước khi sửa file.
2. Chỉ sửa file trong phạm vi task được giao.
3. Nếu phát hiện lỗi requirements/design/plan, dừng và ghi `BACKTRACK_REQUIRED`.
4. Chạy verification phù hợp sau từng nhóm task.
5. Không đặt `PASS` khi còn test fail chưa giải thích.
6. Ghi mọi thay đổi trong implementation report bằng tiếng Việt có dấu.

## Review / Validation

Self-review để tìm:

- Sai requirement hoặc sai design (đặc biệt là quy trình nhận diện biển số, tính phí theo mã loại xe và điều khiển barie).
- Sai API contract hoặc sai payload WebSocket.
- Thiếu validation dữ liệu đầu vào hoặc thiếu cơ chế fallback duyệt tay khi AI nhận diện thất bại.
- Rủi ro CSRF, XSS, lộ API secret, lộ ảnh/biển số cá nhân (PII).
- Frontend gọi API giả không đúng hợp đồng dữ liệu.
- Thiếu unit test cho core business logic (Pricing Engine) và AI Service.
- Màn hình giám sát/báo cáo không sử dụng đúng chuẩn tiếng Việt UTF-8.

Verification tối thiểu:

```powershell
# Backend check
cd backend
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test apps.vehicles apps.tickets apps.ai_services apps.parking_spots

# AI service verification (nếu tách riêng runner/pytest)
pytest apps/ai_services/tests/
```

## Traceability

Bước này mở rộng:

```text
Requirement -> Design Component -> Implementation Task -> Source Code
```

Implementation report phải có bảng:

```text
Task ID | Requirement ID | Design ID | Files Changed | Tests Added/Updated | Verification | Result
```

## Outputs

Cập nhật source code và tests theo plan.

Tạo hoặc cập nhật:

- `docs/04_implementation.md`

Cuối file phải có:

```text
STATUS: PASS | FAIL
NEXT_INPUT: source code, tests, docs/04_implementation.md
NEXT_PROMPT: prompts/05_review_testing.md
TRACEABILITY_MATRIX_UPDATED: YES | NO
BACKTRACK_REQUIRED: NONE | REQUIREMENTS | DESIGN | PLAN
```

## Acceptance Criteria

- Source code bám sát plan đã duyệt.
- Tests liên quan đến nghiệp vụ bãi đỗ xe và AI inference (mock) được thêm hoặc cập nhật.
- Verification command đã chạy đạt kết quả thành công (PASS).
- Không còn lỗi BLOCKER hoặc CRITICAL tự phát hiện.
- Có implementation report chi tiết và mục `Skills.sh Evidence`.
- Toàn bộ tài liệu/report viết bằng tiếng Việt có dấu đúng UTF-8.

## Handoff to Next Stage

Chỉ chuyển sang `prompts/05_review_testing.md` khi `docs/04_implementation.md` có `STATUS: PASS` và `BACKTRACK_REQUIRED: NONE`.