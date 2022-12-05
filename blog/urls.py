from django.urls import path
from . import views

namespace = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path('post/<slug:slug>', views.posts, name='post'),
    path('category/' , views.categories, name='categories'),
    path('category/<str:name>' , views.category, name='category'),
    path('about/' , views.about , name='about'),
    path('contact/' , views.contact , name ='contact')
,]
