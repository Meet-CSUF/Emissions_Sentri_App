from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Emission
from .serializers import EmissionSerializer

# Create your views here.
@api_view(["GET"])
def EmissionData(request):
    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer(queryset, many = True)
    return Response(serializer_class.data)
