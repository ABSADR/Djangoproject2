from django.urls import path

from newarrivals import views

urlpatterns=[

    path('newarrivals/',views.something1,name='new_arrivals')
]