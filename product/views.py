from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from product.forms import ProductForm, ProductSearchForm
from product.models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
@permission_required('product.add_product')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})


def product_search(request):
    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            products = Product.objects.filter(name__icontains=search_query)
            return render(request, 'product_search_results.html', {'products': products})
        else:
            form = ProductSearchForm()
        return render(request, 'product_search.html', {'form':form})


def product_search_bar(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'product_search_results.html', {'products': products})
