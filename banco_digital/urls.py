"""configuracoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from contas.views.cliente_view import ClienteViewSet
from contas.views.consulta_saldo_view import ConsultaContaSaldoViewset
from contas.views.conta_bancaria_view import ContaBancariaViewSet
from contas.views.lista_contas_bancarias_view import ListaContasBancariasViewset
from operacoes.views.consulta_view import ConsultarViewSet
from operacoes.views.lista_transferencias_conta_view import ListaTransferenciasViewset
from operacoes.views.movimentacao_view import MovimentacaoViewSet
from operacoes.views.transferecia_view import TransferenciaViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet,basename='cliente')
router.register(r'contabancaria', ContaBancariaViewSet,basename='contabancaria')
router.register(r'transferencia', TransferenciaViewSet,basename='transferencia')
# router.register(r'movimentacao', MovimentacaoViewSet,basename='movimentacao')
router.register(r'consultartransferencia', ConsultarViewSet,basename='consultar')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contabancaria/<int:pk>/transferencias/', ListaTransferenciasViewset.as_view()),
    # path('contabancaria/<int:pk>/transferencias/recebido', ListaTransferenciasRecebidasViewset.as_view()),
    # path('contabancaria/<int:pk>/transferencias/enviado', ListaTransferenciasEnviadasViewset.as_view()),
    # path('contabancaria/<int:pk>/transferencias/<str:date1>_<str:date2>', ListaTransferenciasIntervaloViewset.as_view()),
    path('contabancaria/todas', ListaContasBancariasViewset.as_view()),
    path('contabancaria/<int:pk>/saldo', ConsultaContaSaldoViewset.as_view(),name='consultasaldo'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
