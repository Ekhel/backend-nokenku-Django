from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'app/dashboard.html')



    
