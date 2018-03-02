from django.core.management import templates
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm

from django.template import RequestContext, loader
from quiz.models import Person




def index(request):





    return render(request, "index.html", data)


def viewtwo(request):

    data = {'name': 'Bony'}

    data['bokachuda'] = 'Mustafiz'


    return render(request, "Home.html", data)