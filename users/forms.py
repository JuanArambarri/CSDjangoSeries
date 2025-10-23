from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #required = false / true (default)
    class Meta:
        model = User #with who it will interact
        fields = ['username', 'email', 'password1', 'password2']