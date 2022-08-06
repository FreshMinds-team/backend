from django.urls import path
from . import views

urlpatterns = [
    path('appointment/',views.getAppointment),
    path('appointment/add/',views.addAppointment),
    path('appointment/update/<str:pk>',views.updateAppointment),
    path('appointment/delete/<str:pk>',views.deleteAppointment),
]
