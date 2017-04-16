from __future__ import unicode_literals

from django.db import models
from Students.models import Student


FOOT = 'Football'
CRI = 'Cricket'
VOLLEY = 'Volleyball'
BASKET = 'Basketball'
TEN = 'Tennis'
BAD = 'Badminton'
CHESS = 'Chess'
NONE = 'None'


AllSport = (            # Add categories here
    (FOOT, 'Football'),
    (CRI, 'Cricket'),
    (VOLLEY, 'Volleyball'),
    (BASKET, 'Basketball'),
    (TEN, 'Tennis'),
    (BAD, 'Badminton'),
    (CHESS, 'Chess'),
    (NONE, 'None'),
)


class Sports(models.Model):

    class Meta:
        verbose_name_plural = "Sports : Items Issued"

    IssueID = models.OneToOneField(Student, unique=True)
    # onetoonefield is used for foreignkey constraint + unique

    SportsName = models.CharField(max_length=100,
                                  choices=AllSport,
                                  blank=True, null=True,
                                  default='None')

    NumberOfItems = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.IssueID.RollNo


class Library(models.Model):

    class Meta:
        verbose_name_plural = "Library : Books Issued"

    IssueId = models.OneToOneField(Student, unique=True)

    BookName = models.CharField(max_length=200, blank=True, null=True)

    RenewalsLeft = models.SmallIntegerField(blank=True, null=True, default=3)

    # for issue date and return date ??

    def __str__(self):
        return self.IssueId.RollNo




















