from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    """docstring for User."""
    is_admin = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
