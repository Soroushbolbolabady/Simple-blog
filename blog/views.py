from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm
from .models import Post, Category


# Create your views here.


def index(request):
    posts = Post.objects.order_by('-pub_date')
    context = {
        'posts': posts,

    }
    return render(request, 'blog/index.html', context)


def posts(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'category': categories,
    }
    return render(request, 'blog/categories.html', context)


def category(request, name):
    category = Category.objects.get(name=name)
    posts = Post.objects.filter(category=category.id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/category.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            form.save()
            return HttpResponseRedirect('')
    else:
        form = ContactForm()
    context = {
        'form': form
        }
    return render(request, 'blog/contact.html', context)
