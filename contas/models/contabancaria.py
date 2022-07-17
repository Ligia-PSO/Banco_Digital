
import random
from django.db import models

from contas.constantes import CONTA_TIPO
from contas.models.cliente import Cliente



# from operacoes.models import Transferencia

class ContaBancaria(models.Model):

    def __str__(self) -> str:
        return '{} {}'.format(self.titular, self.conta)
    
    def conta_num_aleatorio()->int:
                nao_unico = True
                while nao_unico:
                    numero_aleatorio = random.randint(10000, 99999)
                    if not ContaBancaria.objects.filter(conta=numero_aleatorio):
                        numero_aleatorio = False
                return numero_aleatorio
                
    titular=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    conta=models.PositiveIntegerField(primary_key=True,default=conta_num_aleatorio,editable=False)
    saldo=models.FloatField(default=0)
    tipo = models.CharField(max_length=8, choices=CONTA_TIPO, default='Corrente')
    