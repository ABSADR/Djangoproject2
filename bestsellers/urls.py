from django.urls import path

from bestsellers import views

urlpatterns=[

    path('bestsellers/', views.best_sellers, name='best_sellers'),
]