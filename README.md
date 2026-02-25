# MEI - IT Request Management System

A Django-based web application for managing IT support requests. Employees can submit, track, and manage their IT service requests while administrators can review, approve, and update request statuses.

## 📋 Overview

MEI (IT Request Management System) streamlines the process of submitting and tracking IT support requests within an organization. 

**Key Features:**
- **Employee Dashboard** - Submit and track IT requests in real-time
- **Admin Dashboard** - Review, approve, and manage all requests
- **Request Tracking** - Monitor request status through multiple stages (Waiting → Pending → Completed → Closed)
- **Request History** - View closed and cancelled requests
- **File Attachments** - Support for PNG, JPG, and PDF file uploads
- **Responsive Design** - Modern Tailwind CSS UI that works on desktop and mobile

## 📦 Prerequisites

Before running the project, ensure you have:
- Python 3.13+ installed
- pip (Python package manager)
- Git
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/aarown00/MEI.git
cd <folder-name> or open root folder
```

### 2. Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv env

# Activate it
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. PostgreSQL (Local) Configuration Example
For local development using PostgreSQL, update the `DATABASES` setting in  
`itreq/settings.py` as shown below:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'meidb',
        'USER': 'aaronmart',
        'PASSWORD': 'pass123',
        'HOST': 'localhost',
        'PORT': '5432',

     }
 }

### 5. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

## 🏃 Running the Server

### Development Server
```bash
python manage.py runserver
```
Access the application at: `http://localhost:8000`

## 👥 User Roles

### Employee
- Submit new IT requests
- View their active requests
- Track request progress (Waiting → Pending → Completed)
- Cancel requests (only when status is "Waiting")
- Close completed requests
- View request history

### Administrator
- View all employee requests
- Approve pending requests
- Mark completed requests as done
- Close and cancel requests
- Access admin dashboard for full system overview

<!-- ## 🔑 Main URLs

| URL | Purpose |
|-----|---------|
| `/` | Login page |
| `/register/` | User registration |
| `/profile/` | User profile and FAQs |
| `/submit-request/` | Submit new IT request |
| `/view-requests/` | Employee/Admin dashboard |
| `/history/` | Request history |
| `/admin/` | Django admin panel |

## 📧 Email Configuration

To enable email notifications:

1. Use Gmail with an App Password:
   - Enable 2-Factor Authentication on Gmail
   - Generate an App Password at https://myaccount.google.com/apppasswords
   - Use the generated password in `EMAIL_HOST_PASSWORD`

2. Update `settings.py` with your email configuration -->

<!-- ## 🐛 Troubleshooting

**Port already in use:**
```bash
# Change port
python manage.py runserver 8001
```

**Database errors after changes:**
```bash
# Create new migration
python manage.py makemigrations webapp

# Apply migration
python manage.py migrate
```

**Static files not loading:**
```bash
python manage.py collectstatic --clear --noinput -->
```

## 📝 Notes

<!-- - The project uses Tailwind CSS for styling - Bootstrap CSS/JS can be safely removed after form refactoring -->
- All passwords are hashed using Django's default algorithm
- File uploads are stored in the `media/user_uploads/` directory
<!-- - The system sends automated emails for new requests and status updates -->

## 🔐 Security Considerations

- Use `DEBUG=False` in production
- Keep `DJANGO_SECRET_KEY` secure and use environment variables
- Use HTTPS in production
- Regularly update dependencies: `pip list --outdated`
- Enable CSRF protection (enabled by default)

<!-- ## 📄 License

This project is for internal use within the organization.

---

**For support or issues, please contact the development team.** -->
