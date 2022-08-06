from django.urls import path
from . import views

urlpatterns = [
    path('doctor/',views.getDoctor),
    path('doctor/add/',views.addDoctor),
    path('doctor/details/<int:id>',views.getDoctorDetails),
    path('doctor/update/<str:pk>',views.updateDoctor),
    path('doctor/delete/<str:pk>',views.deleteDoctor),
    path('patient/',views.getPatient),
    path('patient/add/',views.addPatient),
    path('patient/update/<str:pk>',views.updatePatient),
    path('patient/delete/<str:pk>',views.deletePatient),
    path('patient/details/<int:id>',views.getPatientDetails),
]
