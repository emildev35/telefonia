from django.contrib import admin
from .models import CodigoUsuario, Extension


@admin.register(CodigoUsuario)
class CodigoUsuarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    pass
