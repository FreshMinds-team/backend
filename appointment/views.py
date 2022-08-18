from appointment.serializers import *
from appointment.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAppointment(request):
    serializer = Appointment1Serializer(Appointment.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAppointmentDetails(request,id):
    serializer = Appointment1Serializer(Appointment.objects.get(pk=id),many=False)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def addAppointment(request):
    print(request.data)
    serializer= AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateAppointment(request,pk):
    appointment = Appointment.objects.get(id=pk)
    serializer = Appointment1Serializer(instance=appointment,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAppointment(request,id):
    appointment = Appointment.objects.get(pk=id)
    serializer = Appointment1Serializer(instance=appointment,data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response('appointment Record Successfully deleted')
    

