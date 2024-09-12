"""
URL configuration for DjangoRest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import api.views as aviews
import apiv2.views as v2views
urlpatterns = [
    path('admin/', admin.site.urls),
]

api= [
    path('stuinfo/<int:pk>',aviews.student_detail,name='student_detail'), 
    path('stuinfo/',aviews.student_detail_all,name='student_detail_all'),
    path('add_student/',aviews.add_student,name='add_stu'), 
]

api_v2 = [
    path('employee_data/',v2views.view_employee_api,name='view_employee'),
]

urlpatterns = urlpatterns + api + api_v2