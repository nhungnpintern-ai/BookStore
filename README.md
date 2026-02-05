Database Layer
FastAPI ↔ Session ↔ SQLAlchemy ↔ PostgreSQL

Tạo môi trường ảo :

python -m venv venv
.\venv\Scripts\activate

Chạy lệnh sau từ thư mục gốc
uvicorn app.main:app --reload

Cấu trúc thư mục
Simple/core
Simple/crud
Simple/models
Simple/router
Simple/schema

Mở trình duyệt và truy cập: http://127.0.0.1:8000/docs để xem Swagger UI.

Cấu hình Database
DATABASE_URL=postgresql://user:password@localhost/dbname

Tạo Class Model
class Book(Base):
**tablename** = "book"
id = Column(Integer, primary_key=True, index=True)
title = Column(String, nullable=False)
author = Column(String, nullable=False)
price = Column(Float, nullable=False)
published_date = Column(Date, nullable=True)

PostgreSQL cho phép tạo bảng
Base.metadata.create_all(bind=engine)

tao class Model
class User(Base):
**tablename** = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
    is_active = Column(Boolean, default=True)

Endpoint
POST /auth/register
Đăng nhập
POST /auth/login
Hash password + JWT
pip install passlib[bcrypt] python-jose[cryptography]
Cách sử dụng Access Token
Authorization: Bearer <access_token>
Quy tắc truy cập API
| Method | Endpoint |
| ------ | ----------- |
| GET | /books |
| GET | /books/{id} |
Phân quyền権限
user (mặc định)
admin
| API | Quyền |
| ------------------ | ----------- |
| DELETE /books/{id} | Chỉ `admin` |
Gán quyền sở hữu sách (Owner)
owner.id = user.id
current_user.id == book.owner_id

Demo trên Swagger UI
Bước 1: Login

Gọi POST /auth/login

Nhấn Authorize (🔒)

Nhập:

username = email

password = mật khẩu

Bước 2: Gọi API

Gọi POST /books → Thành công

User thường gọi DELETE /books/{id} → 403

Admin gọi DELETE /books/{id} → 204
