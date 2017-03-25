
# Create your views here.
from django.http import HttpResponse 
from django.http import Http404 
from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK',status=200)

def paginate(request, objects):
    try:
        limit = int(request.GET.get('limit',10))
    except ValueError:
        limit = 10
    if limit > 100 or limit < 0:
        limit = 10
    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404
    paginator = Paginator(objects,limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def main_questions(request, *args, **kwargs):
    questions = Question.objects.new()
    questions = paginate(request,questions)
    return render(request, 'qa/main.html', {
        'questions': questions
    })

def popular_questions(request, *args, **kwargs):
    questions = Question.objects.popular()
    questions = paginate(request,questions)
    return render(request, 'qa/main.html',{
        'questions': questions
    })

def question_answers(request,*args,**kwargs):
    question_id = args[0] 
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'qa/question.html',{
        'question': question
    })
