from django.urls import path    
from AppTienda import views
from .views import PostCreateView,PostDetailView,UserPostListView,PostDeleteView,PostUpdateView
urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('about/', views.acerca_de, name = "acerca_de"),
    
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('pages/', PostDetailView.as_view(), name='home'),
    path('pages/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('pages/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]