
from contas.models.conta import ContaBancaria
from operacoes.models.movimentacao import Movimentacao
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.consulta_serializer import ConsultarSerializer
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer

from rest_framework import viewsets,permissions,filters
from rest_framework.response import Response
from rest_framework import status
from contas.models.conta import ContaBancaria

from operacoes.models.transferencia import Transferencia
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset =Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response({'consulte as transferencias aqui: http://127.0.0.1:8000/consultar/'},status=status.HTTP_200_OK)
    
    def create(self,request,*args,**kwargs):#POST
        data=request.data
        conta_envia=ContaBancaria.objects.get(conta=data['conta'])
        conta_envia.saldo+=-float(data['quantidade'])
        conta_envia.save()
        conta_benef=ContaBancaria.objects.get(conta=data['beneficiario'])
        conta_benef.saldo+=float(data['quantidade'])
        conta_benef.save()

        super().create(request,*args,**kwargs)
        return Response({'message':'Transferencia Realizada '},status=status.HTTP_200_OK)
    
    # def get(self,request,*args,**kwargs):
    #     transferencias=self.get_queryset()
    #     # serializer=TransferenciaSerializer(transferencias,many=True)
    #     return Response({'ola':''})
    pass


class ConsultarViewSet(viewsets.ModelViewSet):
    queryset =Movimentacao.objects.all()
    serializer_class = ConsultarSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['nome','cpf','cnpj']
    ordering_fields = ['nome']

    

    def list(self, request,):
       
        return Response({'informe as datas a serem consultadas'},status=status.HTTP_200_OK)
    
    def create(self, request):#POST
        consulta=request.data
        
        if consulta['tipo']=='transferencias':
            # Entry.objects.filter(pub_date__range=(start_date, end_date))
            transferencias=Transferencia.objects.filter(Q(beneficiario=consulta['conta'])|Q(conta_id=consulta['conta']))
            serializer=TransferenciaSerializer(transferencias,many=True)
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pass