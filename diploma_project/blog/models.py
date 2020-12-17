from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_VARIANT = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Ссылка')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE, verbose_name= 'Автор')
    body = models.TextField(verbose_name='Текст' )
    publish = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
    status = models.CharField(max_length=10, choices = STATUS_VARIANT, default='draft')
    image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='blog_likes')

    def likes_in_total(self):
        return self.likes.count()

    @property
    def imageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url

    
    class Meta:
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-publish',)
        get_latest_by = 'publish'


    
    def __str__ (self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name= 'Комментарий')
    body = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(User, related_name='comments_name', on_delete=models.CASCADE, verbose_name= 'Автор комментария')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    def __str__(self):
        return self.post.title
# Create your models here.
