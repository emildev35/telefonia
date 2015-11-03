from django.db import models


class Extension(models.Model):
    numero = models.CharField(max_length=6, unique=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)


class CodigoUsuario(models.Model):
    numero = models.CharField(max_length=6, unique=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)
