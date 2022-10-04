from django.urls import path
from AppRegistro import views 

urlpatterns = [
    
    path('register/', views.register, name = 'register'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
    path('profile/', views.ProfileUpdateView.as_view(), name="profile"),
    path('add_avatar/', views.agregar_avatar, name = 'avatar'),
    path('add_order/', views.crear_pedido, name='crear_pedido'),
    path('order/', views.pedidos, name='pedidos'),
    path('delete-order/<int:id>/', views.eliminar_pedido, name="eliminar_pedido"),

]