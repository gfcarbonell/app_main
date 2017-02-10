# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import CivilState


class CivilStateModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = CivilState
		fields = ['id', 'name']

