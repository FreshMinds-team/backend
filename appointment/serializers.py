from rest_framework import serializers
from appointment.models import Appointment
from user.models import *

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"

class ShallowPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['id','username','first_name','last_name','email','phone','address','profilepic']

class ShallowDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['id','username','first_name','last_name','email','phone','address','profilepic']

class Appointment1Serializer(serializers.ModelSerializer):
    patient=ShallowPatientSerializer(many=False,read_only=True)
    doctor=ShallowDoctorSerializer(many=False,read_only=True)
    class Meta:
        model=Appointment
        fields=['id','patient','appointment_date','appointment_time','doctor','price','description','accepted','closed','payment_id']
