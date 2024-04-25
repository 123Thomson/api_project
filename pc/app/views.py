from django.shortcuts import render
from rest_framework import generics
from .models import Laptop
from .serializers import LaptopSerializer

class LaptopViewset(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class= LaptopSerializer
