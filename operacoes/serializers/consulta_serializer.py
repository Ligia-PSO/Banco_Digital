from rest_framework import serializers
from contas.models.contabancaria import ContaBancaria
from operacoes.constantes import TIPO_CONSULTA
from datetime import datetime

from operacoes.exceptions.operacoes_error import ContaBancariaNotFoundError, InvalidDate


class ConsultarSerializer(serializers.Serializer):
    
    data_inicio=serializers.DateField()
    data_fim=serializers.DateField()
    tipo=serializers.ChoiceField(choices=TIPO_CONSULTA)
    conta=serializers.IntegerField()

    
    
    def validate(self,data):

        data_i=str(data.get("data_inicio"))
        data_f=str(data.get("data_fim"))
        hoje = datetime.now().date()

        d1=datetime.strptime(data_i, "%Y-%m-%d").date()
        d2=datetime.strptime(data_f, "%Y-%m-%d").date()
        
        if d1>d2:
            raise InvalidDate(
                    {'data_inicio':'Data inicial nao pode ser depois da final'})
            
        elif d1>hoje:
            raise InvalidDate(
                    {'data_inicio':'Data nao pode ser futura'})
        

        return data

    def validate_conta(self,conta):
        contas_cadastradas=[x['conta'] for x in ContaBancaria.objects.all().values()]
        if conta not in contas_cadastradas:
            raise ContaBancariaNotFoundError(
                "Conta Bancaria nao existe")
        return conta
    
