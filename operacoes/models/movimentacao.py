from django.db import models
from contas.models.contabancaria import ContaBancaria

from operacoes.constantes import TIPO_MOVIMENTACAO

class Movimentacao(models.Model):

    conta=models.ForeignKey(ContaBancaria,on_delete=models.CASCADE,null=True)
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMENTACAO, default="deposito")
    quantidade=models.DecimalField(decimal_places=2,max_digits=12,default=0)
    data=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.conta,self.tipo)
    
    class Meta():
        verbose_name_plural='Movimentações'
        ordering = ['data']