# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket
import uuid
import os
from django.conf import settings

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator


class UserManager(BaseUserManager):

	def _create_user(self, username, email, password, **extra_fields):
		if not username:
			raise ValueError('the given username must be set')
		email = self.normalize_email(email)
		user = self.model(username = username, email = email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)

		try:
			extra_fields.setdefault('host_name', socket.gethostname())
			extra_fields.setdefault('last_update_host_name', socket.gethostname())
			extra_fields.setdefault('mac_address', self.get_mac_address())
		except:
		    extra_fields.setdefault('host_name', 'localhost')
		    extra_fields.setdefault('last_update_host_name', 'localhost')
		    extra_fields.setdefault('mac_address', self.get_mac_address())

		extra_fields.setdefault('ip_address', socket.gethostbyname(socket.gethostname()))
		extra_fields.setdefault('last_update_ip_address', socket.gethostbyname(socket.gethostname()))
		extra_fields.setdefault('last_update_mac_address', self.get_mac_address())
		
		return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		
		try:
			extra_fields.setdefault('host_name', socket.gethostname())
			extra_fields.setdefault('last_update_host_name', socket.gethostname())
			extra_fields.setdefault('mac_address', self.get_mac_address())
		except:
		    extra_fields.setdefault('host_name', 'localhost')
		    extra_fields.setdefault('last_update_host_name', 'localhost')
		    extra_fields.setdefault('mac_address', self.get_mac_address())

		extra_fields.setdefault('ip_address', socket.gethostbyname(socket.gethostname()))
		extra_fields.setdefault('last_update_ip_address', socket.gethostbyname(socket.gethostname()))
		extra_fields.setdefault('last_update_mac_address', self.get_mac_address())
		return self._create_user(username, email, password, **extra_fields)

	def get_mac_address(self):
		return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])


class AuthUser(AbstractBaseUser, PermissionsMixin):
	username 						= models.CharField(
														verbose_name='Nombre de usuario',
														max_length=50,
														unique=True,
														db_index=True,
														validators=[
															        MinLengthValidator(2),
															        MaxLengthValidator(50),
															    ]
													  )
	email    						= models.EmailField(
														verbose_name='Correo electrónico',	
														max_length=100,
														unique=True,
														db_index=True,
														validators=[
															EmailValidator(),
														]
													   )
	is_superuser  					= models.BooleanField(
															verbose_name='¿Super usuario?',	
															default=False
														)
	is_staff  						= models.BooleanField(
															verbose_name='¿Ingresa al staff?',	
															default=True
														)	
	is_active 						= models.BooleanField(
															verbose_name='¿Activo?',
															default=True
														)
	
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )
	registration_date 			   	= models.DateTimeField( 
															verbose_name='Fecha registro',
															auto_now_add=True, 
															auto_now=False
														)
	created_by        	 	 		= models.ForeignKey(
															'self', 
															verbose_name='Creado por',	
															null=True,
															default=None
														)
	host_name				    	= models.CharField(
														verbose_name='Nombre host', 
														max_length=255,
														validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		   	],
													)
	ip_address			    		= models.GenericIPAddressField(
														verbose_name='Dirección I.P.', 
														validators=[
														    validate_ipv46_address,
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		   	],
													)
	mac_address						= models.CharField(
														verbose_name='Dirección M.A.C.', 	
														max_length=255,
														validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		   	],
													)
	last_update_date				= models.DateTimeField(
															verbose_name='Fecha última actualización',
															auto_now_add=False,
															auto_now=True
														)
	last_updated_by					= models.ForeignKey(
														'self', 
														verbose_name='Última actualización por',		
														null=True, 
														default=None, 
														related_name='auth_users_auth_user_related')
	last_update_host_name 			= models.CharField(
														verbose_name='Última actualizacion de nombre host ', 
														max_length=255,
														validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		   	],
													)
	last_update_ip_address			= models.GenericIPAddressField(
														verbose_name='Última actualizacion de Dirección I.P.', 
														validators=[
														    validate_ipv46_address,
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		   	],
													)
	last_update_mac_address 		= models.CharField(
														verbose_name='Última actualizacion de Dirección M.A.C.', 	
														max_length=255,
														validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		   	],
													)

	objects = UserManager()

	USERNAME_FIELD  = 'username'
	REQUIRED_FIELDS = ['email',]

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.username)
		else:
			slug = slugify(self.username)
			if self.slug != slug:
				self.slug = slug
		super(AuthUser, self).save(*args, **kwargs)

	def get_short_name(self):
		return self.username

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'auth_users'
		#Ordenar los registros por un campo especifico
		ordering = ('username',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Auth User'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Auth Users'
