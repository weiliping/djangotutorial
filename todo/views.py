from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    
