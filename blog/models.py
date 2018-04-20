from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    headshot = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.user.username


class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    published = models.DateTimeField(verbose_name="publish date/time",
                                     default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def is_published(self):
        "Returns False if 'published' is in future"
        return self.published <= timezone.now()

    class Meta:
        ordering = ['published']


class Comment(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
