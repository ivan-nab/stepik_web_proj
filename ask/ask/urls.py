"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:
  url(r'^blog/', include('blog.urls'))
"""
import os.path
import sys
from django.conf.urls import url
from django.contrib import admin
BASE_MODULE_DIR = os.path.dirname(__file__)
BASE_MODULE_DIR = os.path.dirname(BASE_MODULE_DIR)
sys.path.insert(0,BASE_MODULE_DIR)
from qa import views
 
urlpatterns = [
    url(r'^$', views.main_questions, name='main_questions'),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^admin/$', admin.site.urls),
    url(r'^question/(\d+)/$', views.question_answers, name='question'),
    url(r'^ask/$', views.question_add, name='question_add'),
    url(r'^popular/$', views.popular_questions, name='popular_questions'),
    url(r'^new/$', views.test),
]
