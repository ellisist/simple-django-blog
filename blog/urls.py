from django.urls import path
from blog.views import BlogHome, PostDetail, AuthorDetail, AuthorPosts
from blog.views import AuthorList, CreatePost, CreateComment, UpdateAuthor
from blog.views import UpdatePost


urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('posts/author/<int:pk>/', AuthorPosts.as_view(), name='author-posts'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('post/create/', CreatePost.as_view(), name='create-post'),
    path('post/<int:pk>/comment/', CreateComment.as_view(),
         name='create-comment'),
    path('author/<int:pk>/update/', UpdateAuthor.as_view(),
         name='update-author'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name='update-post'),
]
