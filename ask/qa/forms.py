# Create your views here.
from django import forms
from django.http import HttpResponse 
from django.http import Http404 
from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from models import Question, Answer
from datetime import datetime

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, **kwargs):
        self._user = user
        super(AskForm,self).__init__(**kwargs)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question