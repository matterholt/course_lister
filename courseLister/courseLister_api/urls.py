from django.urls import path , include
from courseLister_api import views

urlpatterns =[
    path('course/', views.coursesList_all),
    path('course/', views.coursesList_details)
]