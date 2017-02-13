# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Person
from infos_systems.admin import InfoSystemAdmin


class PersonAdmin(InfoSystemAdmin):

	list_display =  [
						'type_person', 
						'get_full_name', 
						'identification_document', 
						'number_identification_document', 
						'birth_day', 
						'gender', 
						'civil_state', 
						'blood_group', 
						'photograph', 
						'email', 
						'telephone', 
						'cell_phone', 
						'description', 
						'observation'
					] + [
	
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
		abstract = True
