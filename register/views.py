from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            #return user ubject
            user = authenticate(username=username, password = user_form.cleaned_data['password'])

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
            return render(request,
                        'index.htm', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
            'signup.htm',
            {'user_form': user_form})