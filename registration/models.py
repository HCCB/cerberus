from django.db import models

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
        middle = self.middle_name[:1]
        if middle:
            middle = ' {}.'.format(middle)
        return "{}, {}{}".format(self.last_name, self.first_name, middle)


class Address(models.Model):
    street1 = models.CharField(max_length=100, default='')
    street2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='Butuan City')
    province = models.CharField(max_length=100, default='Agusan del Norte')
    zip = models.CharField(max_length=10, default='8600')
    kind = models.IntegerField(choices=ADDRESS_TYPES)


class Phone(models.Model):
    phone = models.CharField(max_length=20)
    kind = models.IntegerField(verbose_name='Type', choices=PHONE_TYPES)


class Student(Person):
    pass
