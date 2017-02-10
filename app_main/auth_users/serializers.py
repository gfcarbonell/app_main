# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import AuthUser


class AuthUserModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = AuthUser
		fields = ['id', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'last_login']

