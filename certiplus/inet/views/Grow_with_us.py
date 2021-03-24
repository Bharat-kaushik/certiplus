from django.shortcuts import render,redirect
from django.http import HttpResponse
from userPlus.models import Logo
from inet.models import GrowSubSection



def SubGrow(request,section):

   grow = GrowSubSection.objects.filter(section=section)
   print(grow)
   if len(grow)>=1:
      logo = Logo.objects.all().first()
      details = dict()
      details['grow'] = grow
      for i in details['grow']:
         print(i.id)
      details['logo'] = logo
      return render(request,'SubGrow.html',{"logo": details})
   else:
      raise Exception("not find any grow section")