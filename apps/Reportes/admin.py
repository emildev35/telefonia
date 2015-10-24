from django.contrib import admin
from .models import ConfiguracionCuenta, Cuenta


@admin.register(ConfiguracionCuenta)
class ConfiguracionCuentaAdmin(admin.ModelAdmin):
    pass


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    pass
