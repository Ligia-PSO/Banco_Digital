
import uuid
import random
from django.db import models

from contas.models.cliente import Cliente
# from operacoes.models import Transferencia

class ContaBancaria(models.Model):
    CONTA_TIPO = [
        ('S', 'Salário'),
        ('C', 'Corrente'),
        ('P', 'Poupança'),
    ]

    rand_num = random.randrange(10000, 99999)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    conta=models.PositiveIntegerField(primary_key=True,default=rand_num,editable=False)
    saldo=models.FloatField(default=0)
    tipo = models.CharField(max_length=8, choices=CONTA_TIPO, default='Corrente')

    def __str__(self) -> str:
        return '{} {}'.format(self.cliente, self.conta)
    

    # def transferencias(self):
    #     return Transferencia.objects()

    # def operacoes(self):
    #     return Transferencia.objects()
