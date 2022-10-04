from turtle import title
from django.test import TestCase

from AppTienda.models import Post
import random
import string

class PostTestCase(TestCase):
    pass

    def test_creacion_post(self):
        letras_titulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        titulo_prueba = "".join(letras_titulo)
        post_1 = Post.objects.create(title=titulo_prueba)

        self.assertIsNotNone(post_1.id)
        self.assertEqual(post_1.title, titulo_prueba)




