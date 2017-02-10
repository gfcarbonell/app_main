# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import BloodGroup
from .serializers import BloodGroupModelSerializer


class BloodGroupModelViewSet(viewsets.ModelViewSet):
    model            = BloodGroup
    serializer_class = BloodGroupModelSerializer
    queryset         = BloodGroup.objects.all()
