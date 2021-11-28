from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    """docstring for User."""
    is_agent = models.BooleanField('Is Agent', default=False)
    is_user = models.BooleanField('Is User', default=False)
    is_agency = models.BooleanField('Is Agency', default=False)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='profile_pics')
#
#     def __str__(self):
#         return f'{self.user.username} profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

# default='default.jpg',
