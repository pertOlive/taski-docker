"""докстринг."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """докстринг."""

    class Meta:
        """докстринг."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
