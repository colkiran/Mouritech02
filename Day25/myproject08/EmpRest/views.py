from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status

class Emplist(APIView):

    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializeObj = EmployeeSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(serializeObj.data, status=status.HTTP_201_CREATED)
        return Response(serializeObj.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpUpdateDel(APIView):

    def get(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        empobj = Employee.objects.get(pk=pk)
        serializeObj = EmployeeSerializer(empobj)
        return Response(serializeObj.data)

    def put(self, request, pk):
        empobj = Employee.objects.get(pk=pk)
        empserialize = EmployeeSerializer(empobj, data=request.data)
        if empserialize.is_valid():
            empserialize.save()
            return Response(empserialize.data, status=status.HTTP_200_OK)
        return Response(empserialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        empobj = Employee.objects.get(pk=pk)
        empobj.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)