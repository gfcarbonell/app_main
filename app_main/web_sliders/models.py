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

from web_sections.models import WebSection
from web_slides.models import WebSlide


class WebSlider(InfoSystem):
	__BOOL_SELECTED 		 			= 	((True, 'Yes'), (False, 'Not'))
	web_section 						= 	models.ForeignKey(
																WebSection, 
																verbose_name='Sección Web', 
											)
	web_slide 							= 	models.ForeignKey(
																WebSlide, 
																verbose_name='Diapositiva Web', 
											)
	is_selected 						=   models.BooleanField(
															choices=__BOOL_SELECTED, 
															verbose_name='¿Es Seleccionado?',
															default=True
														)
	position 							= 	models.SmallIntegerField(
												default = 0,
												validators=[
															MinValueValidator(0),
                                       						MaxValueValidator(7)
                                       					],
                                       			help_text='Ingresar posición de las diapositivas web, rango (1-7) .'
											)


	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_name()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def get_name(self):
		return '%s | %s' %(self.web_section.get_name(), self.web_slide.get_title())

	def get_is_selected(self):
		return self.is_selected

	def set_is_selected(self, is_selected):
		self.is_selected = is_selected 

	def get_position(self):
		return self.position 

	def set_position(self, position):
		self.position = position


	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_name())
		else:
			slug = slugify(self.get_name())
			if self.slug != slug:
				self.slug = slug
		super(WebSlider, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'web_sliders'
		#Ordenar los registros por un campo especifico
		ordering = ('web_section', 'web_slide')
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Web Slider'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Web Slider'
