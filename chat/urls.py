from django.urls import path
from . import views

urlpatterns = [
    path('chat/',views.getChat),
    path('chat/add',views.addChat),
]
