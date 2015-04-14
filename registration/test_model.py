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

        self.student = Student.objects.first()

        self.phone = Phone(phone='9328896676', kind='Home', owner=self.student)

        self.address = Address(owner=self.student)

    def tearDown(self):
        pass

    def test_string_repr(self):
        fullname = self.student.fullname
        print self.student
        phone_str = self.phone.__str__()
        print phone_str
        self.assertEqual(phone_str, "<Phone:{}-Home>".format(fullname))
        address_str = self.address.__str__()
        print address_str
        self.assertEqual(address_str, "<Address:{}-Home>".format(fullname))

    def test_students(self):
        fullname = Student.objects.get(last_name='dela Cruz').fullname
        self.assertEqual(fullname, "dela Cruz, Juan F.")
        fullname = Student.objects.get(last_name='Santiago').fullname
        self.assertEqual(fullname, "Santiago, Pablo")
