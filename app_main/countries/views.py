# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from .serializers import CountryModelSerializer


class CountryModelViewSet(viewsets.ModelViewSet):
    model            = Country
    serializer_class = CountryModelSerializer
    queryset         = Country.objects.all()
