from django.contrib import admin
from .models import Llamada, Horario
from .models import Tarifa, TipoLLamada


@admin.register(Llamada)
class LlamadaAdmin(admin.ModelAdmin):
    pass


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoLLamada)
class TipoLLamadaAdmin(admin.ModelAdmin):
    pass
