# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-13 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users_profiles', '0004_auto_20170213_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuserprofile',
            name='photograph',
            field=models.ImageField(blank=True, default='default/No-Avatar-1.png', null=True, upload_to='photographs', verbose_name='Fotografía'),
        ),
    ]