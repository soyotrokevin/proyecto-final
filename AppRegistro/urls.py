from django.urls import path
from AppRegistro import views 

urlpatterns = [
    
    path('register/', views.register, name = 'register'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
    path('profile/', views.ProfileUpdateView.as_view(), name="profile"),
]
