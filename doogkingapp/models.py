from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    user_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street_number = models.IntegerField()

class Housing(models.Model):
    house_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=50)
    street_number = models.IntegerField()
    house_dimension = models.IntegerField()
    house_owner = models.ForeignKey(User, on_delete=models.CASCADE)
