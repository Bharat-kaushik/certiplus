from django.shortcuts import render,redirect
from django.http import HttpResponse
from userPlus.models import Logo
def Home(request):
   logo = Logo.objects.all()[0]
   return render(request,'home.html',{"logo": logo})