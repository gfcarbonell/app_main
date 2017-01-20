# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import WebHeader 
from infos_systems.admin import InfoSystemAdmin
from embed_video.admin import AdminVideoMixin

@admin.register(WebHeader)
class WebHeaderAdmin(InfoSystemAdmin, AdminVideoMixin, admin.ModelAdmin):
	list_display   = ['name', ] + [

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
	search_fields  = ('name',)

	class Meta:
		model = WebHeader