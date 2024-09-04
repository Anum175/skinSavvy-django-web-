# models.py
from django.db import models
from django.contrib.auth.models import User

class Extra(models.Model):
    pid = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.pid.username


# models.py

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
