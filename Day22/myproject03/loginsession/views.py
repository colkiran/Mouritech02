from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request, "home.html", {'gstname': 'Mike Tyson'})

def login(request):
    if 'gstuser'in request.session:
        return render(request, "home.html", {'gstname': request.session['gstuser']})
    return render(request, "login.html")


def add(request):
    if request.method == 'POST':
        usrName = request.POST['nm']
        request.session['gstuser'] = usrName
        request.session.set_expiry_at_browser_close = False
        request.session.set_expiry(datetime.timedelta(seconds=60))
        return render(request, "home.html", {'gstname': request.POST['nm']})
    else:
        return render(request, "login.html")

def delsession(request):
    request.session.clear()
    return render(request, "delssn.html")