import datetime

from django.db import models
from django.db.models import F

import person
from compat import py3_compat


class Instructor(person.Person):
    INSTRUCTOR_TYPES = (
        (1, 'Full-time'),
        (2, 'Part-time'),
    )
    department = models.ForeignKey('Department', related_name='department')
    kind = models.IntegerField(verbose_name='Type', choices=INSTRUCTOR_TYPES)


@py3_compat
class Department(models.Model):
    TITLE_CHOICES = (
        (1, 'Dean'),
        (2, 'Principal'),
    )
    name = models.CharField(max_length=60, default='')
    short_name = models.CharField(max_length=30, default='')
    head = models.OneToOneField(Instructor,
                                null=True,
                                blank=True,
                                related_name='dean_or_principal',
                                limit_choices_to={'department__id': F('id'),
                                                  'kind': 1,
                                                  })
    head_title = models.CharField(max_length=30, default='Dean')

    def __unicode__(self):
        if self.head:
            return u"<{}:{}-{} {}>".format(type(self).__name__,
                                           self.short_name,
                                           self.head_title,
                                           self.head.fullname)

        else:
            return u"<{}:{}>".format(type(self).__name__,
                                     self.short_name,
                                     )


@py3_compat
class Program(models.Model):
    title = models.CharField(max_length=60)
    major = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    short_name = models.CharField(max_length=30)
    department = models.ForeignKey('Department')

    def __unicode__(self):
        return u"<{}: {}>".format(type(self).__name__, self.short_name)


class Student(person.Person):
    LEVEL_CHOICES = (
        (1, "Grade School"),
        (2, "High School"),
        (3, "College"),
        (4, "Graduate"),
        (5, "Doctorate"),
    )
    ENROLLMENT_TYPES = (
        (1, 'New'),
        (2, 'Old'),
        (3, 'Returnee'),
        (4, 'Cross-Enrollee'),
    )

    civil_status = models.CharField(max_length=20, default='Single')
    citizenship = models.CharField(max_length=30, default='Filipino')
    religion = models.CharField(max_length=30, default='Roman Catholic')
    birthdate = models.DateField(default=datetime.date.today)
    birthplace = models.CharField(max_length=100, default='')

    enrollment_type = models.IntegerField(choices=ENROLLMENT_TYPES, default=1)
    school_level = models.IntegerField(choices=LEVEL_CHOICES, default=2)
    year_level = models.IntegerField(default=1)
    id_number = models.CharField(max_length=20, default='', blank=True)
    department = models.ForeignKey('Department', null=True)
    program = models.ForeignKey('Program',
                                null=True,
                                limit_choices_to={'department':
                                                  F('department'), })


class Guardian(person.Person):
    YES_NO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    occupation = models.CharField(max_length=30, default='')
    relationship = models.CharField(max_length=30, default='Father')
    emergency_contact = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    ward = models.ForeignKey('Student', null=True)
