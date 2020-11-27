from django.db import models

class User(models.Model):
    Email = models.CharField(max_length=60)
    PhoneNumber = models.CharField(max_length=60)
    Name = models.CharField(max_length=60)
    Password = models.CharField(max_length=60)