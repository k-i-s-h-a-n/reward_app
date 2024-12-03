from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import App, Task
from .serializers import AppSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]




def admin(request):
    return render(request, 'admin/firstPage.html')