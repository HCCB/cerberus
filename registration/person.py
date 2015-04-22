#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base Objects for Person, descendants are:
  Student - student data
  Guardian - student's guardian
Created on Wed Apr 22 12:37:52 2015
"""

import sys

from django.db import models

from compat import py3_compat




@py3_compat
class Person(models.Model):    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    name_suffix = models.CharField(max_length=10, blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __unicode__(self):
        return u"<{}:{}>".format(type(self).__name__, self.fullname)

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
    ADDRESS_TYPES = (
        (1, 'Home'),
        (2, 'Work'),
        (3, 'Permanent'),
    )
    street1 = models.CharField(max_length=60, default='')
    street2 = models.CharField(max_length=60, default='')
    city = models.CharField(max_length=60, default='Butuan City')
    province = models.CharField(max_length=60, default='Agusan del Norte')
    zip = models.CharField(max_length=10, default='8600')
    kind = models.IntegerField(choices=ADDRESS_TYPES, default=1)

    owner = models.ForeignKey('Person')

    def __unicode__(self):
        return u"<{}:{}-{}:{}>".format(type(self).__name__, self.owner.fullname,
                                       self.get_kind_display(), self.street1)


@py3_compat
class Phone(models.Model):
    PHONE_TYPES = (
        (1, 'Home'),
        (2, 'Work'),
        (3, 'Mobile'),
        (4, 'Fax'),
        (5, 'Other'),
    )
    phone = models.CharField(max_length=20)
    kind = models.IntegerField(verbose_name='Type',
                               choices=PHONE_TYPES,
                               default=1)

    owner = models.ForeignKey('Person')

    def __unicode__(self):
        return u"<{}:{}-{}:{}>".format(type(self).__name__, self.owner.fullname,
                                       self.get_kind_display(), self.phone)


def main():
    """default main function, obviously"""
    pass

if __name__ == "__main__":
    sys.exit(main())

