from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print(request.POST)
        if user_form.is_valid():
            user_form.save()
            #return user ubject
            cd=user_form.cleaned_data
            user = authenticate(username = cd['email'], password = user_form.cleaned_data['password1'])
            print(cd['email'], user_form.cleaned_data['password1'])
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home/')
            else:
                return  HttpResponse('login failed')
        else:
            print(user_form.errors)
            return  HttpResponse('register failed')
    else:
        user_form = UserRegistrationForm()
    return render(request,
            'signup.htm',
            {'user_form': user_form})