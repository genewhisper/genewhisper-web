from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username


class Company(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    company_url = models.URLField(blank=True)
    company_phone_number = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.company_name
