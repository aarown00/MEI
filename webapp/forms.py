from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import IT_Request
from django.forms import ClearableFileInput
from django.conf import settings
import requests

# Define your API key for Abstract API
API_KEY = settings.ABSTRACT_API_KEY

#Registration
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Employee ID'
        })
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Password'
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirm Password'
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isdigit():
            raise forms.ValidationError("ID number should contain only digits.")
        if len(username) != 4:
            raise forms.ValidationError("ID number should contain exactly 4 digits.")
        return username
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("First name should contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("Last name should contain only letters.")
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError("Sorry, this system only accepts Gmail addresses.")
        
        # Check if email already exists in the database
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address already exists.")
        
        # Validate email using Abstract API
        url = f"https://emailvalidation.abstractapi.com/v1/?api_key={API_KEY}&email={email}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            deliverability = data.get("deliverability")
            if deliverability == "UNDELIVERABLE":
                raise forms.ValidationError("The email address is not active.")
        else:
            raise forms.ValidationError("Failed to validate email address.")

        return email
    
#IT Request Form
class IT_RequestForm(forms.ModelForm):

    class Meta:
        model = IT_Request
        fields = ['department', 'eq_name', 'eq_type', 'issue', 'description', 'upload']

    def __init__(self, *args, **kwargs):
        super(IT_RequestForm, self).__init__(*args, **kwargs)
        
        self.fields['department'].required = True
        self.fields['department'].widget.attrs.update({
            'placeholder': 'Department',
            'class': 'form-control'
        })
        
        self.fields['eq_name'].required = True
        self.fields['eq_name'].widget.attrs.update({
            'placeholder': 'Equipment Name',
            'class': 'form-control'
        })
        
        self.fields['eq_type'].required = True
        self.fields['eq_type'].widget.attrs.update({
            'placeholder': 'Equipment Type',
            'class': 'form-control'
        })
        
        self.fields['issue'].required = True
        self.fields['issue'].widget.attrs.update({
            'placeholder': 'Issue',
            'class': 'form-control'
        })
        
        self.fields['description'].required = True
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Description',
            'class': 'form-control'
        })

        self.fields['upload'].widget = ClearableFileInput(attrs={
            'class': 'form-control',  
        })