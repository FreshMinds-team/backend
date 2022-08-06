from django.urls import path
from . import views

urlpatterns = [
    path('medication/',views.getMedication),
    path('medication/details/<int:id>',views.getMedicationDetails),
    path('medication/add/',views.addMedication),
    path('medication/update/<str:pk>',views.updateMedication),
    path('medication/delete/<str:pk>',views.deleteMedication),
]

