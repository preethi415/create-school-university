from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_school(request):
    if request.method=='POST':
        sName=request.POST['sn']
        return HttpResponse(sName)

    return render(request,'create_school.html')
