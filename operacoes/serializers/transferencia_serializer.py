from rest_framework import serializers
import re
from contas.models.contabancaria import ContaBancaria
from contas.validadores import somente_inteiros
from operacoes.models.transferencia import Transferencia


# Serializers define the API representation.
class TransferenciaSerializer(serializers.ModelSerializer):
    # quantidade=serializers.DecimalField(validators=[somente_inteiros])
    
    class Meta():
        model = Transferencia
        exclude = ('Transfer_id',)
        # fields='__all__'


    def validate(self, data):
        
        if data.get('beneficiario')==data.get('conta').conta:
            raise serializers.ValidationError({"beneficiario":["Não se pode realizar transferências para a mesma conta"]})
    
        conta_bancaria=ContaBancaria.objects.get(conta=data.get('conta').conta)

        if conta_bancaria.saldo<data.get('quantidade'):
            raise serializers.ValidationError({"quantidade":["Saldo insuficiente"]})
       
        return data
    
    def validate_quantidade(self, qtd):
        if int(qtd)==0:
            raise serializers.ValidationError("Quantidade de transferencia não pode ser nula")
        # contas_cadastradas=[x['conta'] for x in ContaBancaria.objects.all().values()]
        
        return qtd
    

