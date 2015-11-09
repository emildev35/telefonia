from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.Accounts.views.home', name='accounts_home'),
)

urlpatterns += patterns(
    '',
    url(r'^generarCode$', 'apps.Accounts.ajaxs.generarCodigo', name='accounts_generateCode'),
)
