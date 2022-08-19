from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import random


class CustomUserManager(BaseUserManager):
    def create_user(self,email, password=None):
        if not email:
            raise ValueError("User must have an email address.")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email),
                                password=password,
                                )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    # Username=models.CharField(max_length=20,unique=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=14,null=True)
    active=models.BooleanField(default=True)
    address=models.CharField(max_length=27,null=True)
    TYPES = [('Patient','Patient'),('Doctor','Doctor')]
    type=models.CharField(max_length=27,choices=TYPES,null=True)
    GENDER = [('Male','Male'),('Female','Female'),('Other',"Other")]
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=6,choices=GENDER,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    class Meta:
        pass

    def __str__(self):
        return self.username

class Doctor(User):
    description=models.TextField(max_length=1000,null=True)
    profilepic=models.ImageField(default='media/default.png',upload_to="media/doctor/"+str(random.randint(0, 9999)))
    class Meta:
        pass

class Qualification(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    date = models.DateField()
    doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Expertise(models.Model):
    title=models.CharField(max_length=255)
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE)


class Patient(User):
    profilepic=models.ImageField(default='media/default.png',upload_to="media/patients/"+str(random.randint(0, 9999)))
    patient_case=models.CharField(max_length=255,null=True)

    class Meta:
        pass

