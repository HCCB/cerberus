"""
unittest for models.py

test the create of objects and check the different functions.
make sure to do a proper test of each method and verify that the outputs are
correct.
"""
import datetime

from django.test import TestCase
from registration.models import Guardian, Student, Address, Phone, LEVEL_CHOICES


class StudentTestCase(TestCase):

    PHONE_NUMBER = '9328896677'
    ADDRESS = 'Hotel ni Pidro'

    def setUp(self):
        Student.objects.create(first_name='Juan',
                               middle_name='Felipe',
                               last_name='dela Cruz')
        Student.objects.create(first_name="Pablo",
                               middle_name='',
                               last_name='Santiago')

        self.student = Student.objects.first()
        self.guardian = Guardian.objects.create(first_name='John',
                                                middle_name='T',
                                                last_name='dela Cruz',
                                                occupation='Teacher',
                                                )
        self.phone = Phone(phone=self.PHONE_NUMBER,
                           kind=1,
                           )
        self.address = Address(street1=self.ADDRESS)

        self.student.address_set.add(self.address)
        self.student.phone_set.add(self.phone)
        self.student.guardian_set.add(self.guardian)
        self.student.save()

    def tearDown(self):
        pass

    def test_string_repr(self):
        fullname = self.student.fullname
        print self.student
        phone_str = self.phone.__str__()
        print phone_str
        self.assertEqual(phone_str,
                         "<Phone:{}-Home:{}>".format(fullname,
                                                     self.PHONE_NUMBER))
        address_str = self.address.__str__()
        print address_str
        self.assertEqual(address_str,
                         "<Address:{}-Home:{}>".format(fullname,
                                                       self.ADDRESS))

    def test_students(self):
        fullname = Student.objects.get(last_name='dela Cruz').fullname
        self.assertEqual(fullname, "dela Cruz, Juan F.")
        fullname = Student.objects.get(last_name='Santiago').fullname
        self.assertEqual(fullname, "Santiago, Pablo")

    def test_student_defaults(self):
        obj = Student.objects.first()

        # test some defaults values of the Student object
        self.assertEqual(obj.birthdate, datetime.date.today())

        self.assertEqual(obj.birthplace, '')

        self.assertEqual(obj.get_school_level_display(), LEVEL_CHOICES[1][1])

        self.assertEqual(obj.year_level, 1)

        self.assertEqual(obj.civil_status, 'Single')
        self.assertEqual(obj.citizenship, 'Filipino')
        self.assertEqual(obj.religion, 'Roman Catholic')

        self.assertEqual(obj.get_enrollment_type_display(), 'New')

    def test_student_guardian(self):
        obj = Student.objects.first()

        print obj

        guardians = obj.guardian_set.all()

        for g in guardians:
            print g

        self.assertIsNotNone(guardians, 'guadians should not be none, ' +
                             'it was assigned a value')

    def test_student_address(self):
        obj = Student.objects.first()
        address = obj.address_set.first()

        print "Address: ", address

        self.assertIsNotNone(address, 'address should not be none, ' +
                             'it was assigned a value')

    def test_student_phone(self):
        obj = Student.objects.first()
        phone = obj.phone_set.first()

        print "Phone: ", phone

        self.assertIsNotNone(phone, 'phone should not be none, ' +
                             'it was assigned a value')
