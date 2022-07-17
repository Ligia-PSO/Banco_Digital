
from contas.models.conta import ContaBancaria
from operacoes.models.movimentacao import Movimentacao
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.consulta_serializer import ConsultarSerializer
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer

from rest_framework import viewsets,permissions,filters
from rest_framework.response import Response
from rest_framework import status
from contas.models.conta import ContaBancaria
from django.db.models import Q
from operacoes.models.transferencia import Transferencia
from operacoes.serializers.transferencia_serializer import TransferenciaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

# from operacoes.transferencia_filtro import TransferenciaFilter

class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset =Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):#POST
        self.fazer_transferencia(request)
        super().create(request,*args,**kwargs)
        return Response({'message':'Transferencia Realizada '},status=status.HTTP_200_OK)

    def fazer_transferencia(self,request)->None:

        data=request.data
        conta_envia=ContaBancaria.objects.get(conta=data['conta'])
        conta_envia.saldo+=-float(data['quantidade'])
        conta_envia.save()
        conta_benef=ContaBancaria.objects.get(conta=data['beneficiario'])
        conta_benef.saldo+=float(data['quantidade'])
        conta_benef.save()
        pass




