# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from infos_systems.models import InfoSystem
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

from django.template.defaultfilters import slugify


class IdentificationDocuments(InfoSystem):
	name 	   								= 	models.CharField(
												verbose_name='Nombre', 
											  	max_length=255,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  	db_index=True, 
										  	)
	abreviation 	   						= 	models.CharField(
												verbose_name='Abreviatura', 
											  	max_length=30,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(30),
										  		    ],
											  	db_index=True, 
										  	)
	number_of_digits						= 	models.PositiveSmallIntegerField(
												verbose_name='Número de digitos', 
										      	validators=[
										  		        MinValueValidator(1),
										  		        MaxValueValidator(30),
										  		    ],
										  	)	
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_name()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name 

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_name())
		else:
			slug = slugify(self.get_name())
			if self.slug != slug:
				self.slug = slug
		super(IdentificationDocuments, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'identification_documents'
		#Ordenar los registros por un campo especifico
		ordering = ('name',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Identification Document'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Identification Documents'
