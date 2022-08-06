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

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualification
        fields="__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields="__all__"

class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expertise
        fields="__all__"
