from django.urls import path
from .views import ApplicationListCreate, ApplicationGetDelete

urlpatterns = [
    path("", ApplicationListCreate.as_view(), name="manage_application"),
    path("<uuid:pk>", ApplicationGetDelete.as_view(), name="application_details"),
]
