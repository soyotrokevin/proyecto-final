from django.db import models
from django.contrib.auth.models import User

  
class Pedidos (models.Model):
    marca = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.email}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"
