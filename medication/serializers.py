from rest_framework import serializers
from medication.models import Medication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medication
        fields="__all__"
