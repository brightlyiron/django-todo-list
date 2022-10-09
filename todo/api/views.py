from rest_framework import mixins, viewsets
from . import serializers
from .. import models


class TodoListAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TodoListSerializer
    queryset = models.Todo.objects.values('id', 'title', 'content').all()


todo_list_api = TodoListAPIView.as_view({'get': 'list'})
