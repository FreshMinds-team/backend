from django.db import models
from user.models import *

class Chat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    receiver = models.CharField(max_length= 200 ,null=True)
    message = models.TextField(null=True)
    room = models.CharField(max_length= 200 ,null=True)
    author = models.CharField(max_length= 200 ,null=True)
    time = models.DateTimeField(null=True)