from rest_framework import serializers
from user.models import User
from django.db import model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
