from rest_framework import serializers
from contas.exceptions.contas_database_error import DuplicatedCNPJ, DuplicatedCPF
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
    
    def validate_cpf(self,cpf):
        cpf_cadastradas=[x['cpf'] for x in Cliente.objects.all().values()]
        
        if int(cpf)in cpf_cadastradas:
            raise DuplicatedCPF({"cpf":"CPF ja cadastrado"})
        
        return cpf
    
    def validate_cnpj(self,cnpj):
        cnpj_cadastradas=[x['cnpj'] for x in Cliente.objects.all().values()]
        if int(cnpj)in cnpj_cadastradas:
            raise DuplicatedCNPJ({"cnpj":'CNPJ ja cadastrada'})
        return cnpj
