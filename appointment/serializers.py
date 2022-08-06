from rest_framework import serializers
from appointment.models import Appointment
# from user.serializers import *

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
