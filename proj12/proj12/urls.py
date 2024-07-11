
from django.contrib import admin
from django.urls import path
from A12.views import regaj, course_search_ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regaj/', regaj), 
    path('course_search_ajax/', course_search_ajax), 
]
