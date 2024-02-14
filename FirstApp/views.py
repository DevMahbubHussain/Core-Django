from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    s = '<h1>Welcome to Django Classess... Nurseary level concept</h1>'
    return HttpResponse(s)

def msg(request):
    ss = "<h2>Hi, How are you</h2>"
    return HttpResponse(ss)