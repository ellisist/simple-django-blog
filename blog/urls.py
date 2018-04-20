from django.urls import path
from blog.views import BlogHome, PostDetail, AuthorDetail, AuthorPosts, AuthorList


urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('posts/author/<int:pk>/', AuthorPosts.as_view(), name='author-posts'),
    path('authors/', AuthorList.as_view(), name='author-list'),
]
