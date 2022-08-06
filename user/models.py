from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class User(AbstractUser):
    username=models.CharField(max_length=20,unique=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=40,null=True)
    email=models.EmailField(null=True)
    GENDER = [('Male','Male'),('Female','Female'),('Other',"Other")]
    profilepic=models.ImageField(upload_to="media/",null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=6,choices=GENDER,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username

class Doctor(User,AbstractUser):
    experience=models.CharField(max_length=255)
    qualification=models.CharField(max_length=255)

    class Meta:
        pass

class Patient(User,AbstractUser):
    patient_case=models.CharField(max_length=255)

    class Meta:
        pass