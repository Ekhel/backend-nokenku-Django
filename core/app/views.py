from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request,'app/dashboard.html')

def dashboard(request):
    return render(request, 'app/dashboard')
