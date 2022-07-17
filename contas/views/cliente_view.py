from rest_framework import viewsets,permissions,filters
from rest_framework.response import Response
from rest_framework import status
from contas.models.cliente import Cliente


from contas.serializers.cliente_serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset =Cliente.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['nome','cpf','cnpj']
    ordering_fields = ['nome']
    

    # def list(self, request):
    #     clientes=Cliente.objects.all()
    #     valores=Cliente.objects.all().values()

    #     serializer=ClienteSerializer(clientes,many=True)
    #     for x in valores:
    #         print(x['id'])
    #     print(serializer.data)
        
        
        # return Response(serializer.data)
        
    def create(self,request,*args,**kwargs):
        return super().create(request,*args,**kwargs)

    def retrieve(self, request, *args,**kwargs):
        params=kwargs
        parametro_de_pesquisa=params['pk']
        clientes=Cliente.objects.filter(id=parametro_de_pesquisa)
        
        serializer=ClienteSerializer(clientes,many=True,context={'request': request})
    
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
