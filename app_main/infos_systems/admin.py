# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import InfoSystem
import socket
import uuid


class InfoSystemAdmin():

	list_display = [
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
	exclude = [
			'created_by',
			'host_name', 
			'ip_address', 
			'mac_address', 
			'last_updated_by', 
			'last_update_host_name', 
			'last_update_ip_address', 
			'last_update_mac_address', 
		]

	def get_mac_address(self):
		return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])

	def save_model(self, request, obj, form, change):
		if change:
			obj.last_updated_by = request.user
			try:
				obj.last_update_host_name = socket.gethostname()
			except:
				obj.last_update_host_name = 'localhost'

			obj.last_update_ip_address  = socket.gethostbyname(socket.gethostname())
			obj.last_update_mac_address = self.get_mac_address()
		else:
			obj.created_by      = request.user
			obj.last_updated_by = obj.created_by
			try:
			   obj.host_name 			 = socket.gethostname()
			   obj.mac_address 		  	 = self.get_mac_address()
			   obj.ip_address   		 = socket.gethostbyname(socket.gethostname())
			except:
			   obj.host_name  			 = 'localhost'
			   obj.mac_address 		     = self.get_mac_address()
			   obj.ip_address   		 = socket.gethostbyname(socket.gethostname())
			  
			obj.last_update_host_name 	 = obj.host_name
			obj.last_update_ip_address   = obj.ip_address
			obj.last_update_mac_address  = obj.mac_address
		obj.save()

	class Meta:
		abstract = True