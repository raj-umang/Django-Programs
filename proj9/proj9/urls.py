
from django.contrib import admin
from django.urls import path
from P9.views import add_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_project/', add_project),
]
