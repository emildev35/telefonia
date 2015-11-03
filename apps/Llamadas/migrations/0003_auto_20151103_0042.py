# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Llamadas', '0002_auto_20151103_0039'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cdr',
            table='cdr',
        ),
    ]
