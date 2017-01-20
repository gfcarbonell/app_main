# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from infos_systems.models import InfoSystem
from infos_systems.validators import valid_extension
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from web_sliders.models import WebSlider
from embed_video.fields import EmbedVideoField


class WebHeader(InfoSystem):
	__BOOL_SELECTED 		 			= 	((True, 'Yes'), (False, 'Not'))
	__BOOL_VIDEO_SOURCE 	 			= 	((True, 'U.R.L.'), (False, 'File'))
	web_slider 							= models.ManyToManyField(
												WebSlider, 
												through='web_portals.WebPortal'
											)
	name 	   							= 	models.CharField(
												verbose_name='Nombre', 
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
	image_left  						= 	models.ImageField(
												verbose_name='Imagen (Izquierdo)',
												upload_to='images_web_headers',
												default='default/No_Avatar_1.png',
												validators=[
									  		        valid_extension
									  		    ],
											)
	image_right   						= 	models.ImageField(
												verbose_name='Imagen (Derecho)',
												upload_to='images_web_headers',
												default='default/No_Avatar_1.png',
												validators=[
									  		        valid_extension
									  		    ],
											)
	is_video 	 						=   models.BooleanField(
															choices=__BOOL_SELECTED, 
															verbose_name='¿Es Vídeo?',
															default=False
														)
	video_source 						=   models.BooleanField(
															choices=__BOOL_VIDEO_SOURCE, 
															verbose_name='Fuente de vídeo',
															default=True
														)
	video_url 	   						= 	EmbedVideoField(
												verbose_name='U.R.L. (Vídeo)', 
											  	max_length=255,
										      	validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  	unique=True, 
											  	db_index=True, 
											  	blank=True,
											  	null=True
										  	)
	video_file 							= 	models.FileField(
												verbose_name='Archivo (Vídeo)',
												upload_to='videos_web_headers',
												blank=True,
												null=True
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
		super(WebHeader, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'web_headers'
		#Ordenar los registros por un campo especifico
		ordering = ('name',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Web Header'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Web Headers'
