

from django import forms
from .models import UserInfo
from django.forms import ModelForm



class InputForm(ModelForm):
    print('inputform')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserInfo
        fields = '__all__'

class LoginForm(ModelForm):
    print('loginform')
    class Meta:
        model = UserInfo
        exclude = ('firstname', 'lastname', 'email')
        fields = ( 'username', 'password', )


