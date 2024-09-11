from api import models
from rest_framework import serializers

class StudenTSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    roll_no = serializers.IntegerField()
    