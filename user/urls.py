from django.urls import path
from . import views

urlpatterns = [
    path('user/partial/<str:pk>',views.updateUserPartial),

    path('doctor/',views.getDoctor),
    path('doctor/add/',views.addDoctor),
    path('doctor/details/<int:id>',views.getDoctorDetails),
    path('doctor/update/<str:pk>',views.updateDoctor),
    path('doctor/partial/<str:pk>',views.updateDoctorPartial),
    path('doctor/delete/<str:pk>',views.deleteDoctor),
    
    path('qualification/<int:id>',views.getQualification),
    path('qualification/add/',views.addQualification),
    path('qualification/update/<str:pk>',views.updateQualification),
    path('qualification/delete/<str:pk>',views.deleteQualification),
    
    path('experience/<int:id>',views.getExperience),
    path('experience/add/',views.addExperience),
    path('experience/update/<str:pk>',views.updateExperience),
    path('experience/delete/<str:pk>',views.deleteExperience),
    
    path('expertise/<int:id>',views.getExpertise),
    path('expertise/add/',views.addExpertise),
    path('expertise/update/<str:pk>',views.updateExpertise),
    path('expertise/delete/<str:pk>',views.deleteExpertise),
    
    path('patient/',views.getPatient),
    path('patient/add/',views.addPatient),
    path('patient/update/<str:pk>',views.updatePatient),
    path('patient/delete/<str:pk>',views.deletePatient),
    path('patient/details/<int:id>',views.getPatientDetails),
    path('patient/partial/<str:pk>',views.updatePatientPartial),
]
