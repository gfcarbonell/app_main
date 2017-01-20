# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import WebSlider
from .serializers import WebSliderModelSerializer


class WebSliderModelViewSet(viewsets.ModelViewSet):
    model            = WebSlider
    serializer_class = WebSliderModelSerializer
    queryset         = WebSlider.objects.all()
