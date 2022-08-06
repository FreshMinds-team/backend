from django.urls import path
from . import views

urlpatterns = [
    path('chat/',views.getChat),
    path('chat/add',views.addChat),
    path('chat/update/<str:pk>',views.updateChat),
    path('chat/delete/<str:pk>',views.deleteChat),
]
