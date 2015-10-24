from django.contrib import admin
from .models import Alerta, Mensaje


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    pass


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    pass

