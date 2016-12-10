# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
import socket
import uuid

class InfoSystemCreateView(CreateView):

	def get_mac_address_short(self):
		mac_address = hex(uuid.getnode()).replace('0x', '')
		return ':'.join(mac_address[i : i + 2] for i in range(0, 11, 2))

	def get_mac_address(self):
		return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
	
	def form_valid(self, form):
		self.object = form.save(commit=False)

		self.object.created_by      = self.request.user
		self.object.last_updated_by = self.object.created_by

		try:
		   self.object.host_name 			 = socket.gethostname()
		   self.object.ip_address   		 = socket.gethostbyname(socket.gethostname())
		   self.object.mac_address 		     = self.get_mac_address()
		   
		except:
		   self.object.host_name  			 = 'localhost'
		   self.object.ip_address   		 = socket.gethostbyname(socket.gethostname())
		   self.object.mac_address 		     = self.get_mac_address()

		self.object.last_update_host_name 	 = self.object.host_name
		self.object.last_update_ip_address   = self.object.ip_address
		self.object.last_update_mac_address  = self.object.mac_address
		self.object.save()