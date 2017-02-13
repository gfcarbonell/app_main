# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import Province
from .serializers import ProvinceModelSerializer


class ProvinceModelViewSet(viewsets.ModelViewSet):
    model            = Province
    serializer_class = ProvinceModelSerializer
    queryset         = Province.objects.all()
