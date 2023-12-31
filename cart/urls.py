from django.urls import path

from cart import views

app_name = 'cart'
urlpatterns=[

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('update_cart_item_quantity/', views.update_cart_item_quantity, name='update_cart_item_quantity'),


]