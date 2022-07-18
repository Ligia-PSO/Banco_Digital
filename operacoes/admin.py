from django.contrib import admin
from operacoes.models.transferencia import Transferencia

class TransferenciaAdmin(admin.ModelAdmin):
    list_display=('conta','beneficiario','quantidade','data')

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display=('conta','tipo','quantidade','data')
    
   

admin.site.register(Transferencia,TransferenciaAdmin)
# Register your models here.
