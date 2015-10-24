from django.contrib import admin
from .models import Usuario, Nivel, Cargo, Despacho, Direccion, Unidad, Piso
from .models import CodigoProyecto, Menu


@admin.register(CodigoProyecto)
class CodigoProyectoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_username', 'activo')
    search_fields = ('id',)

    def usuario_username(self, instance):
        return instance.usuario.username


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ('cargo', 'oficina')


class UsuarioInline(admin.TabularInline):
    model = Usuario


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    pass


@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    pass


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    inlines = [UsuarioInline, ]


@admin.register(Piso)
class PisoAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
