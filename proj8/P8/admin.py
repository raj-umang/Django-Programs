from django.contrib import admin
from P8.models import Course, Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_usn' ,'student_sem') 
    ordering=('student_name',)
    search_fields = ['student_name']

admin.site.register(Course)
admin.site.register(Student)
