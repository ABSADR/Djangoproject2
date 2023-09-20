from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product


# Create your views here.
def new_arrivals(request):
    new_products = Product.objects.order_by('-created_at')[:5] #Im getting the latest 5 products

    return render(request, 'newarrivals/new_arrivals.html', {'new_products':new_products})