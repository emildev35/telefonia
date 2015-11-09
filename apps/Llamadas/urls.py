from django.conf.urls import patterns, url
from .views import HomeView, TarifaView, ImportarDatosView
from .views import HorarioView, LlamadasView, LlamadasUsuarioView
from .views import LlamadasOficinaView, LlamadasPersonalesView as LLPV
from .views import LlamadaDetalle
from .views import CdrList, CdrDetail

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='llamadas_home'),
    url(r'^tarifa$', TarifaView.as_view(), name='llamadas_tarifa'),
    url(r'^horario$', HorarioView.as_view(), name='llamadas_horario'),
    url(r'^importdata$', ImportarDatosView.as_view(), name='llamadas_import'),
    url(r'^llamadas$', LlamadasView.as_view(), name='llamadas_llamadas'),
    url(r'^llamada/(?P<pk>[0-9]+)/$', LlamadaDetalle.as_view(), name='llamada_detalle'),
    url(r'^usuario$', LlamadasUsuarioView.as_view(), name='llamadas_usuario'),
    url(r'^oficina$', LlamadasOficinaView.as_view(), name='llamadas_oficina'),
    url(r'^misllamdas$', LLPV.as_view(), name='llamadas_personales'),
    url(r'^cdr$', CdrList.as_view(), name='llamadas_cdr'),
    url(r'^cdr/(?P<pk>[0-9]+)/$', CdrDetail.as_view(), name='llamada_cdr_detalle'),
)

# ajax views
urlpatterns += patterns(
    '',
    url(
        r'^grid_llamada',
        'apps.Llamadas.ajaxs.jqgrid_llamadas',
        name='jqgrid_llamadas'
    ),
)
