from django.shortcuts import render,redirect
from django.http import HttpResponse
from userPlus.models import Logo
from inet.models import SubSectionDetails,GrowSubSection



def SubGrowDetails(request,sub_section):
   grow = SubSectionDetails.objects.filter(sub_section_id=sub_section)

   logo = Logo.objects.all().first()
   details = dict()
   details['grow'] = grow
   details['logo'] = logo
   return render(request,'subgrowdetails.html',{"logo": details})


