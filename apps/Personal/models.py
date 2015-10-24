from django.db import models


class Cargo(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now=True)
    fechaModificacion = models.DateTimeField()


class Area(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(auto_now=True)
    fechaModificacion = models.DateTimeField()


class Funcionario(models.Model):
    apaterno = models.CharField(max_length=50)
    amaterno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fechaNacimiento = models.DateTimeField()
