from rest_framework import serializers
from courseLister_api.models import CourseSummary
from courseLister_api.models import LessonDetails


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSummary
        fields = ["id", "created", "title", "description", "author", "subject_matter"]


class LessonDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDetails
        fields = ["title", "chapter_number", "description", "course_id"]
