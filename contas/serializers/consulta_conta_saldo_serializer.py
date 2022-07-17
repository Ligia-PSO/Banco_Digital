from rest_framework import serializers
from contas.models.conta import ContaBancaria

from operacoes.models.transferencia import Transferencia

class ConsultaContaSaldoSerializer(serializers.ModelSerializer):
    # conta = serializers.ReadOnlyField(source='conta.conta')

    class Meta:
        model = ContaBancaria
        fields = [
            'saldo',
        ]
