# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
   
    portfolio_site=models.URLField(max_length=200, blank=True)
    profile_pic=models.ImageField(upload_to='media/images', blank=True)
    Name=models.CharField(max_length=12)
    email=models.EmailField()
    Contact=models.CharField(max_length=12)
    Address=models.CharField(max_length=12)

user = models.OneToOneField(User,on_delete=models.CASCADE)
Name=models.CharField(max_length=12)
portfolio_site = models.URLField(blank=True)
email=models.EmailField()
profile_pic = models.ImageField(upload_to='media/images',blank=True)
Contact=models.CharField(max_length=12)
Address=models.CharField(max_length=12)
def __str__(self):
  return self.user.username