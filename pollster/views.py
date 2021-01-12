from django.shortcuts import render,get_object_or_404
from .models import *
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request,'pollster/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'pollster/detail.html',{'question': question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'pollster/result.html',{'question': question})    

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'pollster/detail.html',{'question' : question, 'error_message' : "You didnt select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('pollster:results',args=(question.id,)))        


