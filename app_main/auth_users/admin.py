# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from infos_systems.admin import InfoSystemAdmin
from .models import AuthUser

@admin.register(AuthUser)
# Por defecto el admin usa -> UserAdmin
class AuthUserAdmin(InfoSystemAdmin, UserAdmin):

	list_display =  ['username', 'email', 'password', 'is_superuser',  'is_staff', 'is_active', 'last_login'] + [
	
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

	search_fields  = ('username', 'id')

	fieldsets = (
			(('User Info'), {'fields':('username', 'password', 'email')}),

			(('Permissions'), {'fields':( 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
			
		)
	class Meta:
		model = AuthUser
