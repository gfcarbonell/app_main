# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import WebHeader
from .serializers import WebHeaderModelSerializer


class WebHeaderModelViewSet(viewsets.ModelViewSet):
    model            = WebHeader
    serializer_class = WebHeaderModelSerializer
    queryset         = WebHeader.objects.all()
