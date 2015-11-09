from django.db import models
from django.contrib.auth.models import AbstractUser


class Cargo(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now=True)
    fechaModificacion = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.descripcion


class Area(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now=True)
    fechaModificacion = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.descripcion


class Funcionario(AbstractUser):
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    ci = models.CharField(max_length=10, blank=True, null=True)
    ip = models.GenericIPAddressField()
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    fotografia = models.ImageField(null=True, blank=True)
    area = models.ForeignKey('Area', related_name='funcionarios')
    cargo = models.ForeignKey('Cargo', related_name='funcionarios')
