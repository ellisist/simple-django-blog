from django.contrib import admin
from blog.models import Post, Comment, Author


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
