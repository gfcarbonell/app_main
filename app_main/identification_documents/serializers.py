# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import IdentificationDocuments


class IdentificationDocumentsModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = IdentificationDocuments
		fields = ['id', 'name', 'abreviation', 'number_of_digits']

