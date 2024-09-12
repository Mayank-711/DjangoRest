from django.shortcuts import render
from .models import Student
from .serializers import StudenTSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from io import BytesIO
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#Single object
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer_data = StudenTSerializer(stu)
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data,content_type = 'application/json')

#ALL object
def student_detail_all(request):
    stu = Student.objects.all()
    serializer_data = StudenTSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data,content_type = 'application/json')

#ADD OBJECT
@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = request.body
        stream = BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        serializer = StudenTSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')