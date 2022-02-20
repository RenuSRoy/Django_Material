from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'hello.html')

def Next(request):
    return render(request,"Next.html")

def Third_Page(request):
    return render(request,"Third_Page.html")



# Create your views here.
