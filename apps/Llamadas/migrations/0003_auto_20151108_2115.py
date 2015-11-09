# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Llamadas', '0002_auto_20151108_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdr',
            name='dst',
            field=models.ForeignKey(related_name='llamadas_res_pbx', to='Accounts.Extension'),
        ),
        migrations.AlterField(
            model_name='cdr',
            name='src',
            field=models.ForeignKey(related_name='llamadas_pbx', to='Accounts.Extension'),
        ),
    ]
