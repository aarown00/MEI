# MEI System

A full-stack Django web application for IT Request Tracking System designed to manage and monitor user inquiries, technical issues, and service requests efficiently.

## Features

User Authentication – Secure registration and login for both employees and admins.

IT Request Management – Submit IT requests and view their status and history.

File Uploads – Attach images for additional references.

Centralized Dashboard – Admin and employee dashboards for approving, monitoring, and managing request statuses.

## Prerequisites

Before you begin, ensure you have the following installed:

-Python 3.10 or higher (Required for Django 5.x compatibility)

-pip (Python package installer)

-virtualenv (recommended for isolated environments)

-Git

-PostgreSQL 12 or higher

-pgAdmin (optional, for database management)

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/aarown00/MEI.git
cd <folder-name> or open root folder
```

### 2. Create a virtual environment
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. PostgreSQL (Local) Configuration Example
```bash
For local development using PostgreSQL, update the `DATABASES` setting in  
`itreq/settings.py` as shown below:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "meidb",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
### 5. Run database migrations
```bash
python manage.py migrate
```

### 6. Create a superuser 
```bash
python manage.py createsuperuser
```

### 8. Run the development server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Usage

- Access the admin panel at `http://localhost:8000/admin`

