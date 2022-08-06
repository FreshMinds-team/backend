from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class User(AbstractUser):
    username=models.CharField(max_length=20,unique=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    email=models.EmailField(null=True)
    GENDER = [('Male','Male'),('Female','Female'),('Other',"Other")]
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=6,choices=GENDER,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username

class Doctor(User):
    profilepic=models.ImageField(upload_to="media/doctor",null=True)
    class Meta:
        pass

class Qualification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    institution = models.CharField(max_length=100)
    date = models.DateField()
    doctor = models.ForeignKey('Doctor',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    hospital = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    doctor = models.ForeignKey('Doctor',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Patient(User):
    profilepic=models.ImageField(upload_to="media/patients",null=True)
    patient_case=models.CharField(max_length=255)

    class Meta:
        pass