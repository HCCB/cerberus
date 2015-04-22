import datetime

from django.db import models
from django.db.models import F

from compat import py3_compat

ADDRESS_TYPES = (
    (1, 'Home'),
    (2, 'Work'),
    (3, 'Permanent'),
)

PHONE_TYPES = (
    (1, 'Home'),
    (2, 'Work'),
    (3, 'Mobile'),
    (4, 'Fax'),
    (5, 'Other'),
)

LEVEL_CHOICES = (
    (1, "Grade School"),
    (2, "High School"),
    (3, "College"),
    (4, "Graduate"),
    (5, "Doctorate"),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ENROLLMENT_TYPES = (
    (1, 'New'),
    (2, 'Old'),
    (3, 'Returnee'),
    (4, 'Cross-Enrollee'),
)

INSTRUCTOR_TYPES = (
    (1, 'Full-time'),
    (2, 'Part-time'),
)

YES_NO_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)


@py3_compat
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    name_suffix = models.CharField(max_length=10)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __unicode__(self):
        return "<{}:{}>".format(type(self).__name__, self.fullname)

    @property
    def fullname(self):
        """Get the fullname."""
        middle = self.middle_name[:1]
        if middle:
            middle = ' {}.'.format(middle)
        return "{}, {}{}".format(self.last_name, self.first_name, middle)

    class Meta:
        ordering = ['last_name', 'first_name', 'middle_name']


@py3_compat
class Address(models.Model):
    street1 = models.CharField(max_length=60, default='')
    street2 = models.CharField(max_length=60, default='')
    city = models.CharField(max_length=60, default='Butuan City')
    province = models.CharField(max_length=60, default='Agusan del Norte')
    zip = models.CharField(max_length=10, default='8600')
    kind = models.IntegerField(choices=ADDRESS_TYPES, default=1)

    owner = models.ForeignKey('Person')

    def __unicode__(self):
        return "<{}:{}-{}:{}>".format(type(self).__name__, self.owner.fullname,
                                      self.get_kind_display(), self.street1)


@py3_compat
class Phone(models.Model):
    phone = models.CharField(max_length=20)
    kind = models.IntegerField(verbose_name='Type',
                               choices=PHONE_TYPES,
                               default=1)

    owner = models.ForeignKey('Person')

    def __unicode__(self):.
        return "<{}:{}-{}:{}>".format(type(self).__name__, self.owner.fullname,
                                      self.get_kind_display(), self.phone)


class Instructor(Person):
    department = models.ForeignKey('Department', related_name='department')
    kind = models.IntegerField(verbose_name='Type', choices=INSTRUCTOR_TYPES)


@py3_compat
class Department(models.Model):
    name = models.CharField(max_length=30)
    head = models.OneToOneField(Instructor,
                                related_name='dean_or_principal',
                                limit_choices_to={'department__id': F('id'),
                                                  'kind': 1,
                                                  })


@py3_compat
class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10)
    department = models.ForeignKey('Department')


class Student(Person):
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
    course = models.ForeignKey('Course',
                               null=True,
                               limit_choices_to={'department':
                                                 F('department'), })


class Guardian(Person):
    occupation = models.CharField(max_length=30, default='')
    relationship = models.CharField(max_length=30, default='Father')
    emergency_contact = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    ward = models.ForeignKey('Student', null=True)
