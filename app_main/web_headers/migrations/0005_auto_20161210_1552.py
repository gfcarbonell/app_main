# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_headers', '0004_auto_20161210_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webheader',
            name='is_video_source',
        ),
        migrations.AddField(
            model_name='webheader',
            name='video_source',
            field=models.BooleanField(choices=[(True, 'U.R.L.'), (False, 'File')], default=True, verbose_name='Fuente de vídeo'),
        ),
    ]
