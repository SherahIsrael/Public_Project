from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def events(request):
    template = loader.get_template('myFirst.html')
    return HttpResponse(template.render())
