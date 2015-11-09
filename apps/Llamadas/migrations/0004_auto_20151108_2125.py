# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Llamadas', '0003_auto_20151108_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdr',
            name='dst',
            field=models.ForeignKey(related_name='llamadas_res_pbx', db_column=b'dst', to='Accounts.Extension'),
        ),
        migrations.AlterField(
            model_name='cdr',
            name='src',
            field=models.ForeignKey(related_name='llamadas_pbx', db_column=b'src', to='Accounts.Extension'),
        ),
    ]
