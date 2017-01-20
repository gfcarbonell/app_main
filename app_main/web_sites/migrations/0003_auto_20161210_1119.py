# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 16:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_sites', '0002_auto_20161210_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='description',
            field=models.TextField(blank=True, help_text='Escribir una descripción del sitio web (opcional) .', null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='website',
            name='is_active',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'Not')], default=True, verbose_name='¿Activo?'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(db_index=True, max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='U.R.L.'),
        ),
    ]