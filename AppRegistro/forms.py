from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

# Lista con los años seleccionables en el registro
mayor_edad = ['1980', '1981', '1982']

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    birth_date = forms.DateField(label='Fecha de nacimiento', widget=forms.SelectDateWidget(years=mayor_edad))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date' ,'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(label='Fecha de nacimiento', widget=forms.SelectDateWidget(years=mayor_edad))
    class Meta:
        model = User
        fields = ['first_name','last_name', 'birth_date' ,'email']

class MyForm(forms.Form):
    captcha=CaptchaField()