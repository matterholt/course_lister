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