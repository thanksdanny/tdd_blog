from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    # list_display 控制展示的字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # fields 控制表单展示的字段
    fields = ['title', 'body', 'category', 'tags', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
