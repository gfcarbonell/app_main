# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import WebSlider 
from infos_systems.admin import InfoSystemAdmin

@admin.register(WebSlider)
class WebSliderAdmin(InfoSystemAdmin, admin.ModelAdmin):
	list_display   = ['get_name', 'is_selected', 'position'] + [

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
	search_fields  = ('id',)

	class Meta:
		model = WebSlider