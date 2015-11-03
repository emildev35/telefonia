from django.contrib import admin
from .models import Cargo, Funcionario, Area


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass
