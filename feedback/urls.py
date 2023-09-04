from django.urls import path

from feedback import views

urlpatterns = [

 path('create-feedback/',views.FeedbackCreateViwe.as_view(),name='create_feedback'),
]