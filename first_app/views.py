from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Hello everyone, this is my home page<h1>")


def about(request):
    return HttpResponse("<h1>Hello everyone, this is my about page<h1>")
