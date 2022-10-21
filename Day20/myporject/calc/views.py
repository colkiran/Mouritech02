from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html", {'gname': 'Kapil Dev'})

def arith(request):
    return render(request, 'add.html', {'bname': 'CASIO'})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST['num2'])
    val3 = val1 + val2
    return render(request, "add.html", {'res': val3, 'bname': 'CASIO'})
