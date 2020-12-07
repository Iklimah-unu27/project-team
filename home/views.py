from django.shortcuts import render
from acounts.models import UserProfileInfo
from django.db.models import CharField, Count
from django.db.models import Avg, Max, Min,F
from home.models import dataguru, datamurid
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def Htampil(request):
    if request.user.is_authenticated:

        #x=UserProfileInfo.objects.aggregate(Max('nodata'))
        #y=x.objects.annotate(diff=F(x) + F(1))

        dtgr = dataguru.objects.all()
        usr = UserProfileInfo.objects.filter(user=request.user.id)
        data = {
            'nuser': usr,
            'data':dtgr,
            # 'test': x
            # 'testy': y
           

        }
        return render(request, 'vhome/index.html',data)

def Hguru(request):
    return render(request, 'vhome/guru.html')

def Habout(request):
    return render(request, 'vhome/about.html')

def sd(request):
    return render(request, 'vhome/sd.html')

def smp(request):
    return render(request, 'vhome/smp.html')

def sma(request):
    return render(request, 'vhome/sma.html')

def form(request):
    if request.POST:
        models.datamasuk.objects.filter(pk=id).update(
        nama=request.POST['nama'],
        alamat=request.POST['alamat'],
        biaya=request.POST['biaya'],
        nohp=request.POST['nohp'],
        )
        return redirect('masuk')
    task = models.datamasuk.objects.filter(pk=id).first()
    return render(request, 'vhome/form.html',
    { 'data' : task,
    })
