from django.urls import path
from .views import PetListCreate, PetDetailView, PetDetailApplicationView

urlpatterns = [
    path("", PetListCreate.as_view(), name="manage_pet"),
    path("<uuid:pk>", PetDetailView.as_view(), name="pet_details"),
    path(
        "<uuid:pk>/applications/",
        PetDetailApplicationView.as_view(),
        name="pet_application_details",
    ),
]
