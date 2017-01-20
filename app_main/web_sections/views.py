# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import WebSection
from .serializers import WebSectionModelSerializer


class WebSectionModelViewSet(viewsets.ModelViewSet):
    model            = WebSection
    serializer_class = WebSectionModelSerializer
    queryset         = WebSection.objects.all()
