from django.urls import path

from userextend import views

urlpatterns=[

    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('profile/', views.user_profile_redirect, name='user_profile'),
]


# path('profile/<str:username>/', views.user_profile_redirect, name='user_profile')