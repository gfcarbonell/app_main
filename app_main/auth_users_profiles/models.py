# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from auth_users.models import AuthUser
from persons.models import Person
from bar_code_types.models import BarCodeType


class AuthUserProfile(Person):
	auth_user 								= 	models.OneToOneField(
													AuthUser, 
													#related_name='auth_user_authuserprofiles_related'
													related_name='%(app_label)s_%(class)s_related'
												)
	bar_code_type 							=	models.ForeignKey(
													BarCodeType, 
													verbose_name='Tipo de Código de Barra', 
													related_name='%(app_label)s_%(class)s_related'
												)
	bar_code_value 	   						= 	models.CharField(
													verbose_name='Valor Código de Barra', 
												  	max_length=255,
											      	validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		    ],
												  	db_index=True, 
											  	)
	bar_code_image							=	models.ImageField(	
													verbose_name='Imagen Código de Barra',
													upload_to='image/bar_codes',
												)	
	is_active 								= 	models.BooleanField(
													verbose_name='¿Activo?',
													default=True
												)
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_full_name()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_full_name())
		else:
			slug = slugify(self.get_full_name())
			if self.slug != slug:
				self.slug = slug
		super(AuthUserProfile, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		abstract = True
