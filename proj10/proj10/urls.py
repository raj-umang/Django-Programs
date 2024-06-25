
from django.contrib import admin
from django.urls import path
from P10.views import StudentDetailView, StudentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', StudentListView.as_view()),
    path('student_detail/<int:pk>/', StudentDetailView.as_view()),
]
