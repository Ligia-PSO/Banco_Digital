from django.contrib import admin

from contas.models.cliente import Cliente
from contas.models.contabancaria import ContaBancaria

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome','tipo')


class ContaBancariaAdmin(admin.ModelAdmin):
    list_display=('conta','titular')


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(ContaBancaria,ContaBancariaAdmin)
# Register your models here.
