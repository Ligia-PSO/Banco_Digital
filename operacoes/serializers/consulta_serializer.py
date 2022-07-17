from multiprocessing import allow_connection_pickling
from rest_framework import serializers
import re
from contas.models.conta import ContaBancaria
from operacoes.constantes import TIPO_CONSULTA

class ConsultarSerializer(serializers.Serializer):
    # email=
    # cnpj=serializers.CharField(min_length=14,max_length=14,
    #                         allow_blank=False, allow_null=True,required=False)
    data_inicio=serializers.DateField()
    data_fim=serializers.DateField()
    tipo=serializers.ChoiceField(choices=TIPO_CONSULTA)
    conta=serializers.IntegerField()

    def validate_conta(self,conta):
        contas_cadastradas=[x['conta'] for x in ContaBancaria.objects.all().values()]
        if conta not in contas_cadastradas:
            raise serializers.ValidationError(
                "Conta nao existe")
        return conta
