from django.contrib import admin

from models import Student, Guardian, Department, Program, Instructor

# Register your models here.

admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Instructor)
