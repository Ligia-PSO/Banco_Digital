
import uuid
import random
from django.db import models
from contas.constantes import CONTA_TIPO

from contas.models.cliente import Cliente
# from operacoes.models import Transferencia

class ContaBancaria(models.Model):

    random.seed(10)
    rand_num = random.randrange(10000, 99999)
    titular=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    conta=models.PositiveIntegerField(primary_key=True,default=rand_num,editable=False)
    saldo=models.FloatField(default=0)
    tipo = models.CharField(max_length=8, choices=CONTA_TIPO, default='Corrente')

    def __str__(self) -> str:
        return '{} {}'.format(self.titular, self.conta)
 