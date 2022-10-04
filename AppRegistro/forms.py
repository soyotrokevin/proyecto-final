from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppRegistro.models import Avatar, Pedidos
from captcha.fields import CaptchaField


# Lista con los años seleccionables en el registro
mayor_edad = range(1920, 2010, 1) 

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    birth_date = forms.DateField(label='Fecha de nacimiento', widget=forms.SelectDateWidget(years=mayor_edad))
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date' ,'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email'] 

class PedidoForm(forms.Form):
    marca = forms.CharField(max_length=128)
    modelo = forms.CharField(max_length=128)
    email = forms.EmailField()

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields =['imagen'] 