# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuerpo', models.TextField(null=True)),
                ('tipo', models.CharField(max_length=15, null=True, blank=True)),
                ('visto', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remitente', models.EmailField(max_length=254)),
                ('destinatario', models.EmailField(max_length=254)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(default=b'N', max_length=2, choices=[(b'N', b'NO ENVIADO'), (b'E', b'ENVIADO')])),
                ('alerta', models.ForeignKey(related_name='mensaje', blank=True, to='Notificaciones.Alerta', null=True)),
            ],
        ),
    ]
