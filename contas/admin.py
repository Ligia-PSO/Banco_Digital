from django.contrib import admin
from contas.models.cliente import Cliente
from contas.models.conta import ContaBancaria

admin.site.register(Cliente)
admin.site.register(ContaBancaria)
# Register your models here.
