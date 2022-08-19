from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['id'] = user.id
        token['active'] = user.active
        token['profilepic'] = user.profilepic.name
        token['address'] = user.address
        token['phone'] = user.phone
        token['type'] = user.type
        token['gender'] = user.gender
        print(user.id)
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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


