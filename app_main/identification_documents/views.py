# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import IdentificationDocument
from .serializers import IdentificationDocumentModelSerializer


class IdentificationDocumentModelViewSet(viewsets.ModelViewSet):
    model            = IdentificationDocument
    serializer_class = IdentificationDocumentModelSerializer
    queryset         = IdentificationDocument.objects.all()
