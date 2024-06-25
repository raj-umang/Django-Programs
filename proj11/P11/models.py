from django.db import models
from django.forms import ModelForm


class Course(models.Model):
    course_code=models.CharField(max_length=40)
    course_name=models.CharField(max_length=100)
    course_credits=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_usn=models.CharField(max_length=20)
    student_name=models.CharField(max_length=100 )
    student_sem=models.IntegerField()
    enrolment=models.ManyToManyField(Course)

    def __str__(self):
        return self.student_name + "(" + self.student_usn + ")"
    

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ptopic = models.CharField(max_length=200)
    planguages = models.CharField(max_length=200)
    pduration = models.IntegerField()

class ProjectReg(ModelForm):
    required_css_class = "required"
    class Meta:
        model = Project 
        fields = ['student', 'ptopic', 'planguages', 'pduration']