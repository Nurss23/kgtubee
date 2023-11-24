from django import forms
from .models import *
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['channel_name', 'photo']

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username", "password", 
            "first_name", "last_name"
            ]
        
# class UserCreateForm(forms.Form):
#     username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':'form-input'}))
#     password  = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class':'form-input'}))
#     first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class':'form-input'}))
#     last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class':'form-input'}))


class UserAuthForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ["username", "password"]