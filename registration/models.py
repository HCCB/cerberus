import datetime

from django.db import models

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
    kind = models.IntegerField(choices=ADDRESS_TYPES, default='Home')

    owner = models.ForeignKey('Person')

    def __unicode__(self):
        return "<{}:{}-{}>".format(type(self).__name__, self.owner.fullname,
                                   self.get_kind_display())


@py3_compat
class Phone(models.Model):
    phone = models.CharField(max_length=20)
    kind = models.IntegerField(verbose_name='Type',
                               choices=PHONE_TYPES,
                               default='Home')

    owner = models.ForeignKey('Person')

    def __unicode__(self):
        return "<{}:{}-{}>".format(type(self).__name__,
                                   self.owner.fullname,
                                   self.get_kind_display())


class Guardian(Person):
    pass


class Student(Person):
    civil_status = models.CharField(max_length=20, default='Single')
    citizenship = models.CharField(max_length=30, default='Filipino')
    religion = models.CharField(max_length=30, default='Roman Catholic')
    birthdate = models.DateField(default=datetime.date.today)
    birthplace = models.CharField(max_length=100, default='')

    enrollment_type = models.IntegerField(choices=ENROLLMENT_TYPES, default=1)
    school_level = models.IntegerField(choices=LEVEL_CHOICES, default=2)
    year_level = models.IntegerField(default=1)

    guardian = models.ForeignKey(Guardian, null=True, blank=True)
