from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse('HOME PAGE')

def About(request):
    return HttpResponse('About PAGE')
    
def Contact(request):
    return HttpResponse('Contact PAGE')