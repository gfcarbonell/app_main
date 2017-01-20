# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import WebSection


class WebSectionModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebSection
		fields = ['id', 'name', ]
