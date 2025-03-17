from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyd_jobs_info(request):
    s = '<h1>Hyderabad Jobs Informations</h1>'
    return HttpResponse(s)
def bng_jobs_info(request):
    s = '<h1>Bangalore Jobs Informations</h1>'
    return HttpResponse(s)
def pune_jobs_info(request):
    s = '<h1>Pune Jobs Informations</h1>'
    return HttpResponse(s)
def bihar_jobs_info(request):
    s = '<h1>Bihar Jobs Informations</h1>'
    return HttpResponse(s)


        
