from rest_framework import serializers
from contas.models.cliente import Cliente
from contas.validadores import somente_inteiros, somente_letras, validar_cpf_cnpj




class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    cnpj=serializers.CharField(min_length=14,max_length=14,
                            allow_blank=False, allow_null=True,required=False,validators=[somente_inteiros])

    cpf = serializers.CharField(min_length=11,max_length=11,
                            allow_blank=False, allow_null=True,required=False,validators=[somente_inteiros])
    
    nome= serializers.CharField(allow_null=False,validators=[somente_letras])
    sobrenome=serializers.CharField(allow_null=False,validators=[somente_letras])
    endereco= serializers.CharField(allow_null=False,validators=[somente_letras])
   
    class Meta():
        model = Cliente
        fields = ['nome','sobrenome','endereco', 'cpf', 'cnpj','tipo']

    def validate(self, data):
        
        validar_cpf_cnpj(data)

        return data