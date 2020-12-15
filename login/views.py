from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from register.models import User


# Create your views here.


def logout(request):
    return render(request, 'logout.html', {'section': 'logout'})


def forgotPassword(request):
    if request.method == 'POST':
        check_email = request.POST.get('Reset password')
        email_match = User.objects.filter(email=check_email)
        return email_match.password

    return render(request, 'forgetpassword.html', {'section': 'forgetpassword'})

def resetPassword(request):
    return render(request, 'resetpassword.html', {'section': 'logout'})


def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)
        print(LoginForm)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['userid'],
                                password=cd['pwd'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login/loggedin/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            print(form.errors)
            return HttpResponse('Invalid Form')
    else:
        form = LoginForm()
    return render(request, 'index.htm', {'form': form})