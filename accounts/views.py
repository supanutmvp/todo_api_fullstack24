from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializers , UserDetailSerializers
from .models import User

class UserListCreateView(generics.ListCreateAPIView):
    parser_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializers
