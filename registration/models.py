import datetime

from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError

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
        return u"{}".format(self.short_name,)


@py3_compat
class Program(models.Model):
    title = models.CharField(max_length=60)
    major = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    short_name = models.CharField(max_length=30)
    department = models.ForeignKey('Department')

    def __unicode__(self):
        return u"{}".format(self.short_name)


class Student(person.Person):
    GRADE_SCHOOL_LEVEL = 1
    HIGH_SCHOOL_LEVEL = 2
    COLLEGE_LEVEL = 3
    GRADUATE_LEVEL = 4
    DOCTORATE_LEVEL = 5
    LEVEL_CHOICES = (
        (GRADE_SCHOOL_LEVEL, "Grade School"),
        (HIGH_SCHOOL_LEVEL, "High School"),
        (COLLEGE_LEVEL, "College"),
        (GRADUATE_LEVEL, "Graduate"),
        (DOCTORATE_LEVEL, "Doctorate"),
    )
    NEW_ENROLLMENT = 1
    OLD_ENROLLMENT = 2
    RETURNEE_ENROLLMENT = 3
    CROSS_ENROLLMENT = 4
    ENROLLMENT_TYPES = (
        (NEW_ENROLLMENT, 'New'),
        (OLD_ENROLLMENT, 'Old'),
        (RETURNEE_ENROLLMENT, 'Returnee'),
        (CROSS_ENROLLMENT, 'Cross-Enrollee'),
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
    # can a student take more than one program
    program = models.ForeignKey('Program',
                                null=True,
                                blank=True,
                                limit_choices_to={'department':
                                                  F('department'), })

    def clean(self):
        super(Student, self).clean()

        if self.school_level < self.HIGH_SCHOOL_LEVEL:
            self.program = None
        else:
            if self.program is None:
                raise ValidationError({'program':
                                       "Program is required for college " +
                                       "and higher levels"})


class Guardian(person.Person):
    YES_NO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    occupation = models.CharField(max_length=30, default='')
    relationship = models.CharField(max_length=30, default='Father')
    emergency_contact = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    ward = models.ForeignKey('Student', null=True)


class Subject(models.Model):
    short_name = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=60, default='')
    units = models.IntegerField(default=3)


@py3_compat
class Semester(models.Model):
    name = models.CharField(max_length=30, default='')
    series = models.IntegerField(default=0)

    class Meta:  # E302
        ordering = ['series', 'name']

    def __unicode__(self):
        return u"{}".format(self.name)
