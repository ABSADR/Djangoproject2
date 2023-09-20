from django.urls import path

from newarrivals import views

urlpatterns=[

    path('newarrivals/',views.new_arrivals ,name='new_arrivals')
]