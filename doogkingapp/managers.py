from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re


class ProfileManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        #if not validate_email(email):
            #raise ValueError('The email is not correct')

        if not re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email):
            raise ValueError('The email is not correct')
        if not len(password) > 8:
            raise ValueError('Password length should be at least 8')

        if not any(char.isdigit() for char in password):
            raise ValueError('Password should have at least one number')

        if not any(char.isupper() for char in password):
            raise ValueError('Password should have at least one uppercase letter')

        if not any(char.islower() for char in password):
            raise ValueError('Password should have at least one lowercase letter')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Admin must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

