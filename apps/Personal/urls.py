from django.conf.urls import patterns, url
from .views import CargoView, CargoList, CargoDetail
from .views import AreaView, AreaList, AreaDetail
from .views import FuncionarioView, FuncionarioList, FuncionarioDetail
from .views import FuncionariosLista, FuncionarioDetalle

urlpatterns = patterns(
    '',
    url(r'^personal/$', FuncionariosLista.as_view(), name='personal_home'),
    url(r'^personal/detail/(?P<pk>[0-9]+)$', FuncionarioDetalle.as_view(), name='personal_detalle'),
    url(r'^cargo/create$', CargoView.as_view(), name='personal_cargo_create'),
    url(r'^cargo/$', CargoList.as_view(), name='personal_cargo_list'),
    url(r'^cargo/(?P<pk>[0-9]+)$', CargoDetail.as_view(), name='personal_cargo_detail'),
    url(r'^area/create$', AreaView.as_view(), name='personal_area_create'),
    url(r'^area/list$', AreaList.as_view(), name='personal_area_list'),
    url(r'^area/(?P<pk>[0-9]+)$', AreaDetail.as_view(), name='personal_area_detail'),
    url(r'^funcionario/create$', FuncionarioView.as_view(), name='personal_funcionario_create'),
    url(r'^funcionario/list$', FuncionarioList.as_view(), name='personal_funcionario_list'),
    url(r'^funcionario/(?P<pk>[0-9]+)$', FuncionarioDetail.as_view(), name='personal_funcionario_detail'),
)
