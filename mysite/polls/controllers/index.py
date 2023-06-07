from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Product
from polls.models import Item

def index(request):
    return render(request, 'index.html', {})

def frames(request):
    return render(request, 'frames.html', {})

def sunglasses(request):
    return render(request, 'sunglasses.html', {})

def lenses(request):
    return render(request, 'lenses.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def frames(request):
    product = Product.objects.all()
    return render(request, 'frames.html', {'products': product})

def sunglasses(request):
    item = Item.objects.all()
    return render(request, 'sunglasses.html', {'items': item})
