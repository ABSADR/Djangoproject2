from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','image']


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)