from django.urls import path    
from AppTienda import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('acerca-de/', views.acerca_de, name = "acerca_de"),

]