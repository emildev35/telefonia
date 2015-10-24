from django.conf.urls import patterns, url
from .views import UsuariosView, UsuarioDetail


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.Accounts.views.home', name='accounts_home'),
    url(r'^login$', 'apps.Accounts.views.loginview', name='accounts_login'),
    url(r'^logout$', 'apps.Accounts.views.logoutview', name='accounts_logout'),

)

# Rutas para los Usuarios

urlpatterns += patterns(
    '',
    url(r'^usuario/list$', UsuariosView.as_view(), name='accounts_list'),
    url(r'^usuario/(?P<is_usuario>[0-9]{1,5})$', UsuarioDetail.as_view(), name='accounts_detaill'),
)

# Rutas Ajaxs

urlpatterns += patterns(
    '',
    url(r'^generarCode$', 'apps.Accounts.ajaxs.generarCodigo', name='accounts_generateCode'),
)
