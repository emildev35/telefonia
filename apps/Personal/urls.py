from django.conf.urls import patterns, url
from .views import CargoView, CargoList, CargoDetail
from .views import AreaView, AreaList, AreaDetail

urlpatterns = patterns(
    '',
    url(r'^cargo/create$', CargoView.as_view(), name='personal_cargo_create'),
    url(r'^cargo/$', CargoList.as_view(), name='personal_cargo_list'),
    url(r'^cargo/(?P<pk>[0-9]+)$', CargoDetail.as_view(), name='personal_cargo_detail'),
    url(r'^area/create$', AreaView.as_view(), name='personal_area_create'),
    url(r'^area/list$', AreaList.as_view(), name='personal_area_list'),
    url(r'^area/(?P<pk>[0-9]+)$', AreaDetail.as_view(), name='personal_area_detail'),
)
