
# Create your views here.
from django.http import HttpResponse 
from django.http import Http404 
from django.shortcuts import render 
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK',status=200)

def main_questions(request, *args, **kwargs):
    questions = Question.objects.new()
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions,limit)
    paginator.baseurl = "/?page="
    page = paginator.page(page)
    return render(request, 'qa/main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })