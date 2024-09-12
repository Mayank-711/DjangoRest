from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    employee_id = serializers.IntegerField()
    position = serializers.CharField(max_length=100)
    
    def create_employee(self,validate_data):
        return Employee.objects.create(**validate_data)
    
    def update_employee(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.employee_id = validate_data.get('employee_id',instance.employee_id)
        instance.position = validate_data.get('position',instance.position)
        instance.save()
        return instance
