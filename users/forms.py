from django import forms
from . import models


class LoginForm(forms.Form):

    id = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username',
        'id':'id'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Password',
        'id':'password'
        }
    ))