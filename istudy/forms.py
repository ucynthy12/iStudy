from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from cloudinary.forms import CloudinaryFileField


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=300,help_text='Required. Inform a valid email address')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('role', 'phone_number', 'full_name')