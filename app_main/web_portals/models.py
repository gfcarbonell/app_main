# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from infos_systems.models import InfoSystem
from infos_systems.validators import valid_extension
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator 
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify

from web_headers.models import WebHeader
from web_sliders.models import WebSlider


class WebPortal(InfoSystem):
	__BOOL_SELECTED 		 			= 	((True, 'Yes'), (False, 'Not'))
	web_header 							= 	models.ForeignKey(
																WebHeader, 
																verbose_name='Web header', 
											)
	web_slider 							= 	models.ForeignKey(
																WebSlider, 
																verbose_name='Web slider', 
											)
	is_selected 						=   models.BooleanField(
															choices=__BOOL_SELECTED, 
															verbose_name='¿Es Seleccionado?',
															default=True
														)
	is_main 							=   models.BooleanField(
															choices=__BOOL_SELECTED, 
															verbose_name='¿Es Principal?',
															default=False
														)


	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_name()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def get_name(self):
		return '%s | %s' %(self.web_header.get_name(), self.web_slider.get_title())

	def get_is_selected(self):
		return self.is_selected

	def set_is_selected(self, is_selected):
		self.is_selected = is_selected 

	def get_is_main(self):
		return self.is_main 

	def set_is_main(self, is_main):
		self.is_main = is_main

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_name())
		else:
			slug = slugify(self.get_name())
			if self.slug != slug:
				self.slug = slug
		super(WebPortal, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'web_portals'
		#Ordenar los registros por un campo especifico
		ordering = ('web_header', 'web_slider')
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Web Portal'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Web Portals'
