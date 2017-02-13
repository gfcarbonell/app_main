# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentModelSerializer


class DepartmentModelViewSet(viewsets.ModelViewSet):
    model            = Department
    serializer_class = DepartmentModelSerializer
    queryset         = Department.objects.all()
