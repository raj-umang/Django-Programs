from django.contrib import admin
from django.urls import path
from a1.views import evaluate_expression

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expression/', evaluate_expression, name="evaluate_expression")
]
