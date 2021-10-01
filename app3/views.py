from django.http.response import HttpResponse
from pro_2.settings import TEMPLATES
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    return HttpResponse('Welcome to baabte')

def loginfun(request):
    return render(request,'login.html')

def profilefun(request):
    return render(request,'profile.html')    
