from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmissionData

# creating a router
router = DefaultRouter()

urlpatterns = [
    # Writing the API Views
    path("api/", EmissionData.as_view(), name="emission")
]