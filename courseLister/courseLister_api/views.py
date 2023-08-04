# from django.shortcuts import render

from courseLister_api.models import CourseSummary
from courseLister_api.models import LessonDetails
from courseLister_api.serializers import CourseListSerializer
from courseLister_api.serializers import LessonDetailsSerializer
from courseLister_api.serializers import CombinedModelSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class coursesList(generics.ListCreateAPIView):
    queryset = CourseSummary.objects.all()
    serializer_class = CourseListSerializer


class coursesList_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonDetails.objects.all()

    serializer_class = LessonDetailsSerializer


class CombinedModelListView(APIView):
    def get(self, request):
        model_a_data = CourseSummary.objects.all()
        model_b_data = LessonDetails.objects.all()

        combined_data = {
            "model_a": CourseListSerializer(model_a_data, many=True).data,
            "model_b": LessonDetailsSerializer(model_b_data, many=True).data,
        }

        return Response(combined_data)


# class CombinedModelListView(generics.ListAPIView):
#     serializer_class = CombinedModelSerializer

#     def get_queryset(self):
#         model_a_data = CourseSummary.objects.all()
#         model_b_data = LessonDetails.objects.all()

#         combined_data = {
#             "model_a": model_a_data,
#             "model_b": model_b_data,
#         }

#         return combined_data
