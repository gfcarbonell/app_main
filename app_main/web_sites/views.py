# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import WebSite
from .serializers import WebSiteModelSerializer


class WebSiteViewSet(viewsets.ModelViewSet):
    model            = WebSite
    serializer_class = WebSiteModelSerializer
    queryset         = WebSite.objects.all()
