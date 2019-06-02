# user management forms
from django import forms
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#
# class AddUserForm(forms.Form):
#     username = forms.CharField(label='User name')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#     first_name = forms.CharField(label='First name', required=False)
#     last_name = forms.CharField(label='Last name', required=False)
#     email = forms.CharField(label='E-mail', validators=[validate_email])
