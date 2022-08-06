from django.urls import path,include
from  . import views
from .views import *
from user.views import *
from appointment.views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('',include('user.urls')),
    path('',include('appointment.urls')),
    path('',include('chat.urls')),
]
