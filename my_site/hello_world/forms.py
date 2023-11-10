from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 200)
    password = forms.CharField(widget= forms.PasswordInput)