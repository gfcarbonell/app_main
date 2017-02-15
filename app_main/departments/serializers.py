# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Department
from countries.serializers import CountryModelSerializer

class DepartmentModelSerializer(serializers.ModelSerializer):
	country = CountryModelSerializer(many=False)
	class Meta:
		model = Department
		fields = ['id', 'country', 'name', 'postal_code', 'photograph', 'description']

