# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import infos_systems.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web_slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webslide',
            name='image',
            field=models.ImageField(default='default/No_Avatar_1.png', help_text='Subir Imagen', upload_to='images_web_slides', validators=[infos_systems.validators.valid_extension], verbose_name='Imagen'),
        ),
    ]
