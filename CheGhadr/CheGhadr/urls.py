from django.contrib import admin
from django.urls import re_path
from CheGhadr.views import (
    HomeView, ProductView, AboutView
    )

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('^$', HomeView.as_view()),
    re_path('^about$', AboutView.as_view()),
    re_path('^product', ProductView.as_view()),
]
