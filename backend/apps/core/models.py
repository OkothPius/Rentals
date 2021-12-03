from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    estate = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.estate}'

class Rental(models.Model):
    name = models.CharField(max_length=100)
    rent = models.IntegerField()
    house_detail = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

        # Handles redirect
    def get_absolute_url(self):
        return reverse('rental')

class Sale(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    house_detail = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

        # Handles redirect
    def get_absolute_url(self):
        return reverse('rental')
