import datetime as dt
from django.db import models
from apps.Accounts.models import CodigoUsuario, Extension
# from .tasks import registarLlamada


TYPE = (('F', 'FIJO'), ('M', 'MOVIL'))
ZONE_TYPE = (('L', 'LOCAL'), ('N', 'NACIONAL'))


class Tarifa(models.Model):
    tipo = models.CharField(max_length=1, choices=TYPE)
    zona = models.CharField(max_length=1, choices=ZONE_TYPE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        Tarifa.objects.filter(tipo=self.tipo).filter(zona=self.zona).update(activo=False)
        super(Tarifa, self).save(*args, **kwargs)

    def __unicode__(self):
        data = '%s - %s - %s' % (self.tipo, self.zona, self.precio)
        return data


class TipoLLamada(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion


class Llamada(models.Model):
    numero_interno = models.IntegerField()
    numero = models.ForeignKey('NumeroTelefonico', related_name='llamadas')
    hora = models.TimeField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    duracion = models.DurationField()
    codigo_usuario = models.ForeignKey(CodigoUsuario, related_name='llamadas')
    costo = models.DecimalField(max_digits=5, decimal_places=2)
    tiempo_espera = models.DurationField(blank=True, null=True)
    tipo_llamada = models.ForeignKey('TipoLLamada', related_name='llamadas')
    horario = models.ForeignKey('Horario', related_name='llamadas')

    def style_horario(self):
        color = '#FF0000'
        msg = 'Fuera de Horario'
        hora_ing_am = self.horario.hora_ingreso
        hora_sal_am = (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.horario.hora_ingreso
        ) + self.horario.tiempo_jornada).time()
        hora_ing_pm = self.horario.hora_ingreso_tarde
        hora_sal_pm = (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.horario.hora_ingreso_tarde
        ) + self.horario.tiempo_jornada).time()
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
                self.codigo_usuario.funcionario.username
            )
        return data

    def save(self, *args, **kwargs):
        super(Llamada, self).save(*args, **kwargs)
        DescripcionLlamada.objects.create(
            llamada=self,
        )

    class Meta:
        unique_together = ('fecha', 'hora', 'codigo_usuario', 'numero_interno', 'numero')

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
        # registarLlamada.apply_async(args=(self,), countdown = 60 * 10)
        super(DescripcionLlamada, self).save(*args, **kwargs)


class Horario(models.Model):
    hora_ingreso = models.TimeField()
    hora_ingreso_tarde = models.TimeField()
    tiempo_jornada = models.DurationField()
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        data = '%s-%s' % (
            self.hora_ingreso.strftime('%H:%M:%S'),
            self.hora_ingreso_tarde.strftime('%H:%M:%S')
        )
        return data

    def save(self, *args, **kwargs):
        Horario.objects.all().update(activo=False)
        super(Horario, self).save(*args, **kwargs)

    def horaSalida(self):
        return (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.hora_ingreso
        ) + self.tiempo_jornada).time()

    def horaSalidaTarde(self):
        return (dt.datetime.combine(
            dt.date(1, 1, 1,),
            self.hora_ingreso_tarde
        ) + self.tiempo_jornada).time()


class NumeroTelefonico(models.Model):
    numero = models.CharField(max_length=11, primary_key=True)
    departamento = models.CharField(max_length=50)
    zona = models.CharField(max_length=50, default='')
    area_servicio = models.CharField(max_length=50, default='')
    empresa = models.CharField(max_length=50, default='')
    servicio = models.CharField(max_length=30, default='')

    def __unicode__(self):
        return self.numero


class Cdr(models.Model):
    accid = models.AutoField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=45)
    src = models.ForeignKey(Extension, related_name='llamadas_pbx', db_column='src')
    dst = models.ForeignKey(Extension, related_name='llamadas_res_pbx', db_column='dst')
    dcontext = models.CharField(max_length=45)
    channel = models.CharField(max_length=45)
    dstchannel = models.CharField(max_length=45)
    lastapp = models.CharField(max_length=45)
    lastdata = models.CharField(max_length=45)
    duration = models.IntegerField(default=0)
    billsec = models.IntegerField(default=0)
    lastdata = models.CharField(max_length=45)
    duration = models.IntegerField(default=0)
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField(default=0)
    accountcode = models.CharField(max_length=45)
    uniqueid = models.CharField(max_length=45)
    userfield = models.CharField(max_length=45)

    class Meta:
        db_table = 'cdr'
