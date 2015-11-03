from django.db import models


class Menu(models.Model):
    descripcion = models.CharField(max_length=50, null=False)
    color = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    padre = models.ForeignKey('Menu', related_name='hijos', null=True, blank=True)
