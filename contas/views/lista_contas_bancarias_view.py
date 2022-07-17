from rest_framework import generics
from contas.models.contabancaria import ContaBancaria
from contas.serializers.lista_contas_bancarias_serializer import ListaContasBancariasSerializer

class ListaContasBancariasViewset(generics.ListAPIView):
    def get_queryset(self):
        queryset = ContaBancaria.objects.all()  
        return queryset
    

    serializer_class = ListaContasBancariasSerializer
