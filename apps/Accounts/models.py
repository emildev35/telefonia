from django.db import models
from apps.Personal.models import Funcionario


class Extension(models.Model):
    id = models.CharField(max_length=6, unique=True, primary_key=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, related_name='extensiones', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s - %s' % (self.id, self.funcionario.username)

    def save(self, *args, **kwargs):
        Extension.objects.filter(funcionario=self.funcionario).update(activo=False)
        self.activo = True
        super(Extension, self).save(*args, **kwargs)


class CodigoUsuario(models.Model):
    id = models.CharField(max_length=6, unique=True, primary_key=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, related_name='codigos', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s - %s' % (self.id, self.funcionario.username)

    def save(self, *args, **kwargs):
        CodigoUsuario.objects.filter(funcionario=self.funcionario).update(activo=False)
        self.activo = True
        super(CodigoUsuario, self).save(*args, **kwargs)
