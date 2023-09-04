from django.urls import path

from product import views

urlpatterns=[

    path('products/',views.product_list, name='product_list')
]