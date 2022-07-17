from rest_framework import serializers
import re

from contas.models.contabancaria import ContaBancaria


class ContaBancariaSerializer(serializers.ModelSerializer):
    

    class Meta():
        model = ContaBancaria
        fields = ['conta', 'titular', 'saldo', 'tipo']
        # fields='__all__'

    def validate_conta(self, conta):
        return conta