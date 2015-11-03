from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.Home.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('apps.Accounts.urls')),
    url(r'^home/', include('apps.Home.urls')),
    url(r'^llamadas/', include('apps.Llamadas.urls')),
    url(r'^reportes/', include('apps.Reportes.urls')),
    url(r'^personal/', include('apps.Personal.urls')),
    url(r'^notificaciones/', include('apps.Notificaciones.urls')),
)

if not settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

handler404 = 'apps.Home.views.handler404'
