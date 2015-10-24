import datetime
from django_ajax.decorators import ajax
from apps.utils.db import procedure, single_procedure, complex_procedure


@ajax
def timecall_usuario(request):
    tipo = request.GET['tipo']
    tiempo = request.GET['lapso']
    limite = request.GET['limit']
    data = procedure('timecall_usuario', int(tipo), int(tiempo), int(limite))
    return data


@ajax
def usuario_column(request):
    tipo = request.GET['tipo']
    tiempo = request.GET['lapso']
    limite = request.GET['limit']
    data = single_procedure(
        'char_column_usuario',
        int(tipo),
        int(tiempo),
        int(limite)
    )
    return data


@ajax
def oficina_column(request):
    tipo = request.GET['tipo']
    tiempo = request.GET['lapso']
    limite = request.GET['limit']
    data = single_procedure(
        'char_column_oficina',
        int(tipo),
        int(tiempo),
        int(limite)
    )
    return data


@ajax
def full_bar_usuario(request):
    data = complex_procedure(
        ['usuario', 'entrantes', 'salientes', 'operador'],
        'bar_complete_usuario',
        '1999-01-01',
        str(datetime.date.today())
    )
    return data


@ajax
def full_bar_oficina(request):
    data = single_procedure(
        'bar_complete_oficina',
        '1999-01-01',
        str(datetime.date.today())
    )
    return data
