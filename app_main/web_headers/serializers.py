# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import WebHeader


class WebHeaderModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebHeader
		fields = [
					'id', 'name', 'slogan','image_left', 'image_right',
					'is_video', 'video_source', 'video_url', 'video_file'
		 		]
