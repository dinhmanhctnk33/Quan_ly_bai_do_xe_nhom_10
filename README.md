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

Điền `DJANGO_SECRET_KEY` và cấu hình database trong `.env`. Local mặc định dùng SQLite để chạy demo/test. Môi trường MSSQL dùng các biến `DB_ENGINE`, `DB_NAME`, `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`.

## Chạy

```powershell
python manage.py migrate
python manage.py runserver
```

Mở `http://127.0.0.1:8000/`. Kiểm tra health tại `GET /health/`.

## API chính

- `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/auth/me`
- CRUD `/api/vehicle-types/`
- CRUD `/api/parking-spots/`
- CRUD `/api/pricing-rules/`
- `GET /api/tickets/`
- `POST /api/tickets/check-in`
- `POST /api/tickets/check-out`
- `GET /api/reports/summary`
- `POST /api/dev/seed` bị khóa ngoài môi trường phát triển

Các API nghiệp vụ yêu cầu đăng nhập. GET danh mục dành cho người dùng đã xác thực; mutation CRUD yêu cầu admin.

## Kiểm thử

```powershell
python manage.py check
python manage.py check --deploy
python manage.py makemigrations --check --dry-run
python manage.py test
```

Kết quả nghiệm thu hiện tại: 17 tests PASS. MSSQL integration smoke cần chạy riêng trong môi trường có credentials thật; không ghi credentials vào `.env.example` hoặc repository.

## Tài liệu

- `docs/01_requirements.md`: yêu cầu
- `docs/02_design.md`: thiết kế
- `docs/03_implementation_plan.md`: kế hoạch
- `docs/04_implementation.md`: triển khai
- `docs/05_review_testing.md`: review và testing
- `docs/06_final_delivery.md`: bàn giao cuối
- `FINAL_REPORT.md`: quyết định phát hành
