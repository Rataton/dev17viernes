# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, verbose_name='Nmobre')),
                ('description', models.CharField(max_length=300, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=120, null=True, verbose_name='Apellido', blank=True)),
                ('number', models.CharField(max_length=10, verbose_name='Numero')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Celular', blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='person',
            field=models.ForeignKey(to='contactos.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
