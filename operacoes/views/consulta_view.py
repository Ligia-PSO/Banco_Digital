
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.consulta_serializer import ConsultarSerializer
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer

from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer
from django.http import HttpResponseRedirect


class ConsultarViewSet(viewsets.ModelViewSet):
    queryset =Transferencia.objects.all()
    serializer_class = ConsultarSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request,):
        return Response({'informe as datas a serem consultadas'},status=status.HTTP_200_OK)
    
    def create(self, request):#POST
        consulta=request.data
        transf=self.filtrar_transferencias(request)#transferencias feitas no periodo
        serializer=TransferenciaSerializer(transf,many=True)
        
        return Response(serializer.data)


    def filtrar_transferencias(self,request):
        consulta=request.data
        if consulta['tipo']=='todos':
            # Entry.objects.filter(pub_date__range=(start_date, end_date))
            transferencias=Transferencia.objects.filter(Q(beneficiario=consulta['conta'])
            |Q(conta_id=consulta['conta']),data__gte=consulta['data_inicio'],data__lte=consulta['data_fim'])
        
        elif consulta['tipo']=='recebido':
            transferencias=Transferencia.objects.filter(beneficiario=consulta['conta']
            ,data__gte=consulta['data_inicio'],data__lte=consulta['data_fim'])

        elif consulta['tipo']=='enviado':
             transferencias=Transferencia.objects.filter(conta_id=consulta['conta'],
             data__gte=consulta['data_inicio'],data__lte=consulta['data_fim'])

        return transferencias
