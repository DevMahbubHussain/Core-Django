from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.   

# def syljobs(request):
#     date = datetime.datetime.now()
#     mydict = {'date_msg':date}
#     return render(request,'SylhetJobs/wish.html',context=mydict)

def syljobs(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def dhakajobs(request):
    s ="<h1>Dhaka Jobs</h1>"
    return HttpResponse(s)

def cumillajobs(request):
    s ="<h1>Cumila Jobs</h1>"
    return HttpResponse(s)



def menuitems(request,dish):
    drink = {
    'mocha' : 'type of coffee',
    'tea' : 'type of hot beverage',
    'lemonade': 'type of refreshment'
    }

    choose_drink = drink[dish]
    return HttpResponse(f"<h2>{dish}</h2>"+choose_drink)
    
    