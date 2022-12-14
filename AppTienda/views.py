from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def inicio(request):
    context = {
        'posts': Post.objects.all(),
    }

    
    return render(request, "AppTienda/home.html", context)


def acerca_de(request):
    return render(request, "AppTienda/acerca_de_mi.html")


class PostListView(ListView):
    model = Post
    template_name = 'AppTienda/home.html' 
    context_object_name = 'posts'
    ordering = ['date_posted']

class UserPostListView(ListView):
    model = Post
    template_name = 'AppTienda/my_post.html'  
    context_object_name = 'posts'
   

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url =  reverse_lazy('inicio')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False