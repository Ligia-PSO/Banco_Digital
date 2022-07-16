from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets, filters
from contas.models.cliente import Cliente


from contas.serializers.client_serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClienteViewSet(viewsets.ModelViewSet):
    queryset =Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['=nome','cpf','cnpj']
    ordering_fields = ['nome']
    

    def list(self, request):
        clientes=Cliente.objects.all()
        valores=Cliente.objects.all().values()

        serializer=ClienteSerializer(clientes,many=TRUE)
        for x in valores:
            print(x['id'])
        print(serializer.data)
        
        
        return Response(serializer.data)
        
    def create(self,request,*args,**kwargs):
        return super().create(request,*args,**kwargs)

    def retrieve(self, request, *args,**kwargs):
        params=kwargs
        parametro_de_pesquisa=params['pk']
        print(request)
        if len(str(parametro_de_pesquisa))==11:#cpf
            clientes=Cliente.objects.filter(cpf=parametro_de_pesquisa)
        if len(str(parametro_de_pesquisa))==14:#cnpj
            clientes=Cliente.objects.filter(cnpj=parametro_de_pesquisa)
        else:
            clientes=Cliente.objects.filter(id=parametro_de_pesquisa)
        
        serializer=ClienteSerializer(clientes,many=True)
    
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
