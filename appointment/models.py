from django.db import models
from user.models import *

class Appointment(models.Model):
    patient=models.OneToOneField(Patient,on_delete=models.CASCADE,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    accepted=models.BooleanField(default=False)
    appointment_time=models.TimeField()
    appointment_date=models.DateField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __date__(self):
        return self.appointment_date

