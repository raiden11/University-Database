from __future__ import unicode_literals

from django.db import models


BT = 'B.Tech'
MT = 'M.Tech'
PHD = 'Ph.D'
MBA = 'MBA'

CO = 'Computer Science'
EE = 'Electrical'
EC = 'Electronics and Communications'
CE = 'Civil'
ME = 'Mechanical'
BIO = 'Biotech'
NONE = 'None'


AllCourse = (
    (BT, 'B.Tech'),
    (MT, 'M.Tech'),
    (PHD, 'Ph.D'),
    # (MBA, 'MBA'),
)

AllBranch = (
    (CO, 'Computer Science'),
    (EE, 'Electrical'),
    (EC, 'Electronics and Communications'),
    (CE, 'Civil'),
    (ME, 'Mechanical'),
    (BIO, 'Biotech'),
    (NONE, 'None'),
)


class Course(models.Model):

    CourseName = models.CharField(max_length=100, choices=AllCourse,
                                  blank=True, null=True)

    BranchName = models.CharField(max_length=100,
                                  choices=AllBranch, default='None',
                                  blank=True, null=True)
    HOD = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):

        if self.CourseName == 'Ph.D':
            return self.CourseName + ' : ' + self.BranchName
        else:
            return self.CourseName + ' : ' + self.BranchName + ' Engineering'
















