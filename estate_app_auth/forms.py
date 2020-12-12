from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Потребителско име', min_length=4, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Въведи парола')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Потвърди паролата')

    def clean_username(self):
        username = self.cleaned_data['username']
        result = User.objects.filter(username=username)
        if result.count():
            raise ValidationError("Потребителското име вече е заето. Моля изберете друго потребителско име")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Паролите не съвпадат. Моля въведете ги отново.")

        return password2

    def save(self):
        user = User.objects.create_user(
            username= self.cleaned_data['username'],
            password= self.cleaned_data['password1']
        )
        return user

