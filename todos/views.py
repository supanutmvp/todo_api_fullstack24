from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Todo
from .serializers import TodoSerializer

# Get
class ListTodo(generics.ListCreateAPIView): 
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer

# getID / Update / Delete
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer

# Get = ListAPIView
# Get,Post = ListCreateAPIView
# getID , Put , delete = RetrieveUpdateDestroyAPIView