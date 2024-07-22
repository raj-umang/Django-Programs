
from django.contrib import admin
from django.urls import path
from A6.views import home, aboutus, contactus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('about/', aboutus),
    path('contact/', contactus),
]
