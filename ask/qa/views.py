
# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import Question, Answer
from forms import AskForm, AnswerForm

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
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question_id})
        answers = Answer.objects.filter(question=question).all()
        return render(request, 'qa/question.html',{
            'question': question,
            'answers': answers,
            'form': form
        })

def question_add(request, *args, **kwargs):
    user = User.objects.first()
    if request.method =="POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html',{
        'form': form
    })