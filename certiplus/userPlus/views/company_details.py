from django.shortcuts import render,HttpResponse
from userPlus.forms import ComapanyDetails
import uuid


def companyDetails(request):
    if request.method == 'POST':
        form = ComapanyDetails(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.key = str(uuid.uuid4())[0:10]

            company.save()
            return render(request, 'success.html', {'success': "You have successfully added your company details"})
    else:
        form = ComapanyDetails()
        return render(request, 'companydetailsform.html', {'form': form})