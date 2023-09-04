from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def best_sellers(request):
    return render(request, 'bestsellers/bestsel.html')