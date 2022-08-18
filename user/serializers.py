from xml.etree.ElementInclude import include
from rest_framework import serializers
from appointment.serializers import AppointmentSerializer
from medication.serializers import MedicationSerializer
from user.models import *
from django.contrib.auth.hashers import make_password

class PatientSerializer(serializers.ModelSerializer):
    appoint_patient = AppointmentSerializer(many=True,read_only=True,allow_null=True)
    medicine = MedicationSerializer(many=True,read_only=True,allow_null=True)
    
    def create(self, validated_data):
     patient = Patient(
        email = self.validated_data['email'],
        username = self.validated_data['username'],
        first_name = self.validated_data['first_name'],
        last_name = self.validated_data['last_name'],
        phone = self.validated_data['phone'],
        address = self.validated_data['address'],
        type = self.validated_data['type'],
        dob = self.validated_data['dob'],
        profilepic = self.validated_data['profilepic'],
        gender = self.validated_data['gender'],
        )
     patient.set_password(validated_data['password'])
     patient.save()
     return patient

    class Meta:
        model=Patient
        fields="__all__"

class DoctorSerializer(serializers.ModelSerializer):
    appointed= AppointmentSerializer(many=True,read_only=True,allow_null=True)
    class Meta:
        model=Doctor
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
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

class DoctorDataSerializer(serializers.ModelSerializer):
    appointed= AppointmentSerializer(many=True,read_only=True,allow_null=True)
    class Meta:
        model=Doctor
        fields="__all__"