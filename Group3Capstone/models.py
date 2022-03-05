from django.db import models


# Create your models here.
class AccountType(models.TextChoices):
   Administrator = 'A'
   User = 'U'


class User(models.Model):
   User_ID = models.BigAutoField(primary_key=True)
   User_Password = models.CharField(max_length=20, unique=True, blank=True)
   User_FName = models.CharField(max_length=40, null=True)
   User_LName = models.CharField(max_length=40, null=True)
   User_DOB = models.DateField(auto_now=False, auto_now_add=False, null=True)
   User_Address = models.CharField(max_length=100, null=True)
   User_Phone = models.IntegerField(null=True)
   UserName = models.CharField(max_length=40, null=True)
   User_Email = models.CharField(max_length=40, null=True)
   Account_type = models.CharField(max_length=1, choices=AccountType.choices, default=AccountType.Administrator)


class Sport(models.Model):
   Sport_Id = models.BigAutoField(primary_key=True)
   Sport_Name = models.CharField(max_length=40, null=True)  # just the name....


class Group(models.Model):
   Group_Id = models.BigAutoField(primary_key=True)
   Sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)
   Creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Location(models.Model):
   Location_Id = models.BigAutoField(primary_key=True)  # just a name
   Location_Name = models.CharField(max_length=40, null=True)
   Location_Address = models.CharField(max_length=40, null=True)


class Event(models.Model):
   Event_Id = models.BigAutoField(primary_key=True)
   Creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   Group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
   Date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
   Location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


class Reservation(models.Model):
   Reservation_Id = models.BigAutoField(primary_key=True)
   User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   Event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)



#class Sports(models.Model):
#       name = models.CharField(max_length = 20) #just the name....

#class Location(models.Model):
#       location = models.CharField(max_length=30) #just a name

#class Events(models.Model):
#     events = models.CharField(max_length = 30) #if want anything else add it

class Admin(User):
   pass

