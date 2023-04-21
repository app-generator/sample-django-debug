from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test_logs", views.test_logs, name="test-logs"),
]
