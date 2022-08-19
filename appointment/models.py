from django.db import models
from user.models import *

class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,related_name="appoint_patient")
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,related_name="appointed")
    accepted=models.BooleanField(default=False)
    closed=models.BooleanField(default=False)
    description= models.TextField(max_length=255,null=True)
    appointment_time=models.TimeField()
    appointment_date=models.DateField()
    price=models.CharField(max_length=10,null=True)
    payment_id=models.CharField(max_length=30,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __date__(self):
        return self.appointment_date

