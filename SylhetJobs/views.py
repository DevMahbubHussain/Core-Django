from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.   

def syljobs(request):
    date = datetime.datetime.now()
    mydict = {'date_msg':date}
    return render(request,'SylhetJobs/wish.html',context=mydict)

def dhakajobs(request):
    s ="<h1>Dhaka Jobs</h1>"
    return HttpResponse(s)

def cumillajobs(request):
    s ="<h1>Cumila Jobs</h1>"
    return HttpResponse(s)
