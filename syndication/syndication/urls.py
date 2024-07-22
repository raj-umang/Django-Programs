
from django.contrib import admin
from django.urls import path
from S1.feeds import LatestEntriesFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path("latest/feed/", LatestEntriesFeed()),
]
