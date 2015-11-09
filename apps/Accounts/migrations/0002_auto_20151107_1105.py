# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='funcionario',
            field=models.ForeignKey(related_name='extensiones', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='codigousuario',
            name='funcionario',
            field=models.ForeignKey(related_name='codigos', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
