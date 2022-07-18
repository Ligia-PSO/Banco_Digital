from rest_framework import serializers
from contas.models.cliente import Cliente
from contas.validadores import somente_inteiros, somente_letras


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
        # valida cpf e cnpj para os tipos certos de clientes;
        # Pessoa fisica nao pode ter CNPJ e Pessoa juridica nao pode ter CPF

        if (data.get("tipo") == 'PJ'):
            if (data.get("cnpj") == None ) :
                raise serializers.ValidationError(
                    {'cnpj': 'Se é uma pessoa juridica, o cnpj é obrigatorio'})

            if(data.get("cpf")!=None):
                raise serializers.ValidationError(
                    {'cpf':'Pessoa juridica nao tem cpf'})

        elif (data.get("tipo") == 'PF'):

            if (data.get("cpf") == None) :
                 raise serializers.ValidationError(
                    {'cpf':'Se é uma pessoa física o cpf é obrigatorio'})
                    
            if (data.get("cnpj") != None ) :
                 raise serializers.ValidationError({"cnpj":
                   'Pessoa física nao tem cnpj'})

        return data