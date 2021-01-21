# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfileInfo

class UserProfileInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = ('Name','email','Contact','portfolio_site','Address')