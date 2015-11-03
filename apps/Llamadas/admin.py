from django.contrib import admin
from .models import Llamada, Horario
from .models import Tarifa


@admin.register(Llamada)
class LlamadaAdmin(admin.ModelAdmin):
    pass


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    pass
