from django.shortcuts import render
from rest_framework.generics import ListAPIView
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
