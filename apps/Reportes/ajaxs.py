import datetime as dt
from apps.utils.db import wh_procedure, procedure
from django_ajax.response import JSONResponse
from django_ajax.decorators import ajax


def get_tarifas(request):
    tarifas = procedure('grid_tarifas')
    return JSONResponse(tarifas)


def get_horarios(request):
    horarios = procedure('grid_horario')
    return JSONResponse(horarios)


@ajax
def reporte_usuario(request):
    usuario = request.GET['usuario']
    fecha_inicio = request.GET['fecha_inicio']
    fecha_final = request.GET['fecha_final']

    if fecha_inicio == '':
        fecha_inicio = '1999-01-01'
    else:
        fecha_inicio = [x for x in fecha_inicio.split('/')]
        fecha_inicio = fecha_inicio[2] + '-' + fecha_inicio[0] + '-' + fecha_inicio[1]

    if fecha_final == '':
        fecha_final = str(dt.date.today())
    else:
        fecha_final = [x for x in fecha_final.split('/')]
        fecha_final = fecha_final[2] + '-' + fecha_final[0] + '-' + fecha_final[1]

    resultado = wh_procedure(
        'card_complete_usuario',
        ['usuario', usuario],
        str(fecha_inicio),
        str(fecha_final))
    return resultado


@ajax
def reporte_oficina(request):
    oficina = request.GET['oficina']
    fecha_inicio = request.GET['fecha_inicio']
    fecha_final = request.GET['fecha_final']

    if fecha_inicio == '':
        fecha_inicio = '1999-01-01'
    else:
        fecha_inicio = [x for x in fecha_inicio.split('/')]
        fecha_inicio = fecha_inicio[2] + '-' + fecha_inicio[0] + '-' + fecha_inicio[1]

    if fecha_final == '':
        fecha_final = str(dt.date.today())
    else:
        fecha_final = [x for x in fecha_final.split('/')]
        fecha_final = fecha_final[2] + '-' + fecha_final[0] + '-' + fecha_final[1]

    resultado = wh_procedure(
        'card_complete_oficina',
        ['oficina', oficina],
        str(fecha_inicio),
        str(fecha_final))
    return resultado
