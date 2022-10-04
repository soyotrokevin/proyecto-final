from django.shortcuts import render, redirect

from AppRegistro.forms import UserRegisterForm,  UserUpdateForm, AvatarForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from AppRegistro.models import Pedidos
from AppRegistro.forms import PedidoForm

from django.views.generic import  UpdateView

from django.urls import reverse_lazy, reverse



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

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            cliente = Pedidos(**data)
            cliente.save()
            return redirect(reverse('pedidos'))
    else:  # GET
        form = PedidoForm()  # Formulario vacio para construir el html
    return render(request, "AppRegistro/order_form.html", {"form": form})

@login_required
def pedidos(request):
    pedidos = Pedidos.objects.all() 
    contexto = {"pedidos": pedidos}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppRegistro/order.html", contexto)

@login_required
def eliminar_pedido(request, id):
    pedido = Pedidos.objects.get(id=id)
    borrado_id = pedido.id
    pedido.delete()
    url_final = f"{reverse('pedidos')}?borrado={borrado_id}"

    return redirect(url_final)

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid:   
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return render(request, "AppTienda/home.html", {"mensaje": "avatar cargado :)"})

    form = AvatarForm()
    return render(request,"AppRegistro/avatar.html", {'form':form} )


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

