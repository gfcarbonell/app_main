# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-13 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='photograph',
            field=models.ImageField(blank=True, default='default/No-Avatar-1.png', null=True, upload_to='image/provinces', verbose_name='Fotografía'),
        ),
    ]