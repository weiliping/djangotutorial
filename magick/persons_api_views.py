from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Person  
from .serializers import PersonSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PersonView(APIView):
    @method_decorator(login_required, name="dispatch")
    def get(self, request):
        result = Person.objects.get(id=request.user.id) 
        serializers = PersonSerializer(result)
        # return JsonResponse(serializers.data)
        return Response({'status': 'success', "persons":serializers.data}, status=200)  
  
    def post(self, request):
        print(request)  
        serializer = PersonSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)