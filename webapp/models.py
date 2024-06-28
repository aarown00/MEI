from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class IT_Request(models.Model):
    # Helper function to generate choices
    def generate_choices(*args):
        return [(arg, arg.capitalize()) for arg in args]

    # Constants for choices
    EQ_TYPE_CHOICES = generate_choices('Desktop', 'Laptop', 'Printer', 'Network Devices', 'Peripherals')
    ISSUE_CHOICES = generate_choices('Account Creation/Deletion', 'Password Reset/Unlock', 'Server Access', 'Application Installation', 'Troubleshoot', 
                                     'Security Incident Report', 'Data Backup/Recovery', 'Hardware Installation', 'Network' )
    STATUS_CHOICES = generate_choices('Waiting', 'Pending', 'Completed', 'Cancelled_By_Employee', 'Cancelled_By_Admin', 'Closed_By_Employee', 'Closed_By_Admin')
    DEP_CHOICES = generate_choices('Human Resources (HR)', 'Finance/Accounting', 'Information Technology (IT)', 'Marketing/Sales', 'Operations', 'Engineering')

    # Model fields
    eq_name = models.CharField(max_length=100)
    eq_type = models.CharField(max_length=100, choices=EQ_TYPE_CHOICES)
    department = models.CharField(max_length=100, choices=DEP_CHOICES)
    requested_at = models.DateTimeField(auto_now_add=True)
    issue = models.CharField(max_length=100, choices=ISSUE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Waiting')
    upload = models.FileField(null=True, blank=True, upload_to="user_uploads/", validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])
    #Foreign Model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #ID field
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Request: {self.id}, {self.status}, {self.issue}, User:{self.user.first_name} {self.user.last_name}"
    
    def formatted_requested_at(self):
        return self.requested_at.astimezone(timezone.get_current_timezone()).strftime("%m/%d/%Y, %I:%M %p")
