from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from blog.models import Post , Category
from .serializers import PostSerializer , CategorySerializer
from .perimissions import IsOwnerOrReadOnly
# Create your views here.


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = PostSerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = CategorySerializer
