from django.shortcuts import render
from .models import Products
from django.contrib import messages
from django import forms
from .forms import Prodform
# Create your views here.

def ProdDisp(request):
    result = Products.objects.all()
    return render(request, "index.html", {'products': result})

def AddProd(request):
    if request.method == 'POST':
        if request.POST.get('prdname') and request.POST.get('mnftr') and request.POST.get('cat') and request.POST.get('ptype') and request.POST.get('prc'):
            newprd = Products()
            newprd.prodname = request.POST.get('prdname')
            newprd.mnftr = request.POST.get('mnftr')
            newprd.category = request.POST.get('cat')
            newprd.prodtype = request.POST.get('ptype')
            newprd.price = request.POST.get('prc')
            newprd.save()
            messages.success(request, "The Record " + newprd.prodname + " saved successfully.....")
        return render(request, "AddProduct.html")
    else:
        return render(request, "AddProduct.html")

def EditProd(requests, id):
    getAllprod = Products.objects.get(id=id)
    return render(requests, "EditProd.html", {'products':getAllprod})


def UpdateProd(requests, id):
    updateProd = Products.objects.get(id=id)
    form = Prodform(requests.POST, instance=updateProd)
    if form.is_valid():
        form.save()
        messages.success(requests, "The product record is updated successfully......")
        return render(requests, "EditProd.html", {'products': updateProd})