from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl)[0]
            SO.save()
            return HttpResponse('School is created..')
        else:
            return HttpResponse('Invalid data...')

    return render(request,'create_school.html',d)
