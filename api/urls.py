from django.urls import path
from .views import PostList , PostDetail ,CategoryList,CategoryDetail

app_name = 'api'

urlpatterns = [
    path('post/' ,PostList.as_view() , name='posts'),
    path('post/<int:pk>/' ,PostDetail.as_view(), name= 'post' ),
    path('category/',CategoryList.as_view() , name='categories'),
    path('category/<int:pk>',CategoryDetail.as_view(),name='category')

]