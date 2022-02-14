from django import forms

class SignInInputs(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput())


class SignUpInputs(forms.Form):
    first_name=forms.CharField(max_length=20)
    second_name=forms.CharField(max_length=20)
    email=forms.EmailField(widget=forms.EmailInput())
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())