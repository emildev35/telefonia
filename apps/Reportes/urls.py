from django.conf.urls import patterns, url
from .views import pdfUsuario, pdfTopLlamadas


urlpatterns = patterns(
    '',
    url(r'^tarifas', 'apps.Reportes.ajaxs.get_tarifas', name='jqxgrid_tarifa'),
    url(r'^horarios', 'apps.Reportes.ajaxs.get_horarios', name='jqxgrid_horarios'),
    url(r'^usuario_report', 'apps.Reportes.ajaxs.reporte_usuario', name='usuario_report'),
    url(r'^oficina_report', 'apps.Reportes.ajaxs.reporte_oficina', name='oficina_report'),
    url(r'^user_pdf_report', pdfUsuario, name='user_pdf_report'),
    url(r'^top_pdf_report', pdfTopLlamadas, name='top_pdf_report'),
)
