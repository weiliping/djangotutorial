from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Person  
from .serializers import PersonSerializer

class PersonView(APIView):
    def get(self, request):
        result = Person.objects.get(id=request.GET.get('id')) 
        serializers = PersonSerializer(result)  
        return Response({'status': 'success', "persons":serializers.data}, status=200)  
  
    def post(self, request):
        print(request)  
        serializer = PersonSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)