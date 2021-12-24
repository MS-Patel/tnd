from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(default=456)
    is_active=models.BooleanField(default=True)
    is_varfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    first_time_login=models.BooleanField(default=False)
    a_ddress1 = models.CharField(max_length=255, blank=True)