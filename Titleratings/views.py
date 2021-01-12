from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg

def index(request):
    list = Ratings.objects.all()
    list2 = GameofYear.objects.all().order_by('-year')
   

    

    form = RatingsForm()

    if request.method =='POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            form.save()
         
        

    context = {
        'list' : list,
        'list2' : list2,
        
        'form' : form
    }
    return render(request,'Titleratings/list.html',context)

def updateTask(request,pk):
    lists = Ratings.objects.get(id=pk)

    forms = RatingsForm(instance=lists)

    if request.method == 'POST':
        forms = RatingsForm(request.POST,instance=lists)
        if forms.is_valid():
            forms.save()
            return redirect('/ratings/')
    
    context = {
        'forms' : forms
    }


    return render(request,'Titleratings/update_task.html',context)

# def avgmean(request):
#     listnew = Ratings.objects.all().aggregate(Avg('UserRating'))   

#     context = {
#         'listnew' : listnew
#     }

#     return render(request,'Titleratings/list.html',context)

# def got(request):
#     gamelist = GameofYear.objects.all()

#     context = {
#         'gamelist' : gamelist,
#     }   

#     return render(request,'Titleratings/list.html',context) 