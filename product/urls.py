from django.urls import path

from product import views

urlpatterns=[

    path('products/',views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
]