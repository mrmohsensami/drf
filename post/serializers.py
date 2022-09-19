from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ('id', 'title', 'body')
        fields = '__all__'
        # extra_kwargs = {
        #     'body' : {'write_only': True}
        # }

    def validate_title(self, value):
        if value == 'hello':
            raise serializers.ValidationError('title cant be hello')
        return value