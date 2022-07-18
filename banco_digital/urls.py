
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from contas.views.cliente_view import ClienteViewSet
from contas.views.consulta_saldo_view import ConsultaContaSaldoViewset
from contas.views.conta_bancaria_view import ContaBancariaViewSet
from contas.views.lista_contas_bancarias_view import ListaContasBancariasViewset
from operacoes.views.consulta_view import ConsultarViewSet
from operacoes.views.lista_transferencias_conta_view import ListaTransferenciasViewset
from operacoes.views.lista_transferencias_tipo_view import ListaTransferenciasTipoViewset
from operacoes.views.transferecia_view import TransferenciaViewSet


router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet,basename='cliente')
router.register(r'contabancaria', ContaBancariaViewSet,basename='contabancaria')
router.register(r'transferencia', TransferenciaViewSet,basename='transferencia')
router.register(r'consultartransferencia', ConsultarViewSet,basename='consultar')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contabancaria/<int:pk>/transferencias/', ListaTransferenciasViewset.as_view()),
    path('contabancaria/<int:pk>/transferencias/<pk2>', ListaTransferenciasTipoViewset.as_view()),
    path('contabancaria/todas', ListaContasBancariasViewset.as_view()),
    path('contabancaria/<int:pk>/saldo', ConsultaContaSaldoViewset.as_view(),name='consultasaldo'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
