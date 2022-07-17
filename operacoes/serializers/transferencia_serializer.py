from rest_framework import serializers
import re
from contas.models.conta import ContaBancaria
from operacoes.models.transferencia import Transferencia


# Serializers define the API representation.
class TransferenciaSerializer(serializers.ModelSerializer):
    # tipo=serializers.ReadOnlyField()
    # cliente = serializers.ReadOnlyField(source='cliente.nome')
    
    class Meta():
        model = Transferencia
        exclude = ('Transfer_id','tipo')
        # fields='__all__'

    def validate_beneficiario(self, beneficiario):
        contas_cadastradas=[x['conta'] for x in ContaBancaria.objects.all().values()]
        if beneficiario not in contas_cadastradas:
            raise serializers.ValidationError(
                "conta do beneficiario incorreta")

        return beneficiario

    def validate_quantidade(self, quantidade):
        return quantidade

