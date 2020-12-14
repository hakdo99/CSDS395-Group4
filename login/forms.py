  
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    userid = forms.CharField()
    pwd = forms.CharField(widget=forms.PasswordInput)
    #Sign_in_token = forms.CharField(max_length=50)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']