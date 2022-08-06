from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, User):
        token = super().get_token(User)

        # Add custom claims
        token['username'] = User.username
        token['first_name'] = User.first_name
        token['last_name'] = User.last_name
        # token['groups'] = User.groups
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'api/token',
        'api/token/refresh',
    ]
    return Response(routes)
