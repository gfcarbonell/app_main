# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import WebSlide


class WebSlideModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebSlide
		fields = ['id', 'title', 'slogan', 'image', 'description']
