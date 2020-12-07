from django.shortcuts import render
from acounts.models import UserProfileInfo
from django.db.models import CharField, Count
from django.db.models import Avg, Max, Min,F
from home.models import dataguru, datamurid
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import login_required
# from django.conf import settings


# Create your views here.

# @login_required(login_url=settings.LOGIN_URL)
def hoe(request):
    dt = dataguru.objects.all()
    return render(request, 'vfrondend/index.html',{ 
        'data' : dt,
    })   
    
    # dtgr = dataguru.objects.all()
    # usr = UserProfileInfo.objects.filter(user=request.user.id)
    # data = {
    #     'nuser': usr,
    #     'data':dtgr,
    #     'test': x
    #     # 'testy': y
    # }
    # return render(request, 'vfrondend/index.html',data)

def about(request):
    return render(request, 'vfrondend/about.html')

def guru(request):
    return render(request, 'vfrondend/guru.html')