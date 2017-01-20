# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_headers', '0003_auto_20161210_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='webheader',
            name='is_video_source',
            field=models.BooleanField(choices=[(True, 'U.R.L.'), (False, 'File')], default=True, verbose_name='¿Es la fuente de video?'),
        ),
        migrations.AlterField(
            model_name='webheader',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos_web_headers', verbose_name='Archivo (Vídeo)'),
        ),
    ]
