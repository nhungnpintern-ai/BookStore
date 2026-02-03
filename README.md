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
