from django.test import TestCase
from models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name='Juan',
                               middle_name='Felipe',
                               last_name='dela Cruz')
        Student.objects.create(first_name="Pablo",
                               middle_name='',
                               last_name='Santiago')

    def test_students(self):
        fullname = Student.objects.first().fullname
        self.assertEqual(fullname, "dela Cruz, Juan F.")

