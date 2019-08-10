from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Nelayan, Hasil_laut

@login_required
def index(request):
    return render(request,'app/dashboard.html')


@login_required
def datanelayan(request):
    contex = {
        'item':Nelayan.objects.all()
    }
    return render(request,'app/data-nelayan.html',contex)


@login_required
def hasillaut(request):
    contex = {
        'item':Hasil_laut.objects.all()
    }
    return render(request, 'app/hasil-laut.html',contex)

    
