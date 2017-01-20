# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import WebSlider
from web_sections.serializers import WebSectionModelSerializer
from web_slides.serializers import WebSlideModelSerializer


class WebSliderModelSerializer(serializers.ModelSerializer):
	web_section = WebSectionModelSerializer(many=False)
	web_slide 	= WebSlideModelSerializer(many=False)
	class Meta:
		model = WebSlider
		fields = ['id', 'web_section', 'web_slide', 'is_selected', 'position', ]
