# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=150)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CodigoProyecto',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
                ('fechaInvalidacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Codigos de Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=150)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=150)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('despacho', models.ForeignKey(related_name='direcciones', to='Accounts.Despacho')),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('direccion', models.CharField(max_length=140)),
                ('superusuario', models.BooleanField(default=False)),
                ('icon', models.CharField(max_length=140, null=True, blank=True)),
                ('color', models.CharField(max_length=140, null=True, blank=True)),
                ('padre', models.ForeignKey(related_name='hijos', blank=True, to='Accounts.Menu', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=150)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Niveles',
            },
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=150)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('direccion', models.ForeignKey(related_name='unidades', to='Accounts.Direccion')),
            ],
            options={
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('default_name', models.CharField(max_length=150, null=True, blank=True)),
                ('fechaNacimiento', models.DateTimeField(null=True, blank=True)),
                ('ci', models.CharField(max_length=9, null=True, blank=True)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('fechaModificacion', models.DateTimeField(auto_now=True)),
                ('cargo', models.CharField(max_length=150, null=True, blank=True)),
                ('oficina', models.CharField(max_length=150, null=True, blank=True)),
                ('idOficina', models.IntegerField(null=True, blank=True)),
                ('fotografia', models.CharField(max_length=150, null=True, blank=True)),
                ('despacho', models.ForeignKey(related_name='usuarios', blank=True, to='Accounts.Despacho', null=True)),
                ('direccion', models.ForeignKey(related_name='usuarios', blank=True, to='Accounts.Direccion', null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('nivel', models.ForeignKey(related_name='usuarios', blank=True, to='Accounts.Nivel', null=True)),
                ('unidad', models.ForeignKey(related_name='usuarios', blank=True, to='Accounts.Unidad', null=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='codigoproyecto',
            name='usuario',
            field=models.ForeignKey(related_name='codigos', to=settings.AUTH_USER_MODEL),
        ),
    ]
