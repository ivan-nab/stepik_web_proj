
# Create your views here.
from django.http import HttpResponse 
from django.http import Http404 
from django.shortcuts import render 

from models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK',status=200)

def main_questions(request, *args, **kwargs):
    questions = Question.objects.all()
    return render(request, 'qa/main.html', {
        'questions': questions
    })