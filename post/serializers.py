from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()