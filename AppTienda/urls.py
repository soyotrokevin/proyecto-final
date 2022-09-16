from django.urls import path    
from AppTienda import views
from .views import PostCreateView

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('about/', views.acerca_de, name = "acerca_de"),
    path('create/', PostCreateView.as_view(), name='posteo_nuevo'),

]