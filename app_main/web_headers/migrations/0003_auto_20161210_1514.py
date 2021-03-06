# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 20:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web_headers', '0002_auto_20161210_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webheader',
            name='url',
        ),
        migrations.RemoveField(
            model_name='webheader',
            name='video',
        ),
        migrations.AddField(
            model_name='webheader',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos_web_headers', verbose_name='Vídeo (Archivo)'),
        ),
        migrations.AddField(
            model_name='webheader',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(blank=True, db_index=True, max_length=255, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='U.R.L. (Vídeo)'),
        ),
    ]
