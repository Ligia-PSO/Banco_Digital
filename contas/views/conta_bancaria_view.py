from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from contas.models.cliente import Cliente
from contas.models.conta import ContaBancaria


from contas.serializers.conta_serializer import ContaBancariaSerializer


class ContaBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaBancariaSerializer
    queryset = ContaBancaria.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    
    def list(self, request):
        queryset = ContaBancaria.objects.all()
        # return super().list(request)
        return Response(ContaBancariaSerializer(queryset,many=True,context={'request': request}).data)
        # return HttpResponse('<h1>please, enter your username</h1>')

    def create(self,request,*args,**kwargs):
        return super().create(request,*args,**kwargs)

    def retrieve(self, request, *args,**kwargs):
        params=kwargs
        parametro_de_pesquisa=params['pk']
    
        conta_=ContaBancaria.objects.filter(conta=parametro_de_pesquisa)
        serializer=ContaBancariaSerializer(conta_,many=True,context={'request': request})
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

