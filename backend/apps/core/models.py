from django.db import models

class Rental(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    house_detail = models.TextField()
    pub_date = models.DateTimeField('date published')
    estate = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
