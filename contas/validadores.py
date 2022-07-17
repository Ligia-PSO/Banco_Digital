from django.core.exceptions import ValidationError
from rest_framework import serializers

def somente_inteiros(value): 
    if value.isdigit()==False:
        raise ValidationError('Campo somente pode conter numeros inteiros')
def somente_letras(value): #somente aceita espaços e letras
    if not all(x.isalpha() or x.isspace() for x in value):
        raise ValidationError('Campo somente pode conter letras')

def validar_cpf_cnpj(data):

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