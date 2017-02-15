# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import District
from provinces.serializers import ProvinceModelSerializer


class DistrictModelSerializer(serializers.ModelSerializer):
	province = ProvinceModelSerializer(many=False)
	class Meta:
		model = District
		fields = ['id', 'province', 'name', 'photograph', 'description']

