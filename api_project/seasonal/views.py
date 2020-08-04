from django.shortcuts import render
from rest_framework import viewsets

from .models import Fruit
from .serializers import FruitSerializers

# Create your views here.
class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializers
    