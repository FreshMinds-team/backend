from django.urls import path,include
from  . import views
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include('user.urls')),
    path('',include('appointment.urls')),
    path('',include('chat.urls')),
    path('',include('medication.urls')),
]
