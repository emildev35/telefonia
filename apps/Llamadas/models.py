import datetime as dt
from django.db import models
from apps.Accounts.models import CodigoProyecto
from .tasks import registarLlamada


TYPE = (('F', 'FIJO'), ('M', 'MOVIL'))
ZONE_TYPE = (('L', 'LOCAL'), ('N', 'NACIONAL'))


class Tarifa(models.Model):
    tipo = models.CharField(max_length=1, choices=TYPE)
    zona = models.CharField(max_length=1, choices=ZONE_TYPE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    activo = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        Tarifa.objects.filter(tipo=self.tipo).filter(zona=self.zona).update(activo=False)
        super(Tarifa, self).save(*args, **kwargs)

    def __unicode__(self):
        data = '%s - %s - %s' % (self.tipo, self.zona, self.precio)
        return data


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    departamento = models.CharField(max_length=140)
    zona = models.CharField(max_length=150)

    def __unicode__(self):
        data = '%s-%s' % \
            (
                self.departamento,
                self.zona,
            )
        return data


CALL_TYPE = (('I', 'ENTRANTE'), ('O', 'SALIENTE'), ('E', 'OPERADOR'))


class Llamada(models.Model):
    numeroInterno = models.IntegerField()
    region = models.ForeignKey('Region', related_name='llamadas')
    numero = models.CharField(max_length=15)
    hora = models.TimeField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    duracion = models.DurationField()
    codigoProyecto = models.ForeignKey(
        CodigoProyecto,
        related_name='llamadas'
    )
    costo = models.DecimalField(max_digits=5, decimal_places=2)
    tiempoEspera = models.DurationField(blank=True, null=True)
    tipoLlamada = models.CharField(max_length=1, choices=CALL_TYPE)
    horario = models.ForeignKey('Horario', related_name='llamadas')

    def style_horario(self):
        color = '#FF0000'
        msg = 'Fuera de Horario'
        hora_ing_am = self.horario.horaIngreso
        hora_sal_am = (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.horario.horaIngreso
        ) + self.horario.tiempoJornada).time()
        hora_ing_pm = self.horario.horaIngresoTarde
        hora_sal_pm = (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.horario.horaIngresoTarde
        ) + self.horario.tiempoJornada).time()
        if self.hora > hora_ing_am and self.hora < hora_sal_am:
            color = '#80FF00'
            msg = 'En Horario'
        if self.hora > hora_ing_pm and self.hora < hora_sal_pm:
            color = '#80FF00'
            msg = 'En Horario'
        return '<div style="color: %s;">%s</div>' % (
            color,
            msg
        )
    style_horario.allow_tags = True
    style_horario.short_description = 'Horario'

    def __unicode__(self):
        data = '%s-%s-%s-%s' %  \
            (
                self.fecha,
                self.hora,
                self.duracion,
                self.codigoProyecto.usuario.username
            )
        return data

    def save(self, *args, **kwargs):
        super(Llamada, self).save(*args, **kwargs)
        DescripcionLlamada.objects.create(
            llamada=self,
        )

    class Meta:
        unique_together = ('fecha', 'hora', 'codigoProyecto', 'numeroInterno')

DESCRIPTION_TYPE = (('L', 'LABORAL'), ('P', 'PERSONAL'))


class DescripcionLlamada(models.Model):
    nombre = models.CharField(
        max_length=1,
        default='P',
        choices=DESCRIPTION_TYPE
    )
    motivo = models.TextField(default='NO IDENTICADO')
    registrado = models.BooleanField(default=False)
    llamada = models.OneToOneField('Llamada', related_name='descripcon')

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        registarLlamada.apply_async(args=(self,), countdown = 60 * 10)
        super(DescripcionLlamada, self).save(*args, **kwargs)


class Horario(models.Model):
    horaIngreso = models.TimeField()
    horaIngresoTarde = models.TimeField()
    tiempoJornada = models.DurationField()
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        data = '%s-%s' % (
            self.horaIngreso.strftime('%H:%M:%S'),
            self.horaIngresoTarde.strftime('%H:%M:%S')
        )
        return data

    def save(self, *args, **kwargs):
        Horario.objects.all().update(activo=False)
        super(Horario, self).save(*args, **kwargs)

    def horaSalida(self):
        return (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.horaIngreso
        ) + self.tiempoJornada).time()

    def horaSalidaTarde(self):
        return (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.horaIngresoTarde
        ) + self.tiempoJornada).time()
