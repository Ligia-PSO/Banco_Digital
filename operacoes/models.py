from django.db import models
import uuid

from contas.models.conta import ContaBancaria

class Transferencia(models.Model):
    TIPO = [
        ("transferencia", 'tranferencia'),
        ("recebimento", 'recebimento'),
        # ("deposito", 'deposito de dinheiro'),
        # ("saque", 'saque de dinheiro'),
    ]
    
    conta=models.ForeignKey(ContaBancaria, on_delete=models.CASCADE)
    Transfer_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    destinatario=models.IntegerField()#conta
    remetente=models.IntegerField()#conta
    tipo = models.CharField(max_length=13, choices=TIPO, default="transferencia")
    data=models.DateTimeField(auto_now_add=True)
    quantidade=models.DecimalField(decimal_places=2,max_digits=12)

    def __str__(self) -> str:
        return '{} {}'.format(self.conta,self.tipo)

    class Meta:
        ordering = ['data']
#     pass

class Movimentacao(models.Model):
    TIPO = [
        ("deposito", 'deposito'),
        ("saque", 'saque'),
    ]
    
    conta=models.ForeignKey(ContaBancaria,on_delete=models.CASCADE,null=True)
    tipo = models.CharField(max_length=10, choices=TIPO, default="deposito")
    quantidade=models.DecimalField(decimal_places=2,max_digits=12,default=0)

    def __str__(self) -> str:
        return '{} {}'.format(self.conta,self.tipo)