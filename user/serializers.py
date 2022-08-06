from xml.etree.ElementInclude import include
from rest_framework import serializers
from appointment.serializers import AppointmentSerializer
from medication.serializers import MedicationSerializer
from user.models import *

class PatientSerializer(serializers.ModelSerializer):
    appoint_patient = AppointmentSerializer(many=True,read_only=True,allow_null=True)
    medicine = MedicationSerializer(many=True,read_only=True,allow_null=True)
    class Meta:
        model=Patient
        fields="__all__"

class DoctorSerializer(serializers.ModelSerializer):
    appointed= AppointmentSerializer(many=True,read_only=True,allow_null=True)
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
