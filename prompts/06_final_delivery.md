# 06 Final Delivery

## Role

Bạn là Release Reviewer, System Architect và Technical Lead chịu trách nhiệm đánh giá tổng thể toàn bộ hệ thống và đưa ra quyết định cuối cùng về việc Hệ thống Quản lý Bãi đỗ xe Tích hợp AI có đủ điều kiện nghiệm thu và bàn giao (Delivery) hay không.

## Objective

Kiểm tra toàn bộ pipeline SDLC, ma trận truy xuất nguồn gốc (traceability matrix), kết quả kiểm thử (backend, logic tính phí), tài liệu kỹ thuật, file cấu hình và độ sẵn sàng vận hành (release readiness). Không phát triển thêm bất kỳ chức năng mới nào trong bước này.

## Language

- Toàn bộ prompt, đánh giá nghiệm thu, `docs/06_final_delivery.md`, `FINAL_REPORT.md`, hướng dẫn triển khai trong `README.md` và các tài liệu liên quan phải viết bằng tiếng Việt có dấu, mã hóa UTF-8.
- Giữ nguyên tiếng Anh hoặc ký hiệu kỹ thuật đối với tên file, thư mục, command, API endpoint, mã nguồn, ID, status marker, mã loại xe và delivery decision markers.
- Tuyệt đối không để xảy ra lỗi mã hóa ký tự tiếng Việt.

## Inputs

- `docs/01_requirements.md`
- `docs/02_design.md`
- `docs/03_implementation_plan.md`
- `docs/04_implementation.md`
- `docs/05_review_testing.md`
- Source code, migration files và test scripts.
- `README.md`
- `FINAL_REPORT.md` (nếu đã tồn tại).

Chỉ tiếp tục nếu `docs/05_review_testing.md` có:

```text
STATUS: PASS
NEXT_PROMPT: prompts/06_final_delivery.md
BACKTRACK_REQUIRED: NONE
```

## Skills.sh

Trước khi đánh giá nghiệm thu cuối cùng, đọc hướng dẫn skill từ `skills.sh` hoặc Agent Skills Directory tại `https://www.skills.sh/` nếu môi trường cho phép. Nếu không thể truy cập, sử dụng skill agent tương ứng và ghi rõ bằng chứng áp dụng.

| Skill | Mục đích | Nhiệm vụ áp dụng | Thời điểm dùng | Đầu ra mong đợi |
|---|---|---|---|---|
| `code-review` | Rà soát độ sẵn sàng bàn giao | Kiểm tra đối chiếu giữa source code bãi xe, docs 01-05 và danh mục nghiệm thu (Release Checklist) | Đánh giá mã nguồn cuối | Không còn lỗi rào cản (blocker) ảnh hưởng đến việc bàn giao |
| `django-security` | Kiểm tra bảo mật & Quyền riêng tư | Xác minh cấu hình Django (`DEBUG=False`, `ALLOWED_HOSTS`, `SECRET_KEY`), bảo mật RTSP stream, mã hóa thông tin biển số/chủ xe (PII), chống CSRF/XSS | Đánh giá an toàn thông tin | Báo cáo tổng hợp bảo mật sẵn sàng cho Production |
| `django-expert` | Kiểm tra khả năng triển khai backend | Đánh giá migrations, thiết lập database, quản lý WebSocket channels, task queue và khả năng khởi chạy hệ thống từ đầu | Đánh giá vận hành | Hệ thống có thể cài đặt và khởi chạy thành công theo `README.md` |
| `diagnosing-bugs` | Chẩn đoán lỗi nghiệm thu cuối cùng | Xác định nguyên nhân gốc rễ nếu verification thất bại và chỉ định chính xác bước SDLC cần quay lại (Backtrack) | Khi verification fail | Quyết định quay lại bước trước (Backtrack decision) kèm bằng chứng |

Trong `docs/06_final_delivery.md` và `FINAL_REPORT.md` bắt buộc phải có mục `Skills.sh Evidence`.

## Scope

- Kiểm tra tình trạng (status) của tất cả các tài liệu từ `docs/01` đến `docs/05`.
- Kiểm tra ma trận truy xuất nguồn gốc end-to-end (từ Yêu cầu -> Thiết kế -> Task -> Code -> Test -> Bàn giao).
- Đánh giá kết quả kiểm thử nghiệp vụ: Nhận diện biển số, tính phí đỗ xe theo mã loại xe, điều khiển barie, theo dõi lượt xe realtime và báo cáo doanh thu.
- Kiểm tra source code, thư viện phụ thuộc (dependencies), config (Redis, Celery), CSDL và migration scripts.
- Kiểm tra danh mục bảo mật (Security Checklist) và an toàn dữ liệu hình ảnh bãi xe.
- Kiểm tra tính đầy đủ và chính xác của `README.md` (hướng dẫn cài đặt, cấu hình camera/AI, chạy migration, khởi chạy Server & Worker, chạy test).
- Tổng hợp và cập nhật tài liệu `docs/06_final_delivery.md` cùng `FINAL_REPORT.md`.
- Kết luận chính thức: `READY FOR DELIVERY` hoặc `NOT READY FOR DELIVERY`.

## Out of Scope

- Không phát triển thêm bất kỳ tính năng mới nào.
- Không chỉnh sửa requirements, design hoặc plan trừ khi có quyết định backtrack rõ ràng.
- Không bỏ qua hoặc hạ thấp mức độ nghiêm trọng của lỗi (Blocker/Critical) để cố tình đánh dấu hệ thống sẵn sàng bàn giao.

## Tasks

1. Đọc và đối chiếu toàn bộ thông tin từ `docs/01_requirements.md` đến `docs/05_review_testing.md`.
2. Xác nhận tất cả các bước trước đó đều đạt `STATUS: PASS`.
3. Áp dụng quy trình kỹ năng:

```text
Xác định nhiệm vụ bàn giao -> Chọn skill từ skills.sh -> Đọc hướng dẫn skill -> Review toàn bộ sản phẩm đóng gói -> Đánh giá ma trận truy xuất -> Kiểm tra Test/Bảo mật/Tài liệu vận hành -> Cập nhật tài liệu bàn giao -> Cổng chất lượng (Quality Gate) -> Quyết định nghiệm thu (Delivery Decision)
```

4. Đánh giá và cập nhật ma trận truy xuất nguồn gốc:

```text
Requirement ID -> Design Component -> Implementation Task -> Source Code -> Test Case -> Test Result -> Final Delivery Status
```

5. Kiểm tra mức độ sẵn sàng bàn giao: Yêu cầu bài toán bãi đỗ xe, thiết kế hệ thống, kế hoạch thực hiện, báo cáo triển khai, kết quả testing, nhật ký sửa lỗi, tài liệu `README.md`, biến môi trường/secrets, CSDL SQLite/PostgreSQL, giao diện giám sát realtime và API endpoints.
6. Trường hợp không đủ điều kiện (NOT READY), xác định chính xác bước SDLC cần thực hiện backtrack.

## Review / Validation

Lệnh kiểm tra tối thiểu cho môi trường Backend & AI Service:

```powershell
# Backend & Database check
# 1. Kiểm tra cấu hình và lỗi tiềm ẩn của dự án Django
python manage.py check

# 2. Kiểm tra xem có model nào bị thay đổi mà chưa makemigrations không
python manage.py makemigrations --check --dry-run

# 3. Chạy test cho đúng các app tồn tại trong thư mục apps/
python manage.py test apps.vehicles apps.tickets apps.parking apps.core apps.users apps.reports

```

Cổng chất lượng cuối cùng (Final Quality Gate) chỉ được xác nhận thành công khi:

- Toàn bộ `docs/01` đến `docs/05` đều ghi nhận `STATUS: PASS`.
- Tất cả Requirement ID nghiệp vụ bãi đỗ xe đều có minh chứng code và test case tương ứng.
- Toàn bộ unit tests, integration tests và AI verification tests đạt kết quả PASS (hoặc hạn chế được ghi nhận chính thức và chấp nhận được).
- Không còn bất kỳ lỗi nào thuộc mức `BLOCKER` hoặc `CRITICAL`.
- Danh mục kiểm tra bảo mật (Secrets, PII biển số xe, RTSP stream) đạt tiêu chuẩn an toàn.
- Tài liệu `README.md` và `FINAL_REPORT.md` chính xác, đủ chi tiết để nhân sự vận hành/giám sát có thể tự cài đặt và khởi chạy hệ thống từ đầu.
- Không có bất kỳ thay đổi mã nguồn tính năng mới nào phát sinh trong quá trình Final Delivery.
- Toàn bộ văn bản hiển thị sử dụng tiếng Việt UTF-8 chuẩn xác.

## Traceability

Khép kín ma trận truy xuất nguồn gốc hệ thống:

```text
Requirement -> Design Component -> Implementation Task -> Source Code -> Test Case -> Test Result -> Delivery Decision
```

Trong `docs/06_final_delivery.md` bắt buộc phải bao gồm bảng:

```text
Requirement ID | Design ID | Task ID | Code Evidence | Test Result | Delivery Status
```

## Outputs

Tạo mới hoặc cập nhật các tài liệu:

- `docs/06_final_delivery.md`
- `FINAL_REPORT.md`
- `README.md` (nếu các lệnh cài đặt, cấu hình mô hình AI hoặc khởi chạy hệ thống chưa chính xác).

Ở cuối file `FINAL_REPORT.md` bắt buộc phải xuất hiện đoạn thông tin định danh:

```text
STATUS: PASS | FAIL
PROJECT_STATUS: READY | NOT_READY
DELIVERY_DECISION: READY FOR DELIVERY | NOT READY FOR DELIVERY
NEXT_PROMPT: NONE
BACKTRACK_REQUIRED: NONE | REQUIREMENTS | DESIGN | PLAN | IMPLEMENTATION | REVIEW_TESTING
```

## Acceptance Criteria

- Tài liệu `docs/06_final_delivery.md` đã được khởi tạo và ghi nhận đầy đủ đánh giá.
- Báo cáo tổng kết `FINAL_REPORT.md` được trình bày hoàn chỉnh.
- Quyết định bàn giao (`DELIVERY_DECISION`) được đưa ra rõ ràng dựa trên dữ liệu thực tế.
- Khai báo chính xác quy trình backtrack nếu dự án chưa đạt chuẩn bàn giao.
- Không bổ sung mã nguồn tính năng mới trong bước này.
- Kết thúc pipeline với `NEXT_PROMPT: NONE`.

## Handoff to Next Stage

- Nếu kết quả là `READY FOR DELIVERY`: Thực hiện nghiệm thu, bàn giao toàn bộ mã nguồn, tài liệu hướng dẫn `README.md` và `FINAL_REPORT.md`.
- Nếu kết quả là `NOT READY FOR DELIVERY`: Tạm dừng bàn giao; quay lại xử lý tại bước được chỉ định trong mục `BACKTRACK_REQUIRED`.