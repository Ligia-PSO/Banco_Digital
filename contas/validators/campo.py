from django.core.exceptions import ValidationError
def somente_inteiros(value): 
    if value.isdigit()==False:
        raise ValidationError('Campo somente pode conter numeros inteiros')
def somente_letras(value): 
    if value.isalpha()==False:
        raise ValidationError('Campo somente pode conter letras')