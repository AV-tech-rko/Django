from django.db import models
from PIL import Image



class Ratings(models.Model):
    Title = models.CharField(max_length=100,unique=True)
    Release_year = models.IntegerField()
    MyRating = models.FloatField(max_length=100,null=True,blank=True)
    UserRating = models.FloatField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/',default='/staticfiles/images/pending.jpg')
    description = models.CharField(max_length=1000,null=True,blank=True)
    details = models.TextField(max_length=1000,null=True,blank=True)
    
    
    

    def __str__(self):
        return self.Title
        #return 'Title: ' + self.Title + ' '+'|' + ' '+ 'MyRating: '+ str(self.MyRating)

         

class GameofYear(models.Model):
    title = models.CharField(max_length=50,unique=True)
    year = models.IntegerField(max_length=100)
    photo = models.ImageField(upload_to='images/',default='pending.jpg')
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title

       

     

       
