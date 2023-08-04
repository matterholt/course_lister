from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from courseLister_api import views
from .views import CombinedModelListView

urlpatterns = [
    path("courselist/", views.coursesList.as_view()),
    path("courselist/<int:pk>/details", views.coursesList_details.as_view()),
    path("courselist/<int:pk>/combine", views.coursesList_details.as_view()),
    path("combined-models/", CombinedModelListView.as_view(), name="combined-models"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
