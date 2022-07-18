
from rest_framework import generics
from contas.models.contabancaria import ContaBancaria
from contas.serializers.consulta_conta_saldo_serializer import ConsultaContaSaldoSerializer

class ConsultaContaSaldoViewset(generics.ListAPIView):
    def get_queryset(self):
        queryset = ContaBancaria.objects.filter(conta=self.kwargs['pk'])
        
        return queryset
    serializer_class = ConsultaContaSaldoSerializer