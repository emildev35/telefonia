from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^login$', 'apps.Seguridad.views.loginview', name='seguridad_login'),
    url(r'^logout$', 'apps.Seguridad.views.logoutview', name='seguridad_logout'),
)
