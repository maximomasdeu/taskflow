from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

def health_check(request):
    return JsonResponse({"status": "ok", "service": "TaskFlow API"})

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("project").prefetch_related("tags").all()
    serializer_class = TaskSerializer
    @action(detail=False, methods=["get"])
    def romper(self, request):
        return 1 / 0  # error a propósito, SOLO para probar el 500
