
from django.contrib import admin
from django.urls import path
from c1.views import get_cookie, set_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_cookie/', get_cookie ),
    path('set_cookie/', set_cookie ),
]
