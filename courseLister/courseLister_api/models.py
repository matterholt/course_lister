from django.db import models

# Create your models here.
# title:"",type:[], description:"",authors:[], link:"", publishDate:"", cost:""
class CourseList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=180, blank=True, default='')
    description =  models.CharField(max_length=180, blank=True, default='')
    author =  models.CharField(max_length=180, blank=True, default='')
    link =  models.CharField(max_length=180, blank=True, default='')
    subject =  models.CharField(max_length=180, blank=True, default='')

class CourseLesson(models.Model):
    title = models.CharField(max_length=180, blank=True, default='')
    chapter_number = models.CharField(max_length=180, blank=True, default='')
    page_start = models.CharField(max_length=180, blank=True, default='')
    url_link = models.CharField(max_length=180, blank=True, default='')
    course_id = models.ForeignKey(CourseList, default=None, on_delete = models.CASCADE, blank = True, null = True)

