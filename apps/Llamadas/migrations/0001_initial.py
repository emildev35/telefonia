# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
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
                ('horaIngreso', models.TimeField()),
                ('horaIngresoTarde', models.TimeField()),
                ('tiempoJornada', models.DurationField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroInterno', models.IntegerField()),
                ('numero', models.CharField(max_length=15)),
                ('hora', models.TimeField()),
                ('fecha', models.DateField()),
                ('duracion', models.DurationField()),
                ('costo', models.DecimalField(max_digits=5, decimal_places=2)),
                ('tiempoEspera', models.DurationField(null=True, blank=True)),
                ('tipoLlamada', models.CharField(max_length=1, choices=[(b'I', b'ENTRANTE'), (b'O', b'SALIENTE'), (b'E', b'OPERADOR')])),
                ('codigoProyecto', models.ForeignKey(related_name='llamadas', to='Accounts.CodigoProyecto')),
                ('horario', models.ForeignKey(related_name='llamadas', to='Llamadas.Horario')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('departamento', models.CharField(max_length=140)),
                ('zona', models.CharField(max_length=150)),
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
                ('fechaCreacion', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='llamada',
            name='region',
            field=models.ForeignKey(related_name='llamadas', to='Llamadas.Region'),
        ),
        migrations.AddField(
            model_name='descripcionllamada',
            name='llamada',
            field=models.OneToOneField(related_name='descripcon', to='Llamadas.Llamada'),
        ),
        migrations.AlterUniqueTogether(
            name='llamada',
            unique_together=set([('fecha', 'hora', 'codigoProyecto', 'numeroInterno')]),
        ),
    ]
