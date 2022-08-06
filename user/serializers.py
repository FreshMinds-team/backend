from rest_framework import serializers
from user.models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"
