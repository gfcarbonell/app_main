# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.template.defaultfilters import slugify
from infos_systems.models import InfoSystem
from identification_documents.models import IdentificationDocument 
from civil_states.models import CivilState 
from blood_groups.models import BloodGroup 
from infos_systems.models import InfoSystem


class Person(InfoSystem):
	__BOOL_GENDER		 					= 	((True, 'Male - Masculino'), (False, 'Female - Femenino'))
	__BOOL_TYPE_PERSON 						= 	((True, 'Natural - Natural'), (False, 'Legal - Jurídica'))
	type_person 							= 	models.BooleanField(
													choices=__BOOL_TYPE_PERSON, 
													default=True
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
	last_name 	   							= 	models.CharField(
													verbose_name='Apellido Paterno', 
											  		max_length=255,
										      		validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  		db_index=True, 
										  		)
	mother_last_name						= 	models.CharField(
													verbose_name='Apellido Materno', 
											  		max_length=255,
										      		validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(255),
										  		    ],
											  		db_index=True, 
										  		)	
	identification_document					= 	models.ForeignKey(
													IdentificationDocument, 
													verbose_name='Documento de Identificación', 
													related_name='%(app_label)s_%(class)s_related'
												)
	number_identification_document			= 	models.PositiveSmallIntegerField(
													verbose_name='Número Documento de Identificación', 
										      		validators=[
										  		        MinValueValidator(1),
										  		        MaxValueValidator(30),
										  		    ],
										  			db_index=True
										  		)	
	birth_day 								= 	models.DateField(
													verbose_name='Fecha de Nacimiento',
													default = '01-01-1980'
												)
	gender 									= 	models.BooleanField(
													choices=__BOOL_GENDER, 
													verbose_name='Género',
													default=True
												)
	civil_state								= 	models.ForeignKey(
													CivilState, 
													verbose_name='Estado Civil', 
													related_name='%(app_label)s_%(class)s_related'
												)
	blood_group								= 	models.ForeignKey(
													BloodGroup, 
													verbose_name='Grupo Sanguíneo', 
													null=True, 
													default=None,
													related_name='%(app_label)s_%(class)s_related'
												)
	photograph								=	models.ImageField(	
													blank=True,
													null=True,
													verbose_name='Fotografía',
													upload_to='image/photographs',
													default='default/No-Avatar-1.png'
												)
	email 									= 	models.EmailField(
													verbose_name='Correo electrónico',
													max_length=255,
													blank=True, null=True,
													validators=[
															EmailValidator(),
															MinLengthValidator(1),
															MaxLengthValidator(255),
														],
													db_index=True
												)
	telephone 								= models.CharField(verbose_name="Télefono",
													max_length=20,
													blank=True, 
													null=True
												)
	cell_phone								= models.CharField(verbose_name="Celular",
													max_length=20,
													blank=True, 
													null=True,
												)
	description    							= 	models.TextField(
													verbose_name='Descripción', 
													null=True, 
													blank=True
												)
	observation    							= 	models.TextField(
													verbose_name='Observación', 
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

	def get_last_name(self):
		return self.last_name
	
	def set_last_name(self, last_name):
		self.last_name = last_name

	def get_mother_last_name(self):
		return self.mother_last_name

	def set_mother_last_name(self, mother_last_name):
		self.mother_last_name = mother_last_name

	def get_full_name(self):
		return '%s | %s | %s' %(self.get_nombre() , self.get_last_name(), self.get_mother_last_name())

	#Opciones
	class Meta:
		abstract = True