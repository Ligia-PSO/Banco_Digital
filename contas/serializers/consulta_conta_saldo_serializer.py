from rest_framework import serializers
from contas.models.contabancaria import ContaBancaria

from operacoes.models.transferencia import Transferencia

class ConsultaContaSaldoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContaBancaria
        fields = [
            'saldo',
        ]
