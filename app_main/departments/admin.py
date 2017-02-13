# -*- encoding: utf-8 -*-
from django.contrib import admin
from infos_systems.admin import InfoSystemAdmin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(InfoSystemAdmin, admin.ModelAdmin):

	list_display =  ['country', 'name', 'postal_code', 'photograph', 'description'] + [
	
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
		model = Department
