from rest_framework import serializers
from contas.models.contabancaria import ContaBancaria
from operacoes.exceptions.operacoes_error import SaldoInsuficienteError, TransferenciaError
from operacoes.models.transferencia import Transferencia

class TransferenciaSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Transferencia
        exclude = ('Transfer_id',)
        # fields='__all__'


    def validate(self, data):
        
        if data.get('beneficiario')==data.get('conta').conta:
            raise TransferenciaError({"beneficiario":["Não se pode realizar transferências para a mesma conta"]})
    
        conta_bancaria=ContaBancaria.objects.get(conta=data.get('conta').conta)

        if conta_bancaria.saldo<data.get('quantidade'):
            raise SaldoInsuficienteError({"quantidade":["Saldo insuficiente"]})
       
        return data
    
    def validate_quantidade(self, qtd):
        if int(qtd)<0:
            raise TransferenciaError("Quantidade de transferencia não pode ser negativa")
        if int(qtd)==0:
            raise TransferenciaError("Quantidade de transferencia não pode ser nula")
        
        return qtd
    

