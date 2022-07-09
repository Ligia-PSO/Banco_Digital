import uuid
from django.db import models

class Cliente(models.Model):
    PESSOA_FISICA = 'PF'
    PESSOA_JURIDICA = 'PJ'
    FEMININO='F'
    MASCULINO='M'

    CLIENTE_CHOICES = [
        (PESSOA_FISICA, 'Fisica'),
        (PESSOA_JURIDICA, 'Juridica'),
    ]
    CLIENTE_GENERO = [
        (PESSOA_FISICA, 'Feminino'),
        (PESSOA_JURIDICA, 'Masculino'),
    ]
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nome = models.CharField(max_length=100,null=False)
    sobrenome=models.CharField(max_length=100,default='')
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=11, null=True,unique=True)
    cnpj = models.CharField(max_length=14, null=True,unique=True)
    tipo = models.CharField(max_length=2, choices=CLIENTE_CHOICES)
    genero = models.CharField(max_length=2, choices=CLIENTE_GENERO)

    def __str__(self) -> str:
        return '{} {}'.format(self.nome, self.sobrenome)

    @property
    def full_name(self):
        return '{} {}'.format(self.nome, self.sobrenome)
