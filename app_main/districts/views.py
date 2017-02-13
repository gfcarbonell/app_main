# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import District
from .serializers import DistrictModelSerializer


class DistrictModelViewSet(viewsets.ModelViewSet):
    model            = District
    serializer_class = DistrictModelSerializer
    queryset         = District.objects.all()
