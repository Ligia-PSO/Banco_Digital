from multiprocessing import context
from rest_framework import serializers

from operacoes.models.transferencia import Transferencia

class ListaTransferenciasContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transferencia
        fields = [
            'conta',
            'quantidade',
            'beneficiario',
            'data'
        ]
