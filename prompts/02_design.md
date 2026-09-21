# 02 Design

## Role

Bạn là Software Architect, Senior Django/Backend Engineer và UI/UX Designer.

## Objective

Xác định hệ thống Quản lý bãi đỗ xe tích hợp AI sẽ được thiết kế như thế nào dựa trên requirements đã được review và chấp thuận trong `docs/01_requirements.md`. Tạo tài liệu thiết kế có traceability từ Requirement ID sang Design Component. Không viết lại toàn bộ requirements và không triển khai source code thực tế.

## Language

- Toàn bộ prompt, nội dung phân tích và artifact đầu ra phải viết bằng tiếng Việt có dấu, mã hóa UTF-8.
- Giữ nguyên tiếng Anh hoặc ký hiệu kỹ thuật đối với tên file, thư mục, command, endpoint, HTTP method, Requirement ID, Design ID, Task ID, Test ID, status marker, mã loại xe và code block.
- Không để nội dung bị lỗi mã hóa hoặc mất dấu tiếng Việt.

## Inputs

- `docs/01_requirement.md`
- `prompts/01_requirement.md`
- Các file hiện có trong repository nếu cần kiểm tra cấu trúc.

Chỉ tiếp tục nếu `docs/01_requirement.md` có:

```text
STATUS: PASS
NEXT_PROMPT: prompts/02_design.md
```

## Skills.sh

Trước khi tạo artifact, đọc hướng dẫn skill từ `skills.sh` hoặc từ Agent Skills Directory tại `https://www.skills.sh/` nếu môi trường cho phép. Nếu không thể truy cập trực tiếp, dùng skill agent tương ứng theo tên và ghi rõ cách áp dụng trong artifact.

| Skill | Mục đích | Nhiệm vụ áp dụng | Thời điểm dùng | Đầu ra mong đợi |
|---|---|---|---|---|
| `codebase-design` | Thiết kế kiến trúc & ranh giới module | Xác định boundary cho backend Django, AI inference pipeline, realtime event stream (WebSocket), API Gateway và frontend dashboard | Khi bắt đầu thiết kế | Component boundary và system sequence diagram rõ ràng |
| `django-expert` | Thiết kế Django đúng convention | Thiết kế Django settings, apps (vehicles, tickets, ai_services, billing, users), ORM models, URLs, views/serializers | Khi thiết kế backend | Architecture spec & Django project layout khả thi |
| `domain-modeling` | Thiết kế Entity, State & Business Rules | Thiết kế Vehicle, VehicleType (Mã loại xe), ParkingSpot, Ticket/Session, AI_Inference_Log, PricingPolicy, Transaction | Khi thiết kế data | ERD / Logical Data Model nhất quán, chuẩn hóa |
| `frontend-design` | Thiết kế Dashboard, Layout & Realtime UI | Thiết kế Dashboard Bootstrap/Vite-React cho bảo vệ bãi xe (xem camera realtime, cảnh báo, duyệt xe) và quản trị viên (báo cáo, doanh thu) | Khi thiết kế UI/UX | UI spec gồm wireframe flow, state management và accessibility |
| `django-security` | Thiết kế bảo mật & An toàn dữ liệu | Bảo vệ RTSP stream, mã hóa biển số/ảnh chụp (PII), CSRF, JWT, Rate Limiting cho API barrier, an toàn giao dịch thanh toán | Khi review design | Security matrix được ánh xạ trực tiếp vào design |

Trong `docs/02_design.md` phải có mục `Skills.sh Evidence`.

## Scope

- Chọn kiến trúc tổng thể.
- Thiết kế các module backend Django (Vehicles, Parking, Billing/Payment, User/Role Management).
- Thiết kế Logical Domain / Database Model (Bao gồm thực thể Xe, Mã loại xe, Thẻ/Lượt xe, Bãi/Vị trí đỗ, Hóa đơn thanh toán).
- Thiết kế API Contract (RESTful API & WebSocket endpoints cho sự kiện vào/ra realtime).
- Thiết kế giao diện Dashboard Bootstrap 5 / React scaffold (Giao diện tổng quan, Giao diện tiếp nhận xe vào, Các giao diện tra cứu, Dashboard thống kê doanh thu/mật độ, Bản đồ khu đỗ, Giao diện quản lý vé tháng, Giao diện quản lý bảng giá gửi, Giao diện quản lý nhân viên+tài khoản).
- Thiết kế validation, error handling, logging và security controls.
- Tạo bảng traceability `Requirement ID -> Design ID`.

## Out of Scope

- Không viết source code hoàn chỉnh.
- Không lập kế hoạch triển khai chi tiết từng sprint/task.
- Không lặp lại toàn bộ tài liệu requirements.
- Không thêm nghiệp vụ ngoài `docs/01_requirements.md`.

## Tasks

1. Đọc và xác nhận `docs/01_requirements.md`.
2. Trích xuất các Requirement ID quan trọng (Functional & Non-Functional, đặc biệt chú ý đến Latency của AI và độ chính xác nhận diện).
3. Áp dụng workflow skill:

```text
Xác định nhiệm vụ thiết kế -> Chọn skill từ skills.sh -> Đọc hướng dẫn skill -> Áp dụng skill -> Tạo design artifact -> Review -> Chỉnh sửa -> Validate -> Approve
```

4. Thiết kế System Architecture, Component Boundary, Domain Model (ERD), API Contract, UI/UX Workflow và Security Framework.
5. Tạo bảng traceability:

```text
Requirement ID | Design ID | Design Component | Rationale
```

## Review / Validation

`docs/02_design.md` chỉ được đặt `STATUS: PASS` khi:

- Mỗi MUST requirement (Nhận diện biển số, tính phí đỗ xe, phân loại xe qua mã loại xe, mở barie, điều khiển cổng vào/ra, báo cáo...) ánh xạ tới ít nhất một Design ID.
- Không có design component nào không gắn với requirement hoặc constraint cụ thể.
- Architecture không mâu thuẫn với cấu trúc project hiện tại.
- Tất cả các mảng Backend, API Contract, Dashboard UI, Database Schema, Validation & Security đều được bao phủ đầy đủ.
- Design không chứa source code hoàn chỉnh (chỉ chấp nhận pseudo-code, schema DDL hoặc interface definition).
- Security & Privacy review (xử lý hình ảnh cá nhân, bảo vệ camera stream) không còn BLOCKER hoặc CRITICAL.
- Có mục `Skills.sh Evidence`.
- Toàn bộ nội dung tiếng Việt có dấu đúng chuẩn UTF-8.

Nếu phát hiện requirement thiếu hoặc mâu thuẫn, đặt `STATUS: FAIL` và ghi rõ vấn đề cần quay lại bước 01 (`prompts/01_requirements.md`).

## Traceability

Bước này mở rộng:

```text
Requirement -> Design Component
```

Không copy lại toàn bộ requirements. Chỉ tham chiếu Requirement ID.

## Outputs

Tạo hoặc cập nhật:

- `docs/02_design.md`

Cuối file phải có:

```text
STATUS: PASS | FAIL
NEXT_INPUT: docs/02_design.md
NEXT_PROMPT: prompts/03_implementation_plan.md
TRACEABILITY_MATRIX_UPDATED: YES | NO
```

## Acceptance Criteria

- File `docs/02_design.md` tồn tại và đúng format.
- Bao gồm đầy đủ: System Architecture, Domain Model, AI Pipeline Spec, API Contract, UI/UX Design và Security Controls.
- Có bảng Traceability Matrix đầy đủ từ `Requirement ID -> Design ID`.
- Không chứa triển khai source code chi tiết.
- `NEXT_PROMPT` trỏ đúng `prompts/03_implementation_plan.md`.

## Handoff to Next Stage

Chỉ chuyển sang `prompts/03_implementation_plan.md` khi `docs/02_design.md` có `STATUS: PASS`.