# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import CivilState
from .serializers import CivilStateModelSerializer


class CivilStateModelViewSet(viewsets.ModelViewSet):
    model            = CivilState
    serializer_class = CivilStateModelSerializer
    queryset         = CivilState.objects.all()
