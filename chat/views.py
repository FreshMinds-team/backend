from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET'])
def getChat(request):
    serializer = ChatSerializer(Chat.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addChat(request):
    serializer= ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
