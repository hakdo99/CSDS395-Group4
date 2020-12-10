from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.

def login(request):
    return render(request, 'index.htm', {'section': 'login'})

def logout(request):
    return render(request, 'logout.html', {'section': 'logout'})

def forgotPassword(request):
    return HttpResponse("password recovery page")

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'index.htm', {'form': form})