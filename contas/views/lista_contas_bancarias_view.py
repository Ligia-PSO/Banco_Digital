from rest_framework import generics
from contas.models.conta import ContaBancaria
from contas.serializers.lista_contas_bancarias_serializer import ListaContasBancariasSerializer
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.lista_transferencias_conta_serializer import ListaTransferenciasContaSerializer
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ListaContasBancariasViewset(generics.ListAPIView):
    def get_queryset(self):
        queryset = ContaBancaria.objects.all()  
        return queryset
    

    serializer_class = ListaContasBancariasSerializer
