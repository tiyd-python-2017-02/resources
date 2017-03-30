from django.shortcuts import render
from rest_framework import viewsets
from .models import Ability, Task
from .serializers import AbilitySerializer, TaskSerializer


class AbilitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Ability.objects.all().order_by('name')
    serializer_class = AbilitySerializer

class TasksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('description')
    serializer_class = TaskSerializer
