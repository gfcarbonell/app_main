# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import WebSlide
from .serializers import WebSlideModelSerializer


class WebSlideModelViewSet(viewsets.ModelViewSet):
    model            = WebSlide
    serializer_class = WebSlideModelSerializer
    queryset         = WebSlide.objects.all()
