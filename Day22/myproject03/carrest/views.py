from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer

class CarList(APIView):

    def get(self, request):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        cars = self.get_queryset()
        serializer = CarSerializer(cars, many=True)
        return  Response(serializer.data)
