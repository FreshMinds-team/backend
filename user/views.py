from user.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getDoctor(request):
    serializer = DoctorSerializer(Doctor.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addDoctor(request):
    serializer= DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateDoctor(request,id):
    doctor = Doctor.objects.get(pk=id)
    serializer = DoctorSerializer(instance=doctor,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteDoctor(request,id):
    doctor = Doctor.objects.get(pk=id)
    serializer = DoctorSerializer(instance=doctor,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Doctor Record Successfully deleted')
    

@api_view(['GET'])
def getPatient(request):
    serializer = PatientSerializer(Patient.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPatient(request):
    serializer= PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePatient(request,id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePatient(request,id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(instance=patient,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('Patient Record Successfully deleted')