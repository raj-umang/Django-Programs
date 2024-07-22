from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def current_date_time(request):
    now = datetime.datetime.now()
    html = "<html><body><h1> It is now %s </h1></body></html>" %now
    return HttpResponse(html)

def four_hours_ahead(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=4)
    html = "<html><body><h1> After 4 hours It will be %s </h1></body></html>" %dt
    return HttpResponse(html)

def four_hours_before(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=-4)
    html = "<html><body><h1> Before 4 hours It was  %s </h1></body></html>" %dt
    return HttpResponse(html)
    
