#! coding: utf-8
# Create your views here.
from django import forms
from django.forms import ValidationError
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

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        question = Question.objects.filter(pk=question_id).first()
        if not question:
            raise form.ValidationError(u'Вопроса не существует',code=14)
        return question
    def save(self):     
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.save()
        return answer        
