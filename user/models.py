from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20,null='default userna')
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    # password=models.CharField(max_length=40,null=True)
    GENDER = [('Male','Male'),('Female','Female')]
    profilepic=models.ImageField(null=True)
    dob=models.DateField()
    gender=models.CharField(max_length=6,choices=GENDER,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Doctor(User):
    experince=models.CharField(max_length=255)
    qualification=models.CharField(max_length=255)

class Patient(User):
    patient_case=models.CharField(max_length=255)