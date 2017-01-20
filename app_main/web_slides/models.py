# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from infos_systems.models import InfoSystem
from infos_systems.validators import valid_extension
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class WebSlide(InfoSystem):
	title 	   							= 	models.CharField(
												verbose_name='Título', 
											  	max_length=255,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  	unique=True, 
											  	db_index=True, 
										  	)
	slogan 	   							= 	models.CharField(
												verbose_name='Slogan', 
											  	max_length=255,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  	unique=True, 
											  	db_index=True, 
										  	)
	image   							= models.ImageField(
															verbose_name='Imagen',
															upload_to='images_web_slides',
															default='default/No_Avatar_1.png',
															validators=[
												  		        valid_extension
												  		    ],
														)
	description    						= 	models.TextField(
												verbose_name='Descripción', 
												null=True, 
												blank=True,	
												help_text='Escribir una descripción del sitio web (opcional) .'
											)

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_title()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def get_title(self):
		return self.title

	def set_title(self, title):
		self.title = title 

	def get_slogan(self):
		return self.slogan 

	def set_slogan(self, slogan):
		self.slogan = slogan

	def get_image(self):
		return self.image

	def set_image(self, image):
		self.image = image

	def get_description(self):
		return self.description

	def set_description(self, description):
		self.description = description

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_title())
		else:
			slug = slugify(self.get_title())
			if self.slug != slug:
				self.slug = slug
		super(WebSlide, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'web_slides'
		#Ordenar los registros por un campo especifico
		ordering = ('title',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Web Slide'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Web Slides'
