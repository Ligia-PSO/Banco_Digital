from rest_framework import serializers
from contas.models.contabancaria import ContaBancaria

class ListaContasBancariasSerializer(serializers.HyperlinkedModelSerializer):
    saldo= serializers.HyperlinkedIdentityField(view_name='consultasaldo', read_only=True)

    class Meta:
        model = ContaBancaria
        fields = [
            'titular',
            'saldo',
            'conta',
            'tipo'
        ]
