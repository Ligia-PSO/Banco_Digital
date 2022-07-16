from django.contrib import admin
from operacoes.models.movimentacao import Movimentacao
from operacoes.models.transferencia import Transferencia

class TransferenciaAdmin(admin.ModelAdmin):
    list_display=('conta','beneficiario','quantidade','data')

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display=('conta','tipo','quantidade','data')
    
   

admin.site.register(Transferencia,TransferenciaAdmin)
admin.site.register(Movimentacao,MovimentacaoAdmin)
# Register your models here.
