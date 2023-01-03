from rest_framework import serializers
from blog.models import Post , Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        exclude=('slug',)