

from operacoes.models.movimentacao import Movimentacao
from rest_framework import viewsets,permissions

from operacoes.serializers.movimentacao_serializer import MovimentacaoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset =Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # def get(self,request,*args,**kwargs):
    #     transferencias=self.get_queryset()
    #     # serializer=TransferenciaSerializer(transferencias,many=True)
    #     return Response({'ola':''})
    pass