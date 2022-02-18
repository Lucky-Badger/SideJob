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

class Admin(User):
    pass