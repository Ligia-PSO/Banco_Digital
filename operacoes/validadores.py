from contas.models.contabancaria import ContaBancaria
from operacoes.exceptions.operacoes_error import ContaBancariaNotFoundError



def valida_contabancaria(data)->bool:

    contas_cadastradas=[x['conta'] for x in ContaBancaria.objects.all().values()]
        
    if int(data['beneficiario']) not in contas_cadastradas:
        raise ContaBancariaNotFoundError({"beneficiario":"Conta Bancaria não existe"})
    return True
    