from django.http import HttpResponse
from django.shortcuts import redirect, render

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

