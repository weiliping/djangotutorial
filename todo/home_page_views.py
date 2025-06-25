from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HomeView(APIView):
     
	permission_classes = (IsAuthenticated, )
	def get(self, request):
		content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
		return Response(content)
    