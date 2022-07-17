

from contas.models.conta import ContaBancaria
from operacoes.models.movimentacao import Movimentacao
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.consulta_serializer import ConsultarSerializer
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer

from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status
from contas.models.conta import ContaBancaria
from django.db.models import Q
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer



class ConsultarViewSet(viewsets.ModelViewSet):
    queryset =Movimentacao.objects.all()
    serializer_class = ConsultarSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request,):
        return Response({'informe as datas a serem consultadas'},status=status.HTTP_200_OK)
    
    def create(self, request):#POST
        transf=self.filtrar_transferencias(request)#transferencias feitas no periodo
        serializer=TransferenciaSerializer(transf,many=True)
            
        return Response(serializer.data)


    def filtrar_transferencias(self,request):
        consulta=request.data
        if consulta['tipo']=='transferencias':
            # Entry.objects.filter(pub_date__range=(start_date, end_date))
            transferencias=Transferencia.objects.filter(Q(beneficiario=consulta['conta'])
            |Q(conta_id=consulta['conta']),data__gte=consulta['data_inicio'],data__lte=consulta['data_fim'])
        
        return transferencias
