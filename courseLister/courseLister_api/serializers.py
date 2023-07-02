from rest_framework import serializers
from courseLister_api.models import CourseList


class CourseListSerializer (serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = ['created','title','description','author','link', 'subject']
