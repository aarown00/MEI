# MEI - IT Request Management System

A Django-based web application for managing IT support requests. Employees can submit, track, and manage their IT service requests while administrators can review, approve, and update request statuses.

---

## 📋 Overview

MEI (IT Request Management System) streamlines the process of submitting and tracking IT support requests within an organization.

### ✨ Key Features

- **Employee Dashboard** – Submit and track IT requests in real-time  
- **Admin Dashboard** – Review, approve, and manage all requests  
- **Request Tracking** – Monitor request status through multiple stages  
  (Waiting → Pending → Completed → Closed)  
- **Request History** – View closed and cancelled requests  
- **File Attachments** – Support for PNG, JPG, and PDF uploads  
- **Responsive Design** – Modern Tailwind CSS UI (desktop & mobile friendly)

---

## 📦 Prerequisites

Before running the project, ensure you have:

- Python 3.13+
- pip (Python package manager)
- Git
- Virtual environment (recommended)
- PostgreSQL (for local development)

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aarown00/MEI.git
cd MEI
```

### 2️⃣ Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate it

# On Windows:
env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ PostgreSQL Configuration (Local Example)

Update the `DATABASES` setting in:

`itreq/settings.py`

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "meidb",
        "USER": "aaronmart",
        "PASSWORD": "pass123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 5️⃣ Database Setup

```bash
# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

---

## 🏃 Running the Server

### Development Server

```bash
python manage.py runserver
```

Access the application at:

```
http://localhost:8000
```

---

## 👥 User Roles

### 🧑‍💻 Employee

- Submit new IT requests  
- View active requests  
- Track request progress (Waiting → Pending → Completed)  
- Cancel requests (only when status is **Waiting**)  
- Close completed requests  
- View request history  

### 🛠 Administrator

- View all employee requests  
- Approve pending requests  
- Mark completed requests as done  
- Close and cancel requests  
- Access admin dashboard for full system overview  

---

## 📝 Notes

- Passwords are hashed using Django’s default authentication system  
- File uploads are stored in: `media/user_uploads/`

---

## 🔐 Security Considerations

- Set `DEBUG = False` in production  
- Store `DJANGO_SECRET_KEY` in environment variables  
- Use HTTPS in production  
- Keep dependencies updated:

```bash
pip list --outdated
```

- CSRF protection is enabled by default  

---

## 📄 License

This project is for educational and internal organizational use.

---

**Developed using Django and PostgreSQL.**