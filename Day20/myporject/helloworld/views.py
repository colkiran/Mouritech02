from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, "home.html", {'gname': 'Sachin Tendulkar'})

def greetings(request):
    return render(request, "home.html", {'gname': "Rahul Dravid"})