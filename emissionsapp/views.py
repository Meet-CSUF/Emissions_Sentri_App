from django.shortcuts import render
from rest_framework import generics
from .models import Emission
from .serializers import EmissionSerializer

# Create your views here.
class EmissionData(generics.ListCreateAPIView):
    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer
