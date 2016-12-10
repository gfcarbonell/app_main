# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import WebSite 
from infos_systems.admin import InfoSystemAdmin

@admin.register(WebSite)
class WebSiteAdmin(InfoSystemAdmin, admin.ModelAdmin):
	list_display   = ['url', 'description', 'is_active'] + [

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

	list_instances = True
	search_fields  = ('url', 'description', 'is_active')

	class Meta:
		model = WebSite
