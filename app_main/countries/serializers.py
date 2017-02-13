# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Country


class CountryModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ['name', 'postal_code', 'photograph', 'description']

