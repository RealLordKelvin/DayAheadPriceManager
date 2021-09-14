from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Price(models.Model):
    
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=30)

    class Meta:

        verbose_name_plural = 'Data'

class UserInfo(AbstractBaseUser):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserInfo, self).save(*args, **kwargs)

    class Meta:

        verbose_name_plural = 'Userinformation'
