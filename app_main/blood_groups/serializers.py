# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import BloodGroup


class BloodGroupModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = BloodGroup
		fields = ['id', 'name']



