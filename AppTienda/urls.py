from django.urls import path    
from AppTienda import views
from .views import PostCreateView,PostDetailView,UserPostListView

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('about/', views.acerca_de, name = "acerca_de"),
    
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    path('create/', PostCreateView.as_view(), name='posteo_nuevo'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostDetailView.as_view(), name='home'),

]