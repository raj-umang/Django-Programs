from django.shortcuts import render
from django.http import HttpResponse
from A12.models import Student, Course

# Create your views here.

def regaj(request):
    if request.method == 'POST':
        sid=request.POST.get('sname')
        cid=request.POST.get('cname')
        student=Student.objects.get(id=sid)
        course=Course.objects.get(id=cid)
        res=student.enrolment.filter(id=cid)
        if res:
            return HttpResponse("<h1>Student already enrolled </h1>")
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled successfully </h1>")
    else:
        students=Student.objects.all()
        courses=Course.objects.all()
        return render(request,"regaj.html",{"students":students,
        "courses" :courses})
    
def course_search_ajax(request):
    if request.method == 'POST':
        cid=request.POST.get('cname')
        s=Student.objects.all() 
        student_list=list()
        for student in s:
            if student.enrolment.filter(id=cid):
                student_list.append(student)
        if len(student_list)==0:
            return HttpResponse("<h1>No Student enrolled </h1>")
        return render(request,"selected_stu.html",{ "student_list" :student_list})
    else:
        courses=Course.objects.all()
        return render(request,"course_search.html",{ "courses" :courses})
