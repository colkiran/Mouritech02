from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request, "ssnwelcome.html", {'gname' : 'Sourav Ganguly'})


def setsession(request):
    request.session['prdname'] = 'NIKE'
    request.session['product'] = 'JERSY'
    return render(request, 'setSession.html')

def getsession(request):
    pname = request.session['prdname']
    prod = request.session['product']
    key = request.session.keys()
    item = request.session.items()
    prc = request.session.setdefault('price', 5250.00)
    return render(request, 'getSession.html', {'prdname': pname, 'product': prod, 'keys':key, 'item': item, 'price':prc})

def deletesession(request):
    if 'prdname' in request.session:
        request.session.clear()
    return render(request, 'delSession.html')

def setssntime(request):
    request.session['pname'] = 'Reebok'
    request.session.set_expiry(0)
    return render(request, 'setssntime.html')

def getssntime(request):
    pname = request.session['pname']
    return render(request, "getssntime.html", {'prdname': pname})

def deletessntime(request):
    request.session.flush()
    return render(request, 'delssntime.html')