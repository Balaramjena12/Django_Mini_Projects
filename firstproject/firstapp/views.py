from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    s = '<h1>Hello Student Welcome To Mahesh Sir django Classes<h1>'
    return HttpResponse(s)
