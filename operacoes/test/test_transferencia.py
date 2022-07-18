import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from contas.models.cliente import Cliente
from contas.models.contabancaria import ContaBancaria


class TransferenciaTestCase(TestCase):

    @classmethod
    def setUp(cls) -> None:
   
        client = APIClient()

        cliente1 = {"nome": "Marcia","sobrenome": "Alvares","cpf":"12345670001","endereco":"rua teste",
        "tipo":"PF"}
        Cliente.objects.create(**cliente1)
        cliente2 = {"nome": "Breno","sobrenome": "Alvares","cpf":"12345000001","endereco":"rua teste",
        "tipo":"PF"}
        Cliente.objects.create(**cliente2)

        cls.titular_id1=Cliente.objects.get(cpf="12345670001").id
        cls.titular_id2=Cliente.objects.get(cpf="12345000001").id

        conta_bancaria1 = {"titular": str(cls.titular_id1),"saldo": "120","tipo":"S"}
        conta_bancaria2 = {"titular": str(cls.titular_id2),"saldo": "120","tipo":"S"}

        cls.conta1=ContaBancaria.objects.get(titular_id=cls.titular_id1).conta
        cls.conta2=ContaBancaria.objects.get(titular_id=cls.titular_id2).conta

        ContaBancaria.objects.create(**conta_bancaria1)
        ContaBancaria.objects.create(**conta_bancaria2)

    def test_cliente_post_sucesso(self):
    #     # dado
        transf = {"beneficiario": self.conta1,"quantidade": "10","conta": self.conta2}
        response = self.client.post('/transferencia',transf,format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
