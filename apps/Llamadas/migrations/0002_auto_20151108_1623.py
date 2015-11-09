# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Llamadas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='numero',
            field=models.ForeignKey(related_name='llamadas', to='Llamadas.NumeroTelefonico'),
        ),
    ]
