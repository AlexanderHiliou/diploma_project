from django.contrib import admin
from .models import Post, Comment, Tag



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'body')

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)

# Register your models here.
