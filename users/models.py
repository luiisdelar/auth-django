from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """ User model """

    username = models.CharField(
        max_length=150,
        unique=True,
        null=True
    )
    email = models.EmailField(max_length=250, unique=True, null=False)
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    company = models.CharField(max_length=250, blank=False, null=True)
    mobile_number = models.CharField(max_length=14, unique=True, blank=False, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_username(self):
        return self.email

    def __str__(self):
        return f'{self.first_name} {self.last_name}'