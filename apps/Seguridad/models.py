from django.db import models
from apps.Personal.models import Funcionario


class Menu(models.Model):
    descripcion = models.CharField(max_length=50, null=False, unique=True)
    color = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    url = models.CharField(max_length=150, null=True, blank=True)
    padre = models.ForeignKey('Menu', related_name='hijos', null=True, blank=True)
    funcionario = models.ManyToManyField(Funcionario, related_name='menus', blank=True)

    def __unicode__(self):
        return self.descripcion
