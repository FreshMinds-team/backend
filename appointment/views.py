from errno import ESTALE
from appointment.serializers import *
from appointment.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAppointment(request):
    serializer = Appointment1Serializer(Appointment.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPatientPendingAppointment(request,pk):
    serializer = Appointment1Serializer(Appointment.objects.filter(patient=pk,closed=False),many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPatientAcceptedAppointment(request,pk):
    serializer = Appointment1Serializer(Appointment.objects.filter(patient=pk,closed=False,accepted=True),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAppointmentDetails(request,id):
    serializer = Appointment1Serializer(Appointment.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAppointment(request):
    print(request.data)
    serializer= AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAppointment(request,pk):
    appointment = Appointment.objects.get(id=pk)
    serializer = AppointmentSerializer(instance=appointment,data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAppointment(request,pk):
    Appointment.objects.get(id=pk).delete()
    return Response('appointment Record Successfully deleted')
    

