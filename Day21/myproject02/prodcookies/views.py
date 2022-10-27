from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request, 'cookiehome.html', {'gname': 'Sachin Tendulkar'})

def setcookie(request):
    response = render(request, 'setcookie.html')
    response.set_cookie('prdname', 'adidas', max_age=datetime.timedelta(seconds=30))
    return response

def getcookie(request):
    pname = request.COOKIES['prdname']
    return render(request, "getcookie.html", {'prdname' : pname})

def deletcookie(request):
    response = render(request, "deletecookie.html")
    response.delete_cookie('prdname')
    return response


