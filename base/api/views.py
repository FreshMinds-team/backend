from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import *
@api_view(['GET'])
def getRoutes(request):
    routes=[
        'doctor/',
        'doctor/add/',
        'doctor/update/<str:pk>',
        'doctor/delete/<str:pk>',
        'patient/',
        'patient/add/',
        'patient/update/<str:pk>',
        'patient/delete/<str:pk>',
        'appointment/',
        'appointment/add/',
        'appointment/update/<str:pk>',
        'appointment/delete/<str:pk>',
        'medication/',
        'medication/add/',
        'medication/update/<str:pk>',
        'medication/delete/<str:pk>',
        'chat/',
        'chat/add/',
        'chat/update/<str:pk>',
        'chat/delete/<str:pk>',
    ]
    return Response(routes)


