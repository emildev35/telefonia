from base64 import b64encode
from easy_pdf.rendering import render_to_pdf_response
from django.utils.timezone import now as tznow
from django.contrib.auth.decorators import permission_required
from apps.utils.db import full_complex_procedure
from telefonia.settings.production import STATICFILES_DIRS
from apps.Personal.models import Funcionario
from apps.Llamadas.models import Llamada
import datetime


@permission_required('reportes.add_cuenta')
def pdfUsuario(request):
    imagen_path = STATICFILES_DIRS[0] + '/logos/logomopsv.png'
    imagen_bol_path = STATICFILES_DIRS[0] + '/logos/logobolivia.png'
    data = Funcionario.objects.all()
    with open(imagen_path, 'rb') as img:
        imagen_path = b64encode(img.read())
    with open(imagen_bol_path, 'rb') as img:
        imagen_bol_path = b64encode(img.read())
    return render_to_pdf_response(
        request,
        'reportes/user.html',
        {
            'today': tznow(),
            'imagen': imagen_path,
            'imagen_bol': imagen_bol_path,
            'usuarios': data,
        }
    )


@permission_required('reportes.add_cuenta')
def pdfTopLlamadas(request):
    imagen_path = STATICFILES_DIRS[0] + '/logos/logomopsv.png'
    imagen_bol_path = STATICFILES_DIRS[0] + '/logos/logobolivia.png'
    top_usuario = full_complex_procedure(
        ['usuario', 'entrantes', 'salientes', 'operador'],
        'bar_complete_usuario',
        '1999-01-01',
        str(datetime.date.today())
    )
    top_oficina = full_complex_procedure(
        ['oficina', 'entrantes', 'salientes', 'operador'],
        'bar_complete_oficina',
        '1999-01-01',
        str(datetime.date.today())
    )

    print top_usuario
    print top_oficina
    c_llamadas = Llamada.objects.count()
    c_llamadas_entrantes = Llamada.objects.filter(tipo_llamada_id=1).count()
    c_llamadas_salientes = Llamada.objects.filter(tipo_llamada_id=2).count()
    c_llamadas_operador = Llamada.objects.filter(tipo_llamada_id=3).count()
    with open(imagen_path, 'rb') as img:
        imagen_path = b64encode(img.read())
    with open(imagen_bol_path, 'rb') as img:
        imagen_bol_path = b64encode(img.read())
    return render_to_pdf_response(
        request,
        'reportes/topllamadas.html',
        {
            'today': tznow(),
            'imagen': imagen_path,
            'imagen_bol': imagen_bol_path,
            'c_llamadas': c_llamadas,
            'c_llamadas_s': c_llamadas_salientes,
            'c_llamadas_e': c_llamadas_entrantes,
            'c_llamadas_o': c_llamadas_operador,
            'top_usuarios': top_usuario,
            'top_oficinas': top_oficina
        }
    )


@permission_required('reportes.add_cuenta')
def pdfGeneral(request):
    imagen_path = STATICFILES_DIRS[0] + '/logos/logomopsv.png'
    imagen_bol_path = STATICFILES_DIRS[0] + '/logos/logobolivia.png'
    with open(imagen_path, 'rb') as img:
        imagen_path = b64encode(img.read())
    with open(imagen_bol_path, 'rb') as img:
        imagen_bol_path = b64encode(img.read())
    return render_to_pdf_response(
        request,
        'reportes/llamadas.html',
        {
            'today': tznow(),
            'imagen': imagen_path,
            'imagen_bol': imagen_bol_path
        }
    )
