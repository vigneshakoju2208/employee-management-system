from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    def validate_designation(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Designation too short")
        return value
    class Meta:
        model = Employee
        fields = '__all__'