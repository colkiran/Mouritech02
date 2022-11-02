from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProductDetails
from .models import Product

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = ProductDetails(request.POST)
        if fm.is_valid():
            pid = fm.cleaned_data['Prodid']
            pnm = fm.cleaned_data['Prodname']
            cat = fm.cleaned_data['Category']
            pty = fm.cleaned_data['Prodtype']
            prc = fm.cleaned_data['Price']
            reg = Product(Prodid=pid, Prodname=pnm, Category=cat, Prodtype=pty, Price=prc)
            reg.save()
            fm = ProductDetails()
    else:
        fm = ProductDetails()
    stud = Product.objects.all()
    return render(request, 'add.html', {'form': fm, 'stu':stud})

def update_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        fm = ProductDetails(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductDetails(instance=pi)
    return render(request, "update.html", {'form': fm})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")