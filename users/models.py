from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pro_pic = models.ImageField(default='media/pro.png')

