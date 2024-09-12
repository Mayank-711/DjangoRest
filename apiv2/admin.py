from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class StudentModel(admin.ModelAdmin):
    list_display =['id','name','employee_id','position']