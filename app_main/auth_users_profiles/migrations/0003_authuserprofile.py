# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-13 15:30
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blood_groups', '0001_initial'),
        ('identification_documents', '0001_initial'),
        ('civil_states', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_users_profiles', '0002_auto_20170213_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserProfile',
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
                ('type_person', models.BooleanField(choices=[(True, 'Natural|Natural'), (False, 'Legal|Jurídica')], default=True)),
                ('name', models.CharField(db_index=True, max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Nombre')),
                ('last_name', models.CharField(db_index=True, max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Apellido Paterno')),
                ('mother_last_name', models.CharField(db_index=True, max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Apellido Materno')),
                ('number_identification_document', models.PositiveSmallIntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Número Documento de Identificación')),
                ('birth_day', models.DateField(default='01-01-1980', verbose_name='Fecha de Nacimiento')),
                ('gender', models.BooleanField(choices=[(True, 'Male|Masculino'), (False, 'Female|Femenino')], default=True, verbose_name='Género')),
                ('photograph', models.ImageField(blank=True, default='default/No_Avatar_1.png', help_text='Subir fotografia (Opcional).', null=True, upload_to='fotografias', verbose_name='Fotografía')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Correo electrónico')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Télefono')),
                ('cell_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='Observación')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_user_authuserprofiles_related', to=settings.AUTH_USER_MODEL)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_users_profiles_authuserprofile_related', to='blood_groups.BloodGroup', verbose_name='Grupo Sanguíneo')),
                ('civil_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_users_profiles_authuserprofile_related', to='civil_states.CivilState', verbose_name='Estado Civil')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('identification_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_users_profiles_authuserprofile_related', to='identification_documents.IdentificationDocument', verbose_name='Documento de Identificación')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_users_profiles_authuserprofile_related', to=settings.AUTH_USER_MODEL, verbose_name='Última actualización por')),
            ],
            options={
                'verbose_name_plural': 'Auth Users Profiles',
                'verbose_name': 'Auth User Profile',
                'db_table': 'auth_user_profile',
                'ordering': ('auth_user',),
            },
        ),
    ]
