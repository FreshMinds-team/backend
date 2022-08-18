from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChat(request,room):
    serializer = ChatSerializer(Chat.objects.filter(room=room),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChats(request):
    serializer = ChatSerializer(Chat.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addChat(request):
    serializer= ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
