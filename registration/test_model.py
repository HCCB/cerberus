from django.test import TestCase
from models import Student, Address, Phone


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name='Juan',
                               middle_name='Felipe',
                               last_name='dela Cruz')
        Student.objects.create(first_name="Pablo",
                               middle_name='',
                               last_name='Santiago')

        phone = Phone(phone='9328896676',
                      kind='Home',
                      owner=Student.objects.first())

        student = Student.objects.first()

        address = Address(owner=student)

        print student
        print phone
        print address

    def test_students(self):
        fullname = Student.objects.get(last_name='dela Cruz').fullname
        self.assertEqual(fullname, "dela Cruz, Juan F.")
        fullname = Student.objects.get(last_name='Santiago').fullname
        self.assertEqual(fullname, "Santiago, Pablo")
