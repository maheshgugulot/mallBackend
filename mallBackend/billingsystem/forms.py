from django import forms
from .models import Employee

class SignupForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'border: 1px solid #ccc; display: block; padding: 5px; margin: 5px; font-size: 14px;'}),
            'username': forms.TextInput(attrs={'style': 'border: 1px solid #ccc; display: block; padding: 5px; margin: 5px; font-size: 14px;'}),
            'email': forms.EmailInput(attrs={'style': 'border: 1px solid #ccc; display: block; padding: 5px; margin: 5px; font-size: 14px;', 'placeholder': 'Email address'}),
            'password': forms.PasswordInput(attrs={'style': 'border: 1px solid #ccc; display: block; padding: 5px; margin: 5px; font-size: 14px;'}),
        }

