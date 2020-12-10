from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                        'index.htm', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
            'signup.htm',
            {'user_form': user_form})