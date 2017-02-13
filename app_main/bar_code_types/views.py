# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import BarCodeType
from .serializers import BarCodeTypeModelSerializer


class BarCodeTypeModelViewSet(viewsets.ModelViewSet):
    model            = BarCodeType
    serializer_class = BarCodeTypeModelSerializer
    queryset         = BarCodeType.objects.all()
