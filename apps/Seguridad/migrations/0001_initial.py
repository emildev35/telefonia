# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=150, null=True, blank=True)),
                ('funcionario', models.ManyToManyField(related_name='menus', to=settings.AUTH_USER_MODEL, blank=True)),
                ('padre', models.ForeignKey(related_name='hijos', blank=True, to='Seguridad.Menu', null=True)),
            ],
        ),
    ]
