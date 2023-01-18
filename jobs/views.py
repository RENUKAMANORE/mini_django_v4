from django.shortcuts import render,HttpResponse
from .models import Portal

# Create your views here.
def welcome(request):
    return HttpResponse("<h1> welcome to our project </h1>")

def portal_details(request):
    objs = Portal.objects.all()
    portals = []
    for obj in objs:
        portals.append(obj.name)

    final = "=====".join(portals)
    return HttpResponse(f"<p> {final} </p>")
