from django.db import models
from PIL import Image

class UpcomingGames(models.Model):
    title = models.CharField(max_length=100,unique=True)
    platform = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/',default='/staticfiles/images/pending.jpg')
    release_date = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height >300 and img.width>157:
            output_size = (100,150)
            img.thumbnail(output_size)
            img.save(self.photo.path) 
