# from django.shortcuts import render

from courseLister_api.models import CourseSummary
from courseLister_api.models import LessonDetails
from courseLister_api.serializers import CourseListSerializer
from courseLister_api.serializers import LessonDetailsSerializer

from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class coursesList(generics.ListCreateAPIView):
    queryset = CourseSummary.objects.all()
    serializer_class = CourseListSerializer


class coursesList_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonDetails.objects.all()
    serializer_class = LessonDetailsSerializer
