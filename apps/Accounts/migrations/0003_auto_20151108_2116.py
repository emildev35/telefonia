# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20151107_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='id',
            field=models.CharField(max_length=6, unique=True, serialize=False, primary_key=True),
        ),
    ]
