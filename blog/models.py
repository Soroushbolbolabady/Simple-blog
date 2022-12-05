from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    thumbnail = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField('date published')

    def get_absolute_url(self):
        return reverse("post detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],max_length=11)
    message = models.TextField()
