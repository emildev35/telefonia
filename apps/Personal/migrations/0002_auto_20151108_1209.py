# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='amaterno',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='apaterno',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='nombres',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='oficina',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='area',
            field=models.ForeignKey(related_name='funcionarios', to='Personal.Area'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(related_name='funcionarios', to='Personal.Cargo'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
