from rest_framework import serializers

from posts.models import Post


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['status']


    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer:
    pass