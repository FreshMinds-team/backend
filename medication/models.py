from django.db import models
from user.models import Patient

class Medication(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,related_name='medicine')
    medicine=models.CharField(max_length=255)
    amount=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    prescribed_date=models.DateField(auto_now=True)

