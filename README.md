# Hệ thống Quản lý Bãi đỗ xe

Phiên bản này cung cấp nghiệp vụ cốt lõi bằng Django: quản lý loại xe, vị trí, bảng giá, lượt xe vào/ra, thanh toán tại bãi và báo cáo summary. Biển số và mã thẻ/vé được nhập thủ công.

## Phạm vi

AI/ALPR, camera, WebSocket, barie, RFID, IoT, thanh toán trực tuyến và vé tháng chưa được triển khai theo tài liệu yêu cầu. Không đặt secret thật trong repository.

## Cài đặt

Yêu cầu Python 3.12 trở lên.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Điền `DJANGO_SECRET_KEY` và `GEMINI_API_KEY` (cho module AI Assistant) trong file `.env`. 
Local mặc định dùng SQLite để chạy demo/test. Môi trường MSSQL dùng các biến `DB_ENGINE`, `DB_NAME`, `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`.

## Chạy hệ thống

1. **Khởi tạo cơ sở dữ liệu và dữ liệu mẫu (Seed Data)**:
   ```powershell
   python manage.py migrate
   python manage.py seed_demo
   ```
   *(Lệnh `seed_demo` nạp sẵn dữ liệu khởi tạo cho 10 bảng CSDL: người dùng mẫu `admin`/`mai`/`hung`, 4 khu vực đỗ xe, loại xe, bảng giá, các lượt xe đang gửi/đã ra và vé tháng).*

2. **Khởi chạy Server**:
   ```powershell
   python manage.py runserver
   ```

3. **Truy cập hệ thống**:
   - Trang chủ / Dashboard: `http://127.0.0.1:8000/`
   - Endpoint kiểm tra health: `GET http://127.0.0.1:8000/health/`
   - AI Assistant Chatbot: `POST http://127.0.0.1:8000/api/ai/chat/` hoặc biểu tượng Chatbot AI trên giao diện.

## API chính

- **Xác thực**: `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/auth/me`
- **Danh mục & Bãi đỗ**: CRUD `/api/vehicle-types/`, CRUD `/api/parking-spots/`, CRUD `/api/pricing-rules/`
- **Vé & Lượt xe**: `GET /api/tickets/`, `POST /api/tickets/check-in`, `POST /api/tickets/check-out`, CRUD `/api/tickets/monthly/`
- **AI Assistant**: `GET /api/ai/chat/` (status), `POST /api/ai/chat/` (hỏi-đáp AI)
- **Báo cáo**: `GET /api/reports/summary`

## Kiểm thử

```powershell
# Kiểm tra cấu hình và migration Django
python manage.py check
python manage.py makemigrations --check --dry-run

# Chạy toàn bộ Unit Tests của hệ thống (Django tests)
python manage.py test

# Chạy riêng bộ unit test cho AI Assistant
python manage.py test apps.ai_assistant.tests_ai

# Chạy script kiểm thử tự động API Chatbot AI (cần server đang chạy)
python test_ai_assistant.py --mode all
```

Tài liệu ca kiểm thử chi tiết và kịch bản test thủ công được lưu tại `AI_TestCase_v2.docx`.

## Tài liệu

- `docs/01_requirements.md`: yêu cầu
- `docs/02_design.md`: thiết kế
- `docs/03_implementation_plan.md`: kế hoạch
- `docs/04_implementation.md`: triển khai
- `docs/05_review_testing.md`: review và testing
- `docs/06_final_delivery.md`: bàn giao cuối
- `FINAL_REPORT.md`: quyết định phát hành
