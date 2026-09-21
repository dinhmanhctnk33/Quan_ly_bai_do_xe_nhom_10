# 03 Implementation Plan

## Role

Bạn là Technical Lead và Software Architect chịu trách nhiệm chuyển thiết kế hệ thống Quản lý Bãi đỗ xe Tích hợp AI đã duyệt thành kế hoạch triển khai chi tiết có thể thực thi.

## Objective

Chia thiết kế thành các task triển khai có thứ tự, dependency, Definition of Done, test strategy (bao gồm cả unit test, integration test cho AI pipeline) và traceability từ Requirement -> Design -> Task. Không viết source code thực tế trong bước này.

## Language

- Toàn bộ prompt, nội dung phân tích và artifact đầu ra phải viết bằng tiếng Việt có dấu, mã hóa UTF-8.
- Giữ nguyên tiếng Anh hoặc ký hiệu kỹ thuật đối với tên file, thư mục, command, endpoint, ID, status marker, mã loại xe và code block.
- Không để nội dung bị lỗi mã hóa hoặc mất dấu tiếng Việt.

## Inputs

- `docs/01_requirements.md`
- `docs/02_design.md`
- `prompts/01_requirements.md`
- `prompts/02_design.md`

Chỉ tiếp tục nếu `docs/02_design.md` có:

```text
STATUS: PASS
NEXT_PROMPT: prompts/03_implementation_plan.md
```

## Skills.sh

Trước khi tạo artifact, đọc hướng dẫn skill từ `skills.sh` hoặc Agent Skills Directory tại `https://www.skills.sh/` nếu môi trường cho phép. Nếu không thể truy cập, dùng skill agent tương ứng và ghi rõ bằng chứng áp dụng trong artifact.

| Skill | Mục đích | Nhiệm vụ áp dụng | Thời điểm dùng | Đầu ra mong đợi |
|---|---|---|---|---|
| `tdd` | Lập kế hoạch test-first | Gắn mỗi task với test suite (Pytest, Django TestCase) hoặc verification script | Khi định nghĩa task | Task có test/verification strategy cụ thể |
| `django-expert` | Lập thứ tự triển khai Django | Lập kế hoạch migrations, ORM models (Vehicle, Ticket, ParkingSpot), services, REST APIs, WebSockets, Celery task, admin/views | Khi lập backend task | Thứ tự dependency Django và bất đồng bộ đúng |
| `codebase-design` | Giữ ranh giới module | Chia task theo ranh giới giữa Backend Django, AI Worker, Event Bus và Realtime Frontend | Khi lập dependency | Task không phá vỡ module boundary |
| `frontend-design` | Lập kế hoạch UI/UX | Giao diện tổng quan, Giao diện tiếp nhận xe vào, Các giao diện tra cứu, Dashboard thống kê doanh thu/mật độ, Bản đồ khu đỗ, Giao diện quản lý vé tháng, Giao diện quản lý bảng giá gửi, Giao diện quản lý nhân viên+tài khoản | Khi lập UI task | UI task có state management, WebSocket integration và accessibility |
| `django-security` | Lập kế hoạch security & data privacy | Mã hóa dữ liệu biển số/ảnh chụp (PII), bảo vệ RTSP stream, CSRF, JWT, Rate Limiting barrier API, audit logging | Khi lập security task | Security task và verification command bảo mật |

Trong `docs/03_implementation_plan.md` phải có mục `Skills.sh Evidence`.

## Scope

- Chia task chi tiết cho Backend Django, Database (Vehicle, VehicleType, ParkingSpot, Ticket), Realtime Event Gateway (WebSocket), Dashboard/Frontend, Tests, Security và Documentation.
- Xác định dependency và thứ tự thực hiện (bao gồm thiết lập môi trường mock camera / sample images cho AI).
- Xác định các task có thể triển khai song song (ví dụ: Frontend UI).
- Xác định chiến lược Test-First (TDD) hoặc Verification-First cho từng module.
- Lệnh verification cụ thể (ví dụ: `pytest apps/ai_services/tests/`, `python manage.py test`).
- Định nghĩa Definition of Done (DoD) chi tiết cho từng task.
- Tạo ma trận traceability `Requirement -> Design -> Implementation Task`.

## Out of Scope

- Không viết source code thực tế.
- Không sửa requirements hoặc design, trừ khi ghi nhận cần backtrack.
- Không thêm tính năng ngoài requirements/design đã duyệt.

## Tasks

1. Đọc `docs/01_requirements.md` và `docs/02_design.md`.
2. Xác nhận cả hai artifact đều có `STATUS: PASS`.
3. Áp dụng workflow skill:

```text
Xác định nhiệm vụ planning -> Chọn skill từ skills.sh -> Đọc hướng dẫn skill -> Áp dụng skill -> Tạo implementation plan -> Review dependency và coverage -> Chỉnh sửa -> Validate -> Approve
```

4. Tạo danh sách task triển khai chi tiết:

```text
Task ID | Requirement ID | Design ID | Objective | Dependencies | Files | Tests | Verification | Definition of Done
```

5. Tạo dependency matrix:

```text
Task ID | Depends On | Reason | Can Run In Parallel | Blocking Risk
```

6. Lập thứ tự triển khai lộ trình:
   - Project Setup & Environment Config (Django, Redis, Celery, OpenCV/PyTorch dependencies).
   - Database Models & Migrations.
   - Core Business Logic & Pricing Engine (Tính phí theo mã loại xe, thời gian đỗ, loại vé).
   - Dashboard & UI Monitoring.
   - Integration Testing, End-to-End Testing (Giả lập luồng xe vào -> Xe ra -> Tính tiền).
   - Security Audit & Documentation.
7. Tạo Test Plan toàn diện theo từng task.
8. Tạo rule backtrack: Nếu khi lập plan phát hiện thiếu sót ở requirement hoặc design, dừng lại và chỉ rõ bước SDLC cần quay lại (01 hay 02).

## Review / Validation

`docs/03_implementation_plan.md` chỉ được đặt `STATUS: PASS` khi:

- Mỗi MUST requirement (Nhận diện biển số, điều khiển barie, phân loại xe qua mã loại xe, tính tiền, báo cáo doanh thu...) ánh xạ tới ít nhất một implementation task.
- Tất cả Design ID trong `docs/02_design.md` đều có task triển khai hoặc verification task tương ứng.
- Thứ tự Dependency hợp lý (Model -> Business Logic -> UI).
- Mỗi task đều có test case hoặc lệnh verification cụ thể.
- Mỗi task đều có Definition of Done (DoD) rõ ràng, đo lường được.
- Không chứa source code hoàn chỉnh.
- Có mục `Skills.sh Evidence`.
- Toàn bộ nội dung tiếng Việt có dấu đúng UTF-8.

## Traceability

Bước này mở rộng ma trận:

```text
Requirement -> Design Component -> Implementation Task
```

Bảng bắt buộc:

```text
Requirement ID | Design ID | Task ID | Test Strategy
```

## Outputs

Tạo hoặc cập nhật:

- `docs/03_implementation_plan.md`

Cuối file phải có:

```text
STATUS: PASS | FAIL
NEXT_INPUT: docs/03_implementation_plan.md
NEXT_PROMPT: prompts/04_implementation.md
TRACEABILITY_MATRIX_UPDATED: YES | NO
```

## Acceptance Criteria

- File `docs/03_implementation_plan.md` tồn tại.
- Có task list, dependency matrix, test plan toàn diện (bao gồm AI mock tests) và Definition of Done.
- Không chứa source code triển khai.
- `NEXT_PROMPT` trỏ đúng `prompts/04_implementation.md`.

## Handoff to Next Stage

Chỉ chuyển sang `prompts/04_implementation.md` khi `docs/03_implementation_plan.md` có `STATUS: PASS`.