from django.db import models

ADDRESS_TYPES = (
    'Home',
    'Work',
    'Permanent',
)

PHONE_TYPES = (
    'Home',
    'Work',
    'Mobile',
    'Fax',
    'Other',
)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "<{}:{}>".format(type(self).__name__, self._full_name)

    @property
    def fullname(self):
        """Get the fullname."""
        return "{} {} {}.".format(self.last_name,
                                  self.first_name,
                                  self.middle_name[0])


class Address(models.Model):
    street1 = models.CharField(max_length=100, default='')
    street2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='Butuan City')
    province = models.CharField(max_length=100, default='Agusan del Norte')
    zip = models.CharField(max_length=10, default='8600')
    kind = models.CharField(max_length=15, choices=ADDRESS_TYPES)
    person = models.ForeignKey(Person,
                               related_name='%(app_label)s_%(class)s' +
                               '_has_Address')


class Phone(models.Model):
    phone = models.CharField(max_length=20)
    kind = models.CharField(max_length=10, verbose_name='Type',
                            choices=PHONE_TYPES)
    person = models.ForeignKey(Person,
                               related_name='%(app_label)s_%(class)s_has_Phone')


class Student(Person):
    pass
