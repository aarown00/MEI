from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import IT_Request
from django.forms import ClearableFileInput

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
        if len(username) > 10:
            raise forms.ValidationError("ID number should contain up to 10 digits.")
        return username
    
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
