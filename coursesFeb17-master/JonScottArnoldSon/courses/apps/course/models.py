from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True, related_name='course_id')
    description = models.TextField(max_length=1000)
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, related_name='c_id')


# class Course(models.Model):
#     course_name = models.CharField(max_length=255)
#     description = models.TextField(max_length=1000)
#     date_added = models.DateTimeField(auto_now_add=True)