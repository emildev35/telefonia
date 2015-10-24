from django.db import models
from django.contrib.auth.models import AbstractUser


class Nivel(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    fechaCreacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Niveles'


class Cargo(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Unidad(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.ForeignKey('Direccion', related_name='unidades')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Unidades'


class Despacho(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Direccion(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    despacho = models.ForeignKey('Despacho', related_name='direcciones')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Direcciones'


class Piso(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __unicode__(self):
        return self.nombre


class Usuario(AbstractUser):
    nivel = models.ForeignKey(
        'Nivel',
        related_name='usuarios',
        blank=True,
        null=True
    )
    default_name = models.CharField(max_length=150, blank=True, null=True)
    fechaNacimiento = models.DateTimeField(blank=True, null=True)
    ci = models.CharField(max_length=9, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    fechaModificacion = models.DateTimeField(
        auto_now=True
    )
    unidad = models.ForeignKey(
        'Unidad',
        related_name='usuarios',
        blank=True,
        null=True
    )
    despacho = models.ForeignKey(
        'Despacho',
        related_name='usuarios',
        blank=True,
        null=True
    )
    direccion = models.ForeignKey(
        'Direccion',
        related_name='usuarios',
        blank=True,
        null=True
    )
    cargo = models.CharField(max_length=150, blank=True, null=True)
    oficina = models.CharField(max_length=150, blank=True, null=True)
    idOficina = models.IntegerField(blank=True, null=True)
    fotografia = models.CharField(max_length=150, blank=True, null=True)


class CodigoProyecto(models.Model):
    id = models.IntegerField(primary_key=True)
    activo = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now=True)
    fechaInvalidacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey('Usuario', related_name='codigos')

    def __unicode__(self):
        return '%s %s' % (
            self.id,
            self.usuario.username
        )

    def save(self, *args, **kwargs):
        CodigoProyecto.objects.filter(usuario=self.usuario).update(activo=False)
        super(CodigoProyecto, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Codigos de Proyectos'


class Menu(models.Model):
    nombre = models.CharField(max_length=140)
    direccion = models.CharField(max_length=140)
    superusuario = models.BooleanField(default=False)
    icon = models.CharField(max_length=140, null=True, blank=True)
    color = models.CharField(max_length=140, null=True, blank=True)
    padre = models.ForeignKey(
        'Menu',
        related_name='hijos',
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.nombre
