from django.contrib import admin

from models import Student, Guardian, Department, Program
from models import Instructor, Subject, Semester

# Register your models here.

admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Instructor)
admin.site.register(Subject)
admin.site.register(Semester)
