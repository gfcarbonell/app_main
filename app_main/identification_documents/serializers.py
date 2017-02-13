# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import IdentificationDocument


class IdentificationDocumentModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = IdentificationDocument
		fields = ['id', 'name', 'abreviation', 'number_of_digits']

