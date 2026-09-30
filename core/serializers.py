from datetime import date

from rest_framework import serializers

from .models import Project, Task, Tag

class TagSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Tag 
        fields = ["id", "name"] 

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id", "project", "title", "description",
            "priority", "status", "due_date", "tags", "created_at",
        ]

    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError(
                "La fecha límite no puede ser en el pasado."
            )
        return value

    def validate(self, data):
        if data.get("status") == "completada" and not data.get("due_date"):
            raise serializers.ValidationError(
                "No se puede marcar una tarea como completada sin fecha límite registrada."
            )

        if data.get("status") == "en_progreso":
            project = data.get("project") or self.instance.project
            completed_tasks = project.tasks.filter(status="completada")
            if self.instance:
                completed_tasks = completed_tasks.exclude(pk=self.instance.pk)
            if not completed_tasks.exists():
                raise serializers.ValidationError(
                    "No se puede iniciar una tarea si el proyecto no tiene tareas completadas."
                )
        return data


class ProjectSerializer(serializers.ModelSerializer): 
    tasks = TaskSerializer(many=True, read_only=True) 

    class Meta: 
        model = Project 
        fields = ["id", "name", "description", "tasks", "created_at"]