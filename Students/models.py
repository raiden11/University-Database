from __future__ import unicode_literals

from django.db import models
from Courses.models import Course
from Subjects.models import Subject


class Student(models.Model):

    RollNo = models.CharField(max_length=50, unique=True)
    Name = models.CharField(max_length=200, blank=True)
    DateOfBirth = models.DateField(null=True, blank=True)
    # PhoneNo = models.IntegerField(null=True, blank=True)
    Course = models.ForeignKey(Course, blank=True, null=True, default=1)
    Subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.RollNo







