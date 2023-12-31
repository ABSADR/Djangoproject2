from django.urls import path

from userextend import views

urlpatterns=[

    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('profile/', views.user_profile_redirect, name='user_profile'),
    path('edit-user/',views.edit_user, name='edit_user'),
    path('list-of-users/',views.UserListView.as_view(), name='list_of_users'),
    path('edit-profile/,', views.edit_profile, name='edit_profile'),

]


# path('profile/<str:username>/', views.user_profile_redirect, name='user_profile')