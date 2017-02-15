# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Province
from departments.serializers import DepartmentModelSerializer


class ProvinceModelSerializer(serializers.ModelSerializer):
	department = DepartmentModelSerializer(many=False)
	class Meta:
		model = Province
		fields = ['id', 'department', 'name', 'photograph', 'description']

