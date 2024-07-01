
from django.contrib import admin
from django.urls import path
from P11.views import construct_csv_from_model, construct_pdf_from_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('construct_csv_from_model/', construct_csv_from_model, name='construct_csv_from_model'),
    path('pdf/', construct_pdf_from_model, name='construct_pdf_from_model'),
]
