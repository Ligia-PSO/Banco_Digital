import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User

from contas.models.cliente import Cliente

# from contas.models.cliente import Cliente

# class TransferenciaTestCase(TestCase):

#     @classmethod
#     def setUp(self) -> None:
   
#         client = APIClient()

    # def test_cliente_post_sucesso(self):
    #     # dado
    #     cliente = {"nome": "Marcia","sobrenome": "Alvares","cnpj":"12345670001234","endereco":"rua teste",
    #     "tipo":"PJ"}

    #     # quando
    #     response = self.client.post('/cliente/', cliente, format='json')

    #     # entao
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_cliente_create(self):
    #     # dado
    #     cliente = {"nome": "Marcia","sobrenome": "Alvares","cnpj":"12345670001234","endereco":"rua teste",
    #     "tipo":"PJ"}

    #     # quando
    #     Cliente.objects.create(**cliente)
    #     cliente_cadastrado = Cliente.objects.get(cnpj="12345670001234")

    #     # entao
    #     self.assertEqual(cliente_cadastrado.nome, 'Marcia')

    # def test_cliente_cpf_tamanho_error(self):
    #     # dado
    #     cliente = {"nome": "Marcia",'cpf':'123456789011',"sobrenome": "Alvares","endereco":"rua teste",
    #     "tipo":"PF"}

    #     # quando
    #     response = self.client.post('/cliente/', cliente, format='json')

    #     # entao
    #     self.assertEqual(json.loads(response.content), {
    #             "cpf": ['Certifique-se de que este campo não tenha mais de 11 caracteres.']}
    #     )
    
    # def test_cliente_cnpj_tamanho1_error(self):
    #     cliente = {"nome": "Marcia","sobrenome": "Alvares","cnpj":"123456700012345","endereco":"rua teste",
    #     "tipo":"PJ"}

    # #     # quando
    #     response = self.client.post('/cliente/', cliente, format='json')

    # #     # entao
    #     self.assertEqual(json.loads(response.content), {
    #             "cnpj": ['Certifique-se de que este campo não tenha mais de 14 caracteres.']})

    # def test_cliente_cnpj_tamanho2_error(self):
    #     cliente = {"nome": "Marcia","sobrenome": "Alvares","cnpj":"1234567000123","endereco":"rua teste",
    #     "tipo":"PJ"}

    # #     # quando
    #     response = self.client.post('/cliente/', cliente, format='json')

    # #     # entao
    #     self.assertEqual(json.loads(response.content), {
    #             "cnpj": ['Certifique-se de que este campo tenha mais de 14 caracteres.']})

    # def test_cliente_cnpj_int_error(self):
    #     cliente = {"nome": "Marcia","sobrenome": "Alvares","cnpj":"1234567000123a","endereco":"rua teste",
    #     "tipo":"PJ"}

    # #     # quando
    #     response = self.client.post('/cliente/', cliente, format='json')

    # #     # entao
    #     self.assertEqual(json.loads(response.content), {
    #             "cnpj":["Campo somente pode conter numeros inteiros"]})

    