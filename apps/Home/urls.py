from django.conf.urls import patterns, url
from .views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home_home'),
)
# Ajax patterns
urlpatterns += patterns(
    '',
    url(r'^timecall_usuario$', 'apps.Home.ajaxs.timecall_usuario', name='timecall_usuario'),
    url(r'^call_usuario$', 'apps.Home.ajaxs.usuario_column', name='char_column_usuario'),
    url(r'^call_oficina$', 'apps.Home.ajaxs.oficina_column', name='char_column_oficina'),
    url(r'^full_bar_usuario$', 'apps.Home.ajaxs.full_bar_usuario', name='full_bar_usuario'),
    url(r'^full_bar_oficina$', 'apps.Home.ajaxs.full_bar_oficina', name='full_bar_oficina'),
)
