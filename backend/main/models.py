from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime
# Create your models here.

class MyUser(AbstractBaseUser):
    id = models.AutoField(unique=True)
    email = models.EmailField(max_length=90, 
                              unique=True)
    password = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    lastName = models.CharField(max_length=100)

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.email}"


class Announcements(models.Model):
    ann_id = models.AutoField(unique=True)
    title = models.CharField(max_length=90)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    cathegorires = models.TextField()
    explanation = models.TextField()
    images = models.TextField()

    def __str__(self):
        return f"{self.title}"