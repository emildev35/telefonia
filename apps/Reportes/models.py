from django.db import models
from apps.Personal.models import Funcionario


class ConfiguracionCuenta(models.Model):
    montoDisponible = models.DecimalField(max_digits=5, decimal_places=2)
    activo = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now=True)
    fechaBaja = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.montoDisponible)

    def save(self, *args, **kwargs):
        ConfiguracionCuenta.objects.filter(activo=True).update(activo=False)
        super(ConfiguracionCuenta, self).save(*args, **kwargs)


class Cuenta(models.Model):
    funcionario = models.ForeignKey(Funcionario, related_name='cuentas')
    mes = models.IntegerField()
    gestion = models.IntegerField()
    montoDisponible = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    estado = models.BooleanField(default=True)
    monto = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    configuracion = models.ForeignKey('ConfiguracionCuenta', related_name='cuentas')

    def save(self, *args, **kwargs):
        self.objects.filter(estado=True).update(estado=False)
        super(Cuenta, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.usuario.username


class UploadCvs(models.Model):
    cvsFile = models.FileField(upload_to='cvs')
    fechaCreacion = models.DateTimeField(auto_now=True)
    funcionario = models.ForeignKey(Funcionario, related_name='uploads')

    def __unicode__(self):
        return '%s - %s' % \
            (
                self.usuario.username,
                self.fechaCreacion
            )
