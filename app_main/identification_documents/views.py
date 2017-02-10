# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import IdentificationDocuments
from .serializers import IdentificationDocumentsModelSerializer


class IdentificationDocumentsModelViewSet(viewsets.ModelViewSet):
    model            = IdentificationDocuments
    serializer_class = IdentificationDocumentsModelSerializer
    queryset         = IdentificationDocuments.objects.all()
