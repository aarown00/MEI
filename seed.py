import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itreq.settings')  # <-- change this
django.setup()

from django.contrib.auth.models import User
from webapp.models import IT_Request  # <-- change this to your app name

# ──────────────────────────────────────────────
# Config
# ──────────────────────────────────────────────
NUM_REQUESTS = 20

EQ_TYPES     = ['Desktop', 'Laptop', 'Printer', 'Network Devices', 'Peripherals']
ISSUES       = ['Account Creation/Deletion', 'Password Reset/Unlock', 'Server Access',
                'Application Installation', 'Troubleshoot', 'Security Incident Report',
                'Data Backup/Recovery', 'Hardware Installation', 'Network']
STATUSES     = ['Waiting', 'Pending', 'Completed', 'Cancelled_By_Employee',
                'Cancelled_By_Admin', 'Closed_By_Employee', 'Closed_By_Admin']
DEPARTMENTS  = ['Human Resources (HR)', 'Finance/Accounting', 'Information Technology (IT)',
                'Marketing/Sales', 'Operations', 'Engineering']

SAMPLE_DESCRIPTIONS = [
    "The device is running slow and needs to be checked immediately.",
    "User is unable to log in after multiple failed attempts.",
    "Requesting installation of software required for daily operations.",
    "Network connection keeps dropping throughout the day.",
    "New employee needs account set up with proper permissions.",
    "Printer is offline and not responding to any print jobs.",
    "Suspicious email received, possible phishing attempt.",
    "Critical files were accidentally deleted, need recovery ASAP.",
    "Hardware component making unusual noise, requires inspection.",
    "Remote access to server is not working after recent update.",
]

SAMPLE_EQ_NAMES = [
    "DESKTOP-001", "LAPTOP-HR-03", "PRINTER-FLR2", "SWITCH-MAIN",
    "MONITOR-42", "KEYBOARD-09", "SERVER-01", "ROUTER-GW", "NAS-STORAGE", "WS-MKT-07"
]

FIRST_NAMES = ["Alice", "Bob", "Carlos", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ivan", "Julia"]
LAST_NAMES  = ["Santos", "Reyes", "Cruz", "Garcia", "Lopez", "Mendoza", "Torres", "Flores", "Rivera", "Gomez"]

# ──────────────────────────────────────────────
# Create dummy users if needed
# ──────────────────────────────────────────────
def get_or_create_users(n=5):
    users = list(User.objects.filter(is_superuser=False))
    
    needed = n - len(users)
    for i in range(needed):
        first = random.choice(FIRST_NAMES)
        last  = random.choice(LAST_NAMES)
        username = f"{first.lower()}.{last.lower()}{random.randint(10,99)}"
        user = User.objects.create_user(
            username=username,
            password="password123",
            first_name=first,
            last_name=last,
            email=f"{username}@company.com"
        )
        users.append(user)
        print(f"  Created user: {username}")
    
    return users

# ──────────────────────────────────────────────
# Seed
# ──────────────────────────────────────────────
def seed():
    print("Seeding database...")
    
    users = get_or_create_users(n=5)
    created_count = 0

    for i in range(NUM_REQUESTS):
        request = IT_Request.objects.create(
            eq_name    = random.choice(SAMPLE_EQ_NAMES),
            eq_type    = random.choice(EQ_TYPES),
            department = random.choice(DEPARTMENTS),
            issue      = random.choice(ISSUES),
            description= random.choice(SAMPLE_DESCRIPTIONS),
            status     = random.choice(STATUSES),
            upload     = None,
            user       = random.choice(users),
        )

        # Backdate requested_at randomly within the last 60 days
        random_days = random.randint(0, 60)
        random_hours = random.randint(0, 23)
        request.requested_at = timezone.now() - timedelta(days=random_days, hours=random_hours)
        request.save(update_fields=['requested_at'])

        created_count += 1
        print(f"  [{i+1:02d}] {request}")

    print(f"\nDone! {created_count} IT_Request records created.")

if __name__ == "__main__":
    seed()