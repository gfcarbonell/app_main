# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import AuthUser
from .serializers import AuthUserModelSerializer


class AuthUserModelViewSet(viewsets.ModelViewSet):
    model            = AuthUser
    serializer_class = AuthUserModelSerializer
    queryset         = AuthUser.objects.all()
