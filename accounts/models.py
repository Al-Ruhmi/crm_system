

from django.db import models
from django.contrib.auth.models import AbstractUser,User
from .manager import UserManager


# Create your models here.
class User(AbstractUser):
    email   = models.EmailField(unique=True,max_length=255)
    username  = models.CharField(max_length=255)
    
    
    full_name  = models.CharField(unique=True,max_length=255) #max_length=1024,
    active   = models.BooleanField(default=True)
    staff   = models.BooleanField(default=False)
    admin   = models.BooleanField(default=False)
    confirm  = models.BooleanField(default=False)
    confirmed_date= models.DateTimeField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['full_name']
    objects = UserManager()

    def __str__(self):
        return self.full_name


