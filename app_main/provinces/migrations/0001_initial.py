# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-13 17:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')),
                ('host_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Nombre host')),
                ('ip_address', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address, django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Dirección I.P.')),
                ('mac_address', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Dirección M.A.C.')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha última actualización')),
                ('last_update_host_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Última actualizacion de nombre host ')),
                ('last_update_ip_address', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address, django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Última actualizacion de Dirección I.P.')),
                ('last_update_mac_address', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Última actualizacion de Dirección M.A.C.')),
                ('name', models.CharField(db_index=True, max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Nombre')),
                ('photograph', models.ImageField(blank=True, default='default/No-Avatar-1.png', null=True, upload_to='provinces', verbose_name='Fotografía')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Department', verbose_name='Departamento')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces_province_related', to=settings.AUTH_USER_MODEL, verbose_name='Última actualización por')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'provinces',
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
    ]
