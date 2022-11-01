from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import ProfileManager


class Profile(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    otp = models.CharField(max_length=32, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return self.email


class Housing(models.Model):
    house_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=25)
    floor = models.CharField(max_length=25, blank=True)
    door = models.CharField(max_length=25, blank=True)
    house_dimension = models.IntegerField()
    house_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return " ".join([self.city, self.street, self.street_number])
