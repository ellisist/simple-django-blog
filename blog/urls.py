from django.urls import path
from blog.views import BlogHome, PostDetail


urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
