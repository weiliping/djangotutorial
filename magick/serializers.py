from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)  
    last_name = serializers.CharField(max_length=30) 
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']