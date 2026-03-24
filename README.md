# Employee Management System (EMS)

## 🚀 Features
- JWT Authentication (Admin, Manager, Employee roles)
- Employee CRUD with role-based permissions
- Department management with relationships
- Pagination & search support
- API documentation (Swagger)

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (can upgrade to PostgreSQL)
- JWT Authentication

## 🔐 Roles & Permissions
- Admin: Full access
- Manager: Create & update employees and departments
- Employee: Read-only access

## 📄 API Documentation
Swagger UI available at:
http://127.0.0.1:8000/swagger/

## ⚙️ Setup Instructions
```bash
git clone <your-repo-link>
cd employee-management-system
pip install -r requirements.txt
python manage.py runserver