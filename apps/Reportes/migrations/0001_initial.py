# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionCuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('montoDisponible', models.DecimalField(max_digits=5, decimal_places=2)),
                ('activo', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
                ('fechaBaja', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField()),
                ('gestion', models.IntegerField()),
                ('montoDisponible', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('monto', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('configuracion', models.ForeignKey(related_name='cuentas', to='Reportes.ConfiguracionCuenta')),
                ('usuario', models.ForeignKey(related_name='cuentas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadCvs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cvsFile', models.FileField(upload_to=b'cvs')),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(related_name='uploads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
