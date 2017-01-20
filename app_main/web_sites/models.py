# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from infos_systems.models import InfoSystem
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class WebSite(InfoSystem):
	__BOOL_SELECTED 		 			= 	((True, 'Yes'), (False, 'Not'))
	url 	   							= 	models.URLField(
												verbose_name='U.R.L.', 
											  	max_length=255,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  	unique=True, 
											  	db_index=True, 
										  	)
	description    						= 	models.TextField(
												verbose_name='Descripción', 
												null=True, 
												blank=True,	
												help_text='Escribir una descripción del sitio web (opcional) .'
											)
	is_active 							=   models.BooleanField(
															choices=__BOOL_SELECTED, 
															verbose_name='¿Activo?',
															default=True
														)

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_url()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def get_url(self):
		return self.url

	def set_url(self, url):
		self.url = url 

	def get_description(self):
		return self.description 

	def set_description(self, description):
		self.description = description

	def get_is_active(self):
		return self.is_active

	def set_is_active(self, is_active):
		self.is_active = is_active

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_url())
		else:
			slug = slugify(self.get_url())
			if self.slug != slug:
				self.slug = slug
		super(WebSite, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'web_sites'
		#Ordenar los registros por un campo especifico
		ordering = ('url',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Web Site'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Web Sites'
