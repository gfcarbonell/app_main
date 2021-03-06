# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from infos_systems.models import InfoSystem
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
from provinces.models import Province


class District(InfoSystem):
	province 								=	models.ForeignKey(
													Province, 
													verbose_name='Provincia', 
												)
	name 	   								= 	models.CharField(
												verbose_name='Nombre', 
											  	max_length=255,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  	db_index=True, 
										  	)
	photograph								=	models.ImageField(	
												blank=True,
												null=True,
												verbose_name='Fotografía',
												upload_to='image/districts',
												default='default/No-Avatar-1.png'
											)
	description    							= 	models.TextField(
												verbose_name='Descripción', 
												null=True, 
												blank=True
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
		super(District, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'districts'
		#Ordenar los registros por un campo especifico
		ordering = ('name',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'District'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Districts'
