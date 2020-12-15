  
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    userid = forms.CharField()
    pwd = forms.CharField(widget=forms.PasswordInput)
    #Sign_in_token = forms.CharField(max_length=50)


