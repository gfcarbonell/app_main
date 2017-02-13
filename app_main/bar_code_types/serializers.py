# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import BarCodeType


class BarCodeTypeModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = BarCodeType
		fields = ['id', 'name']

