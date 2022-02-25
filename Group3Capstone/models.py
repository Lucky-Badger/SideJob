from django.db import models

# Create your models here.
class AccountType(models.TextChoices):
    Administrator='A'
    User='U'

class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices=AccountType.choices, default=AccountType.Administrator)


class Sports(models.model):
        name = models.CharField(max_length = 20) #just the name....

class Location(models.model):
        location = models.CharField(max_length=30) #just a name

class Events(models.model):
        events = models.CharField(max_length = 30) #if want anything else add it

class Admin(User):
    pass