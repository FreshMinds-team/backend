from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:room>',views.getChat),
    path('chat/',views.getChats),
    path('chats/add',views.addChat),
]
