from django.shortcuts import render
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from .serializers import EmployeeSerializer
import json
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse
# Create your views here.

def view_employee_api(request):
    if request.method =="GET":
        data = request.body
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id',None)
        if id is not None:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many =True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')

def create_employee(request):
    if request.method =="POST":
        data = request.body
        stream = BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data_Created'}
            json_data = JSONRenderer.render(res)
            return HttpResponse(json_data,content_type ='application/json')
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data,content_type ='application/json')
    
def update_employee(request):
    if request.method =="PUT":
        data = request.body
        stream = BytesIO(data)
        parsed_data = JSONParser.parse(stream)
        serializer = EmployeeSerializer(data=data)