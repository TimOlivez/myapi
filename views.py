from django.shortcuts import render, get_object_or_404
from django.conf import settings    
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serialisers import (
    EmployeeSerializer,
    EmployeedetailSerializer,
    EmployeeEditSerializer,
)

# List all employees or add a new employee
@api_view(["GET", "POST"])
def employee_list_create(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific employee
@api_view(["GET", "PUT", "DELETE"])
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "GET":
        serializer = EmployeedetailSerializer(employee)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EmployeeEditSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        employee.delete()
        return Response({"msg": "Employee deleted"}, status=status.HTTP_204_NO_CONTENT)