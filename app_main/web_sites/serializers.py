# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import WebSite


class WebSiteModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebSite
		fields = ['id', 'url', 'description', 'is_active']
