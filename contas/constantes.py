SALARIO='S'
CORRENTE='C'
POUPANCA='P'

CONTA_TIPO = [
        (SALARIO, 'Salário'),
        (CORRENTE, 'Corrente'),
        (POUPANCA, 'Poupança'),
    ]

PESSOA_FISICA = 'PF'
PESSOA_JURIDICA = 'PJ'

FEMININO='F'
MASCULINO='M'

CLIENTE_CHOICES = [
    (PESSOA_FISICA, 'Fisica'),
    (PESSOA_JURIDICA, 'Juridica'),
]
CLIENTE_GENERO = [
    (FEMININO, 'Feminino'),
    (MASCULINO, 'Masculino'),
]