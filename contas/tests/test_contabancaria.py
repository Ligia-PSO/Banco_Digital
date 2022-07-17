import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User

from contas.models.cliente import Cliente
from contas.models.contabancaria import ContaBancaria


# from contas.models.cliente import Cliente
# path('contabancaria/<int:pk>/saldo', ConsultaContaSaldoViewset.as_view(),name='consultasaldo')
class ContaBancariaTestCase(TestCase):

    @classmethod
    def setUp(cls) -> None:
        client = APIClient()
        cliente = {"nome": "Marcia","sobrenome": "Alvares","cpf":"12345670001","endereco":"rua teste",
        "tipo":"PF"}
        Cliente.objects.create(**cliente)

        cls.titular_id=Cliente.objects.get(cpf="12345670001").id

    def test_conta_bancaria_post_sucesso(self):
        # dado
        conta_bancaria = {"titular": str(self.titular_id),"saldo": "120","tipo":"S"}

        # quando
        response = self.client.post('/contabancaria/', conta_bancaria, format='json')

        # entao
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_conta_bancaria_create(self):
    #     # dado
        
        conta_bancaria = {"titular": str(self.titular_id),"saldo": "120","tipo":"S"}

    #     # quando
        ContaBancaria.objects.create(**conta_bancaria)
        cliente_cadastrado = ContaBancaria.objects.get(titular_id=self.titular_id)

    #     # entao
        self.assertEqual(cliente_cadastrado.saldo, '120')