from medication.serializers import *
from medication.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMedication(request):
    serializer = MedicationSerializer(Medication.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMedicationDetails(request,id):
    serializer = MedicationSerializer(Medication.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMedication(request):
    serializer= MedicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateMedication(request,id):
    medication = Medication.objects.get(pk=id)
    serializer = MedicationSerializer(instance=medication,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMedication(request,id):
    medication = Medication.objects.get(pk=id)
    serializer = MedicationSerializer(instance=medication,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Medication Record Successfully deleted')
    

