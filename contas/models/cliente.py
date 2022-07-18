import uuid
from django.db import models

from contas.constantes import CLIENTE_CHOICES

class Cliente(models.Model):
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nome = models.CharField(max_length=100,null=False)
    sobrenome=models.CharField(max_length=100,default='')
    endereco = models.CharField(max_length=100)
    # email=models.EmailField()
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11, null=True,unique=True)
    cnpj = models.CharField(max_length=14, null=True,unique=True)
    tipo = models.CharField(max_length=2, choices=CLIENTE_CHOICES)

    def __str__(self) -> str:
        return '{} {}'.format(self.nome, self.sobrenome)
        