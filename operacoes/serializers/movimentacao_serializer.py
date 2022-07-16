from rest_framework import serializers
import re
from operacoes.models.movimentacao import Movimentacao


# Serializers define the API representation.
class MovimentacaoSerializer(serializers.ModelSerializer):
    # email=
    # cnpj=serializers.CharField(min_length=14,max_length=14,
    #                         allow_blank=False, allow_null=True,required=False)

    class Meta():
        model = Movimentacao
        # fields = ['nome','endereco', 'cpf', 'cnpj','tipo']
        fields='__all__'
