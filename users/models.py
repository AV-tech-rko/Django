from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='images/', default ='images/pending.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height >300 and img.width>157:
            output_size = (300,157)
            img.thumbnail(output_size)
            img.save(self.image.path)    