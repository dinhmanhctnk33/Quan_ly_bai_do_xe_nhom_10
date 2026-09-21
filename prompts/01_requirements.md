# 01 Requirements

## Role

Bạn là Chuyên viên phân tích nghiệp vụ (Business Analyst) và Kỹ sư yêu cầu phần mềm (Software Requirements Engineer) trong quy trình phát triển phần mềm bằng AI.

## Objective

Xác định phần mềm cần làm gì đối với Hệ thống Quản lý Bãi đỗ xe (Phiên bản Quản lý Nghiệp vụ Cốt lõi - Không tích hợp AI)
Dựa trên định hướng nghiệp vụ từ `prompts/00_project.md`, hãy tạo/cập nhật tài liệu yêu cầu đã được rà soát, rõ ràng, có thể truy vết và đủ chất lượng để chuyển sang bước Design (`02_design.md`). Không thiết kế kiến trúc chi tiết, không thiết kế database schema vật lý và không viết source code trong bước này.

Pipeline:

```text
00_project -> 01_requirements.md -> 02_design.md -> 03_implementation_plan.md -> 04_implementation.md -> 05_review_testing.md -> 06_final_delivery.md
Language
Toàn bộ prompt, nội dung phân tích và artifact đầu ra phải viết bằng tiếng Việt có dấu, mã hóa UTF-8.

Giữ nguyên tiếng Anh hoặc ký hiệu kỹ thuật đối với tên file, thư mục, command, endpoint, HTTP method, Requirement ID, Design ID, Task ID, Test ID, status marker, mã loại xe và code block.

Không để nội dung bị lỗi mã hóa hoặc mất dấu tiếng Việt.

Inputs
Phần Project Brief trong prompt này.

Phần Project Structure trong prompt này.

Các file hiện có trong repository nếu cần đối chiếu bối cảnh.

Chỉ tiếp tục nếu có thể tạo hoặc cập nhật docs/01_requirements.md.

Skills.sh
Trước khi tạo artifact, đọc hướng dẫn skill từ skills.sh hoặc từ Agent Skills Directory tại https://www.skills.sh/ nếu môi trường cho phép. Nếu không thể truy cập trực tiếp, dùng skill agent tương ứng theo tên và ghi rõ cách áp dụng trong artifact.

Skill	Mục đích	Nhiệm vụ áp dụng	Thời điểm dùng	Đầu ra mong đợi
software-requirements	Chuẩn hóa SRS, Requirement ID, acceptance criteria và traceability	Tạo yêu cầu chức năng, phi chức năng, ràng buộc, quy tắc nghiệp vụ, giả định, câu hỏi mở cho bãi đỗ xe	Trước và trong khi viết yêu cầu	Yêu cầu có ID, source, priority, status và tiêu chí chấp nhận kiểm thử được
domain-modeling	Thiết lập thuật ngữ nghiệp vụ nhất quán	Chuẩn hóa thuật ngữ loại xe, mã loại xe, thẻ/vé xe, lượt xe vào/ra, làn xe, vị trí đỗ, bảng giá đỗ xe	Trước khi viết yêu cầu chi tiết	Glossary và ngôn ngữ miền (Domain Glossary) nhất quán
brainstorming	Phát hiện điểm mơ hồ, thiếu và mâu thuẫn	Rà soát project brief, xác định assumption và open question về quy trình kiểm soát bãi xe thủ công/bán tự động	Trong bước review trước quality gate	Danh sách ambiguity, assumption và open question
Skill phải được áp dụng thật, không chỉ liệt kê. Trong docs/01_requirements.md phải có mục Skills.sh Evidence ghi: skill đã dùng, nhiệm vụ áp dụng, đầu ra đã dùng và vị trí bằng chứng trong tài liệu.

Scope
Xác định mục tiêu phần mềm.

Xác định stakeholder và actor (Bảo vệ/Nhân viên vận hành, Quản trị viên, Khách gửi xe).

Xác định phạm vi và ngoài phạm vi.

Xác định yêu cầu chức năng cốt lõi (Ghi nhận xe vào/ra, Quản lý loại xe, Quản lý bảng giá, Quản lý vị trí đỗ, Tính phí đỗ xe).

Xác định yêu cầu phi chức năng.

Xác định ràng buộc, quy tắc nghiệp vụ (Business Rules), quy tắc validation và exception case (Xử lý mất thẻ, xe quá hạn, nhập sai mã loại xe).

Viết use case hoặc user story.

Viết acceptance criteria kiểm thử được.

Gán Requirement ID ổn định.

Phát hiện yêu cầu mơ hồ, thiếu, trùng lặp hoặc mâu thuẫn.

Khởi tạo traceability từ source sang requirement.

Out of Scope
Không tích hợp mô hình AI / ALPR (nhận diện biển số tự động qua camera) trong giai đoạn này.

Không tích hợp điều khiển phần cứng barie thực tế qua cổng Serial/IoT.

Không thiết kế kiến trúc, schema cơ sở dữ liệu vật lý, API contract chi tiết hoặc UI layout chi tiết.

Không lập kế hoạch triển khai.

Không viết hoặc sửa source code.

Không tự thêm nghiệp vụ ngoài project brief; nếu cần thì ghi thành assumption hoặc open question.

Tasks
Đọc Project Brief và Project Structure.

Áp dụng workflow skill:

Plaintext
Xác định nhiệm vụ -> Chọn skill từ skills.sh -> Đọc hướng dẫn skill -> Áp dụng skill -> Tạo artifact -> Review artifact -> Chỉnh sửa -> Validate -> Approve
Tạo bảng source trace:

SRC-001: bối cảnh nghiệp vụ bãi đỗ xe.

SRC-002: phạm vi và ngoài phạm vi.

SRC-003: actor và workflow lượt xe vào/ra.

SRC-004: quy tắc nghiệp vụ tính phí theo mã loại xe và quản lý thẻ/vé.

SRC-005: ràng buộc công nghệ và cấu trúc project.

Tạo yêu cầu theo format:

Plaintext
Requirement ID | Type | Source ID | Priority | Status | Requirement | Acceptance Criteria
Tạo use case hoặc user story cho các luồng chính (Xe vào, Xe ra, Cấu hình bảng giá, Tra cứu lịch sử).

Tạo bảng assumptions và open questions.

Review và chỉnh sửa cho đến khi yêu cầu chính xác, không trùng lặp và kiểm thử được.

Review / Validation
docs/01_requirements.md chỉ được đặt STATUS: PASS khi:

Mỗi yêu cầu quan trọng có ID ổn định.

Mỗi yêu cầu có source ID.

Mỗi MUST requirement có acceptance criteria kiểm thử được.

Scope và out of scope rõ ràng (xác nhận rõ việc chưa tích hợp AI).

Business rules và validation rules (đặc biệt là logic tính phí theo mã loại xe) không mâu thuẫn.

Open questions không bị âm thầm biến thành yêu cầu đã xác nhận.

Ràng buộc công nghệ và cấu trúc project được ghi ở mức constraint, không biến thành implementation.

Có mục Skills.sh Evidence.

Toàn bộ nội dung tiếng Việt có dấu đúng UTF-8.

Nếu quality gate không đạt, đặt STATUS: FAIL, liệt kê blocking issues và không chuyển sang Design.

Traceability
Bước này khởi tạo:

Plaintext
Source -> Requirement
Các bước sau mở rộng thành:

Plaintext
Requirement -> Design Component -> Implementation Task -> Source Code -> Test Case -> Test Result -> Final Delivery
Outputs
Tạo hoặc cập nhật:

docs/01_requirements.md

Cuối file phải có:

Plaintext
STATUS: PASS | FAIL
NEXT_INPUT: docs/01_requirements.md
NEXT_PROMPT: prompts/02_design.md
TRACEABILITY_MATRIX_UPDATED: YES | NO
Acceptance Criteria
docs/01_requirements.md tồn tại.

Không tạo hoặc sửa source code.

Requirements đủ chất lượng để chuyển sang Design.

Không còn BLOCKER hoặc CRITICAL trong review yêu cầu.

NEXT_PROMPT trỏ đúng prompts/02_design.md.

Handoff to Next Stage
Chỉ chuyển sang prompts/02_design.md khi docs/01_requirements.md có STATUS: PASS.

Project Brief
Xây dựng hệ thống quản lý bãi đỗ xe tập trung vào các chức năng nghiệp vụ cốt lõi, phục vụ công tác kiểm soát lượt xe vào/ra, tính phí đỗ xe và quản lý không gian bãi đỗ. Hệ thống chưa áp dụng công nghệ AI nhận diện biển số tự động trong giai đoạn này (sử dụng nhập liệu biển số/mã thẻ thủ công hoặc giả lập).

Vấn đề nghiệp vụ:

Quản lý lượt xe vào/ra bằng sổ sách thủ công dễ gây thất thoát, nhầm lẫn và ùn tắc.

Tính phí đỗ xe thủ công dễ dẫn đến sai sót hoặc gian lận tiền vé.

Khó kiểm soát số lượng vị trí đỗ xe còn trống theo từng loại xe trong bãi.

Thiếu công cụ tra cứu lịch sử gửi xe và báo cáo doanh thu theo thời gian.

Mục tiêu nghiệp vụ:

Quản lý tập trung các loại xe (xe máy, ô tô, xe đạp, v.v.) và mã loại xe tương ứng.

Kiểm soát quy trình xe vào: Ghi nhận thời gian vào, mã thẻ/vé, biển số (nhập tay) và phân bổ vị trí đỗ.

Kiểm soát quy trình xe ra: Ghi nhận thời gian ra, tự động tính phí đỗ xe dựa trên bảng giá và thời gian gửi.

Quản lý bảng giá linh hoạt theo mã loại xe, khung giờ (ngày/đêm) hoặc lượt đỗ.

Theo dõi trạng thái sức chứa và vị trí đỗ trong bãi đỗ xe.

Thống kê lịch sử lượt xe và báo cáo doanh thu bãi xe.

Trong phạm vi:

Quản lý loại xe (Vehicle Types): Xem, thêm, sửa, xóa, quản lý trạng thái (hoạt động/ngừng hoạt động).

Quản lý bảng giá đỗ xe (Pricing Rules): Thiết lập công thức tính phí theo mã loại xe, block thời gian hoặc vé theo lượt/ngày.

Quản lý vị trí đỗ (Parking Spots): Theo dõi danh sách chỗ đỗ, trạng thái (trống, đang đỗ, bảo trì).

Quản lý lượt gửi xe (Tickets/Parking Sessions):

Lượt xe vào: Nhập thủ công biển số xe, chọn mã loại xe, gán mã thẻ/vé, ghi nhận thời gian vào.

Lượt xe ra: Tra cứu mã thẻ/biển số, ghi nhận thời gian ra, hệ thống tự động tính tiền phí đỗ xe.

Quản lý thẻ/vé đỗ xe: Cấp phát, thu hồi, báo mất thẻ (xử lý sự cố).

Tra cứu lịch sử gửi xe, lọc theo thời gian, mã loại xe, biển số.

Dashboard thống kê tổng quan: Số xe đang trong bãi, lượt xe vào/ra trong ngày, ước tính doanh thu.

Phân trang, tìm kiếm và lọc danh sách.

Ngoài phạm vi (Giai đoạn này):

Tích hợp mô hình AI (ALPR - Nhận diện biển số tự động từ hình ảnh/camera).

Kết nối phần cứng thực tế (Cảm biến barie, cổng đọc thẻ RFID vật lý, camera RTSP realtime).

Thanh toán trực tuyến qua cổng thanh toán (MOMO, VNPay, ZaloPay).

Đăng ký và quản lý vé tháng/vé lượt dài hạn phức tạp (nếu chưa được yêu cầu).

Quản lý nhiều cơ sở bãi đỗ xe khác nhau (Multi-site).

Actors:

Nhân viên bảo vệ / Nhân viên vận hành làn xe.

Quản lý bãi đỗ xe (Admin).

Nhóm phát triển phần mềm và Tester.

Business rules:

Biển số xe và mã thẻ/vé là bắt buộc khi cho xe vào bãi.

Mã loại xe (ví dụ: MOTORBIKE, CAR_4SEAT, TRUCK) xác định công thức tính phí áp dụng.

Mỗi vé/thẻ đang hoạt động tại một thời điểm chỉ gắn với một lượt xe đang đỗ trong bãi.

Giá đỗ xe phải lớn hơn hoặc bằng 0.

Thời gian xe ra phải lớn hơn hoặc bằng thời gian xe vào.

Xe không thể làm thủ tục xe ra nếu chưa có bản ghi xe vào hợp lệ.

Khi xe ra và thanh toán thành công, vị trí đỗ tương ứng được tự động cập nhật về trạng thái "Trống" và thẻ vé trở về trạng thái "Sẵn sàng".

Technology constraints:
Thực hiện theo chuẩn PEP8

Backend là Django (Python).

Database mặc định là Microsoft SQL Server tại database/db.msSQL.

Dashboard quản lý được Django render tại /.

Dashboard dùng Bootstrap 5.

Dashboard gọi JSON API cùng origin.

frontend/ là scaffold Vue/React; trong phạm vi bài này  triển khai CRUD thật và gọi API thật.

Không commit secret thật.

Required endpoints ở mức requirement:

GET /health/

CRUD Loại xe dưới /api/vehicle-types

CRUD Vị trí đỗ dưới /api/parking-spots

CRUD Bảng giá dưới /api/pricing-rules

Nghiệp vụ Lượt xe vào/ra dưới /api/tickets (/api/tickets/check-in, /api/tickets/check-out)

Thống kê báo cáo dưới /api/reports/summary

POST /api/dev/seed

Initial open questions:

Hệ thống tính phí đỗ xe theo block giờ (ví dụ: 2 giờ đầu X đồng, mỗi giờ sau Y đồng) hay theo ca Ngày/Đêm?

Khi khách hàng làm mất thẻ xe, quy trình xử lý phạt/chứng minh chủ xe được hệ thống ghi nhận như thế nào?

Số lượng vị trí đỗ xe có giới hạn cố định theo từng loại xe hay cho phép đỗ linh hoạt?

Có cần quản lý danh sách vé tháng (khách gửi cố định) không hay chỉ xử lý vé lượt (khách vãng lai)?

Project Structure
Plaintext
parking_management/
│
├── .env.example                # File cấu hình mẫu (không commit secret thật)
├── .gitignore                  # Bỏ qua venv, node_modules, .env, log, db credentials
├── README.md                   # Hướng dẫn cài đặt, config MSSQL và vận hành dự án
├── manage.py                   # Entry point chính của Django
├── requirements.txt            # Package Python (Django, DRF, mssql-django, djangorestframework-simplejwt, v.v.)
│
├── database/                   # Thư mục chứa cấu hình và script Database
│   └── db.msSQL                # Script DDL khởi tạo/cấu hình Microsoft SQL Server
│
├── frontend/                   # Scaffold Frontend SPA (Vue.js / React.js)
│   ├── public/
│   ├── src/
│   │   ├── api/                # Các hàm gọi REST API (/api/auth, /api/users, /api/tickets, v.v.)
│   │   ├── components/         # Component dùng chung (Navbar, Sidebar, Modal, Table)
│   │   ├── router/             # Router xử lý Auth Guard (chỉ user đã login mới vào được)
│   │   ├── views/              # Trang Quản lý Nhân viên, Loại xe, Bãi đỗ, Vé, Báo cáo, Login
│   │   ├── App.vue / App.jsx
│   │   └── main.js / main.jsx
│   ├── package.json
│   └── vite.config.js / vue.config.js
│
├── config/                     # Configuration của Django Project (Core Settings)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Cấu hình MSSQL, DRF, JWT Auth, Static/Media files, CORS
│   ├── urls.py                 # Router tổng hợp (phân luồng Django UI `/` và `/api/*`)
│   └── wsgi.py
│
├── static/                     # Static files phục vụ Dashboard Django (Bootstrap 5)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/                  # Django Templates (Server-side rendering)
│   ├── base.html               # Base layout tích hợp Bootstrap 5 (CDN/Static)
│   ├── authentication/
│   │   └── login.html          # Trang đăng nhập cho Dashboard Django tại `/login`
│   └── dashboard/
│       └── index.html          # Dashboard quản lý chính render tại route `/`
│
└── apps/                       # Các Django Apps phân tách theo miền nghiệp vụ (PEP8)
    ├── __init__.py
    │
    ├── authentication/         # Xử lý Đăng nhập, Xác thực Token & Session
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── serializers.py      # Serializer cho Login, Refresh Token
    │   ├── urls.py             # Route: /api/auth/login, /api/auth/logout, /api/auth/me
    │   └── views.py            # API Views xử lý authentication
    │
    ├── users/                  # Quản lý Nhân viên & Phân quyền
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py           # Custom User Model (Mã NV, Họ tên, Chức vụ, Ca làm việc)
    │   ├── permissions.py          # Custom Permission (IsAdminUser, IsStaffGuard)
    │   ├── serializers.py      # CRUD Serializers cho Nhân viên
    │   ├── urls.py             # CRUD API /api/users (Danh sách, Tạo mới, Sửa, Vô hiệu hóa)
    │   └── views.py
    │
    ├── core/                   # Hệ thống chung, Health check & Seed data
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── urls.py             # Endpoints: GET /health/, POST /api/dev/seed
    │   └── views.py
    │
    ├── vehicles/               # Quản lý Loại xe (Vehicle Types)
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py           # Model VehicleType (Mã loại xe, Tên loại xe, Mô tả)
    │   ├── serializers.py
    │   ├── urls.py             # CRUD /api/vehicle-types
    │   └── views.py
    │
    ├── parking/                # Quản lý Vị trí đỗ & Bảng giá
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py           # Models: ParkingSpot (Khu vực, Vị trí), PricingRule (Bảng giá)
    │   ├── serializers.py
    │   ├── urls.py             # CRUD /api/parking-spots, CRUD /api/pricing-rules
    │   └── views.py
    │
    ├── tickets/                # Nghiệp vụ Lượt xe vào/ra (Check-in & Check-out)
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py           # Model Ticket (Biển số, Thời gian vào/ra, Tổng tiền, Trạng thái)
    │   ├── serializers.py
    │   ├── services.py         # Business logic: Tính tiền gửi xe, kiểm tra chỗ trống, check-in, check-out
    │   ├── urls.py             # CRUD /api/tickets, POST /api/tickets/check-in, POST /api/tickets/check-out
    │   └── views.py
    │
    └── reports/                # Thống kê & Báo cáo
        ├── __init__.py
        ├── apps.py
        ├── services.py         # Logic SQL/ORM tổng hợp doanh thu, lượt xe, công suất bãi đỗ
        ├── urls.py             # Endpoint: GET /api/reports/summary
        └── views.py