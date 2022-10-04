from django.test import TestCase
from AppRegistro.models import Pedidos
import random
import string

class PedidosTestCase(TestCase):
    

    def test_creacion_post(self):
        letras_prueba = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        pedido_prueba = "".join(letras_prueba)
        pedido_1 = Pedidos.objects.create(marca=pedido_prueba)

        self.assertIsNotNone(pedido_1.id)
        self.assertEqual(pedido_1.marca, pedido_prueba)

    #Test si cumple el máximo de carácteres
    def test_marca_max_length(self):
