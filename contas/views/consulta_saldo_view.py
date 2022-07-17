
from rest_framework import generics
from contas.models.contabancaria import ContaBancaria
from contas.serializers.consulta_conta_saldo_serializer import ConsultaContaSaldoSerializer
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.lista_transferencias_conta_serializer import ListaTransferenciasContaSerializer

class ConsultaContaSaldoViewset(generics.ListAPIView):
    def get_queryset(self):
        queryset = ContaBancaria.objects.filter(conta=self.kwargs['pk'])
        
        return queryset
    serializer_class = ConsultaContaSaldoSerializer