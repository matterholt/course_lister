from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns
from courseLister_api import views

urlpatterns =[
    path('courselist/', views.coursesList.as_view()),
    path('courselist/<int:pk>/', views.coursesList_singles.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)