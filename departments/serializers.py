from rest_framework import serializers
from .models import Department
from employees.models import Employee

class EmployeeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'designation', 'is_active']

class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'manager', 'employees']