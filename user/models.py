from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    User_Role = [('Patient','Patient'),('Doctor','Doctor')]
    GENDER = [('Male','Male'),('Female','Female')]
    user_type=models.CharField(max_length=8,choices=User_Role,default='Patient')
    profilepic=models.ImageField(null=True)
    dob=models.DateField()
    gender=models.CharField(max_length=6,choices=GENDER,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)


