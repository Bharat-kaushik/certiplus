from django.shortcuts import render,redirect
from django.http import HttpResponse
from userPlus.models import Logo
from inet.models import GrowSubSection



def SubGrow(request,section):
   print(section)
   grow = GrowSubSection.objects.all()
   logo = Logo.objects.all().first()
   details = dict()
   details['grow'] = grow
   print(details['grow'][0].section)
   details['logo'] = logo
   return render(request,'SubGrow.html',{"logo": details})