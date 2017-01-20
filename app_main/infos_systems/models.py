# -*- encoding: utf-8 -*-
from django.db import models
from auth_users.models import AuthUser
from django.core.validators import validate_ipv46_address
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator


class InfoSystem(models.Model):
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )
	registration_date 			   	= models.DateTimeField( 
															verbose_name='Fecha registro',
															auto_now_add=True, 
															auto_now=False
														)
	created_by        	 	 		= models.ForeignKey(
														AuthUser, 
														verbose_name='Creado por',		
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
														AuthUser, 
														verbose_name='Última actualización por',
														related_name='%(app_label)s_%(class)s_related'
													)
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

	class Meta:
		abstract = True
