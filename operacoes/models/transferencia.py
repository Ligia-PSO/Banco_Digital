from django.db import models
import uuid

from contas.models.conta import ContaBancaria


class Transferencia(models.Model):

    conta=models.ForeignKey(ContaBancaria, on_delete=models.CASCADE,null=True)#qual a conta que está enviando
    Transfer_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    beneficiario=models.IntegerField()#conta que irá receber
    data=models.DateField(auto_now_add=True)
    quantidade=models.DecimalField(decimal_places=2,max_digits=12)
    tipo = models.CharField(max_length=13, default="enviada")
    
    def __str__(self) -> str:
        return '{} {}'.format(self.conta,self.tipo)

    class Meta:
        ordering = ['data']