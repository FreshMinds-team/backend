from medication.serializers import *
from medication.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getMedication(request):
    serializer = MedicationSerializer(Medication.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addMedication(request):
    serializer= MedicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateMedication(request,id):
    medication = Medication.objects.get(pk=id)
    serializer = MedicationSerializer(instance=medication,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteMedication(request,id):
    medication = Medication.objects.get(pk=id)
    serializer = MedicationSerializer(instance=medication,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Medication Record Successfully deleted')
    

