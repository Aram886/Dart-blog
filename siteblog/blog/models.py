from django.db import models
from django.urls import reverse_lazy

"""
Category
=========
title, slug

Tag
=========
title, slug

Post
=========
title, slug, author, content, created_at, photo, views, category, tags
"""


class Category(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='Url', unique=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Tag'
        verbose_name_plural = "Tags"

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, verbose_name='Url', unique=True)
    author = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Number of views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = "Posts"