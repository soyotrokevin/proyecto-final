from django.urls import path
from AppRegistro import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
]
