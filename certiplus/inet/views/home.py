from django.shortcuts import render,redirect
from django.http import HttpResponse
from userPlus.models import Logo
from inet.models import GrowSection,ContectSections



def Home(request):
   grow = GrowSection.objects.all()
   contect = ContectSections.objects.all()
   logo = Logo.objects.all().first()
   for i in grow:
      print(i.__dict__)
   details = dict()
   details['contect'] = contect
   details['grow'] = grow
   details['logo'] = logo
   return render(request,'home.html',{"logo": details})