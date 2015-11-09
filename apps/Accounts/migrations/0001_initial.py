# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoUsuario',
            fields=[
                ('id', models.CharField(max_length=6, unique=True, serialize=False, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('fecha_baja', models.DateTimeField(null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('fecha_baja', models.DateTimeField(null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
