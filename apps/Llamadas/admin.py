from django.contrib import admin
from .models import Llamada, Horario
from .models import Region, Tarifa


@admin.register(Llamada)
class LlamadaAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'hora',
        'numeroInterno',
        'codigoProyecto',
        'tipoLlamada',
        'duracion',
        'numero',
        'style_horario',
        'costo'
    )
    list_filter = (
        'fecha',
        'tipoLlamada'
    )
    search_fields = [
        'numeroInterno',
        'codigoProyecto__id',
        'numero'
    ]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'zona', 'precio', 'activo')
