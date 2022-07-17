import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# from contas.models.cliente import Cliente

class ClienteTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_cliente_nome_error(self):
        # dado
        cliente = {"nome": "","cnpj":"12345670001234","endereco":"rua teste",
        "tipo":"PJ"}

        # quando
        response = self.client.post('/cliente/', cliente, format='json')

        # entao
        self.assertEqual(
            json.loads(response.content), {
                "nome": ["Este campo não pode ser em branco."]}
        )