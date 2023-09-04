from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def something1(request):
    return HttpResponse('NEWSS')