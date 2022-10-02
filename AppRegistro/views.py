from django.shortcuts import render, redirect

from AppRegistro.forms import UserRegisterForm,  UserUpdateForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LogoutView


from django.contrib import messages
from django.urls import reverse_lazy

# Registro Usuario

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            human = True
            form.save()
            return render(request, "AppTienda/home.html", {"mensaje":"Usuario Creado"})
        else:
            return render(request, "AppTienda/home.html", {"mensaje":"Error con el registro"})
    
    formulario = UserRegisterForm()  
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "AppRegistro/registro.html", context=context)

# Login 
def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "AppTienda/home.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppTienda/home.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"AppTienda/home.html", {"mensaje":"Error, formulario erroneo"})
            

    form = AuthenticationForm()
    return render(request,"AppRegistro/login.html", {'form':form} )


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'AppRegistro/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

class CustomLogoutView(LogoutView):
    template_name = 'AppRegistro/logout.html'
    next_page = reverse_lazy('inicio')

