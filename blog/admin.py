from django.contrib import admin
from .models import Post, Comment ,Category


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date' ,'thumbnail')
    list_filter = ('title' , 'pub_date')
    search_fields = ('title' , 'text')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Post , PostAdmin)
admin.site.register(Category , CategoryAdmin)
