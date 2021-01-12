from django.shortcuts import render,redirect
from .models import *

def upgames(request):
    upgames = UpcomingGames.objects.all()

    context = {
        'upgames' : upgames
    }

    return render(request,'UpcomingGames/home.html',context)
