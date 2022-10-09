from rest_framework import serializers


class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()

    def update(self, instance, validated_data):
        raise NotImplementedError("미구현")

    def create(self, validated_data):
        raise NotImplementedError("미구현")
