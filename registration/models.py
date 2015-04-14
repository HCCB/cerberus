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


@py3_compat
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    name_suffix = models.CharField(max_length=10)

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
    street1 = models.CharField(max_length=100, default='')
    street2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='Butuan City')
    province = models.CharField(max_length=100, default='Agusan del Norte')
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


class Student(Person):
    pass
