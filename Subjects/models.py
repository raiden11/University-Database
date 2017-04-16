from __future__ import unicode_literals

from django.db import models
from Courses.models import Course


class Subject(models.Model):

    Course = models.ForeignKey(Course, blank=True, null=True)
    SubjectName = models.CharField(max_length=200, blank=True, null=True)
    SubjectCode = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.SubjectCode








