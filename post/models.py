from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title