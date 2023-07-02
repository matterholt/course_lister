# from django.shortcuts import render

from courseLister_api.models import CourseList
from courseLister_api.serializers import CourseListSerializer

from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class coursesList(generics.ListCreateAPIView):
    queryset = CourseList.objects.all()
    serializer_class = CourseListSerializer


class coursesList_singles(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseList.objects.all()
    serializer_class = CourseListSerializer