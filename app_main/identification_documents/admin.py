# -*- encoding: utf-8 -*-
from django.contrib import admin
from infos_systems.admin import InfoSystemAdmin
from .models import IdentificationDocuments


@admin.register(IdentificationDocuments)
class IdentificationDocumentsAdmin(InfoSystemAdmin, admin.ModelAdmin):

	list_display =  ['name', 'abreviation', 'number_of_digits'] + [
	
						'slug', 
						'registration_date', 
						'created_by', 
						'host_name', 
						'ip_address', 
						'mac_address',
				    	'last_update_date', 
				    	'last_updated_by', 
				    	'last_update_host_name', 
				    	'last_update_ip_address', 
				    	'last_update_mac_address'
				     ]

	search_fields  = ('name', 'id')
	
	class Meta:
		model = IdentificationDocuments
