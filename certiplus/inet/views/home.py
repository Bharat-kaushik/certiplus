from django.shortcuts import render,redirect
from django.http import HttpResponse
from userPlus.models import Logo
from inet.models import GrowSection



def Home(request):
   grow = GrowSection.objects.all()
   logo = Logo.objects.all().first()

   details = dict()
   details['grow'] = grow
   details['logo'] = logo
   return render(request,'home.html',{"logo": details})