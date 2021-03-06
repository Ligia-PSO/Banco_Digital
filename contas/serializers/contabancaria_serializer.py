from rest_framework import serializers

from contas.models.contabancaria import ContaBancaria


class ContaBancariaSerializer(serializers.ModelSerializer):
    

    class Meta():
        model = ContaBancaria
        fields = ['conta', 'titular', 'saldo', 'tipo']
