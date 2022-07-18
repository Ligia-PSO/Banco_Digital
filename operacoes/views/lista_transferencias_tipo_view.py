
from rest_framework import generics
from operacoes.models.transferencia import Transferencia

from django.db.models import Q

from operacoes.serializers.lista_transferencias_tipo_serializer import ListaTransferenciasTipoSerializer

class ListaTransferenciasTipoViewset(generics.ListAPIView):
    def get_queryset(self):
        if self.kwargs['pk2']=='enviado':
            queryset=Transferencia.objects.filter(Q(conta_id=self.kwargs['pk']))
        if self.kwargs['pk2']=='recebido':
            queryset=Transferencia.objects.filter(Q(beneficiario=self.kwargs['pk']))

        # queryset = Transferencia.objects.filter(Q(beneficiario=self.kwargs['pk'])|Q(conta_id=self.kwargs['pk']))
        return queryset
        
    serializer_class = ListaTransferenciasTipoSerializer
