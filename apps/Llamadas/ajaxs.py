from django_ajax.response import JSONResponse
from apps.utils.grid import jqgrid_generic


def jqgrid_llamadas(request, *kwargs):
    grid = jqgrid_generic(request, 'jgrid_llamadas', [
        'id',
        'usuario',
        'hora',
        'fecha',
        'duracion',
        'numero',
        'interno',
        'costo',
        'tipo_llamada',
        'codigo_proyecto',
        'horario'
        ])

    return JSONResponse(grid)
