
from django.contrib import admin
from django.urls import path
from a1.views import current_date_time, four_hours_ahead, four_hours_before

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdt/', current_date_time),
    path('fha/', four_hours_ahead),
    path('fhb/', four_hours_before),
]
