from django.shortcuts import render,redirect
from userPlus.models import Logo
from django.http import HttpResponse

def basic(request):
   logo = Logo.objects.all().first()
   print("this is logo",logo)
   print(logo.__dict__)
   return render(request,'basics.html', {"logo": logo})
