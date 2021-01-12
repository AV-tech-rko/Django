from django import forms
from django.forms import ModelForm
from .models import *
    
class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ('Title','Release_year','UserRating')
        
