from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse ('<h1>Hello {}!<h1>'.format(nome))