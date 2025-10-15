from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from.models import CustomUser
from .serializers import CustomUserSerializer

    
class UserViewSet(viewsets.ModelViewSet):
       queryset = CustomUser.objects.all()
       serializer_class = CustomUserSerializer
       permission_classes = [permissions.IsAuthenticated]
       
       def get_permissions(self):
           return CustomUser.objects.filter(id=self.request.user.id)
       def get_object(self):
             return self.request.user