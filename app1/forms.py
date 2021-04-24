from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from .admin import UserCreationForm
class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=200)

    class Meta:
        model = MyUser
        fields = ('email','Phone', 'Address')

class ProfileUpdateForm(forms.ModelForm):
    
    email = forms.EmailField(max_length=200)

    class Meta:
        model = MyUser
        fields = ('email','Phone', 'Address')

