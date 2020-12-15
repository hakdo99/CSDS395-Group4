  
from django import forms
from django.contrib.auth.forms import UserCreationForm
from restaurantPage.models import Restaurant
from django.contrib.auth import get_user_model




class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'accountRestaurant')

"""def clean_password2(self):
        cd = self.cleaned_data
        if cd['pwd'] != cd['confirmPwd']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['confirmPwd']

    def makeAccount(self, name, id, password):
        User=User.create(name,id,password)
        if User is not None:
            User.save()
        else:
            print('user creation unsuccessful')
        userRes = Restaurant.create(name, User)
        if userRes is not None:
            userRes.save()
            return User
        else:
            Print('restaurant creation unsuccessful')"""

class passwordChangeForm(forms.Form):
    email = forms.CharField(max_length=100)
    #found_accounts=User