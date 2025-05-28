from rest_framework import serializers  
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# If you want to customize fields for detail, add, or edit, you can do so.
# Otherwise, you can use EmployeeSerializer for all operations.

class EmployeedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'