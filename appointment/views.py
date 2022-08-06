from appointment.serializers import *
from appointment.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getAppointment(request):
    serializer = Appointment1Serializer(Appointment.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAppointmentDetails(request,id):
    serializer = Appointment1Serializer(Appointment.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addAppointment(request):
    serializer= Appointment1Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateAppointment(request,id):
    appointment = appointment.objects.get(pk=id)
    serializer = Appointment1Serializer(instance=appointment,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAppointment(request,id):
    appointment = appointment.objects.get(pk=id)
    serializer = Appointment1Serializer(instance=appointment,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('appointment Record Successfully deleted')
    

