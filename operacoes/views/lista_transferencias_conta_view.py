
from rest_framework import generics
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.lista_transferencias_conta_serializer import ListaTransferenciasContaSerializer
from django.db.models import Q



class ListaTransferenciasViewset(generics.ListAPIView):
    def get_queryset(self):
        queryset = Transferencia.objects.filter(Q(beneficiario=self.kwargs['pk'])|Q(conta_id=self.kwargs['pk']))
        return queryset

    # def post(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    serializer_class = ListaTransferenciasContaSerializer
