from django.db import models
from apps.Accounts.models import Usuario
from apps.Llamadas.models import Llamada


STATES_MAIL = (('N', 'NO ENVIADO'), ('E', 'ENVIADO'))


class Alerta(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='alertas')
    cuerpo = models.TextField(null=True)
    tipo = models.CharField(max_length=15, null=True, blank=True)
    visto = models.BooleanField(default=False)


class Mensaje(models.Model):
    remitente = models.EmailField()
    destinatario = models.EmailField()
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=2, choices=STATES_MAIL, default='N')
    alerta = models.ForeignKey(
        'Alerta',
        related_name='mensaje',
        blank=True,
        null=True
    )
