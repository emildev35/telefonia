# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cdr',
            fields=[
                ('accid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('calldate', models.DateTimeField()),
                ('clid', models.CharField(max_length=45)),
                ('src', models.CharField(max_length=45)),
                ('dst', models.CharField(max_length=45)),
                ('dcontext', models.CharField(max_length=45)),
                ('channel', models.CharField(max_length=45)),
                ('dstchannel', models.CharField(max_length=45)),
                ('lastapp', models.CharField(max_length=45)),
                ('billsec', models.IntegerField(default=0)),
                ('lastdata', models.CharField(max_length=45)),
                ('duration', models.IntegerField(default=0)),
                ('disposition', models.CharField(max_length=45)),
                ('amaflags', models.IntegerField(default=0)),
                ('accountcode', models.CharField(max_length=45)),
                ('uniqueid', models.CharField(max_length=45)),
                ('userfield', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionLlamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'P', max_length=1, choices=[(b'L', b'LABORAL'), (b'P', b'PERSONAL')])),
                ('motivo', models.TextField(default=b'NO IDENTICADO')),
                ('registrado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_ingreso', models.TimeField()),
                ('hora_ingreso_tarde', models.TimeField()),
                ('tiempo_jornada', models.DurationField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_interno', models.IntegerField()),
                ('numero', models.CharField(max_length=15)),
                ('hora', models.TimeField()),
                ('fecha', models.DateField()),
                ('duracion', models.DurationField()),
                ('costo', models.DecimalField(max_digits=5, decimal_places=2)),
                ('tiempo_espera', models.DurationField(null=True, blank=True)),
                ('codigo_usuario', models.ForeignKey(related_name='llamadas', to='Accounts.CodigoUsuario')),
                ('horario', models.ForeignKey(related_name='llamadas', to='Llamadas.Horario')),
            ],
        ),
        migrations.CreateModel(
            name='NumeroTelefonico',
            fields=[
                ('codigo', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('region', models.CharField(max_length=50)),
                ('servicio', models.CharField(max_length=20)),
                ('empresa', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=1, choices=[(b'F', b'FIJO'), (b'M', b'MOVIL')])),
                ('zona', models.CharField(max_length=1, choices=[(b'L', b'LOCAL'), (b'N', b'NACIONAL')])),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLLamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='llamada',
            name='tipo_llamada',
            field=models.ForeignKey(related_name='llamadas', to='Llamadas.TipoLLamada'),
        ),
        migrations.AddField(
            model_name='descripcionllamada',
            name='llamada',
            field=models.OneToOneField(related_name='descripcon', to='Llamadas.Llamada'),
        ),
        migrations.AlterUniqueTogether(
            name='llamada',
            unique_together=set([('fecha', 'hora', 'codigo_usuario', 'numero_interno')]),
        ),
    ]
