from django.shortcuts import render
from .models import Student
from .serializers import StudenTSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
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