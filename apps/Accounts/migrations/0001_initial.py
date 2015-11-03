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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=6)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('fecha_baja', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=6)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('fecha_baja', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
