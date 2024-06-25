from django.shortcuts import render
from django.http import HttpResponse
# from reportlab.pdfgen import canvas
from  P11.models import Course, Student, ProjectReg
import csv

# Create your views here.
def construct_csv_from_model(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type = "text/csv")
    response['Content-Disposition'] = 'attachment; filename = "course_data.csv" '
    writer = csv.writer(response)
    writer.writerow(['Course Name', 'Course Code', 'Course Credits'])
    for course in courses:
        writer.writerow([course.course_name, course.course_code, course.course_credits])
    return response
