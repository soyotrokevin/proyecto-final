from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, "AppTienda/home.html")

def acerca_de(request):
    return render(request, "AppTienda/acerca_de_mi.html")