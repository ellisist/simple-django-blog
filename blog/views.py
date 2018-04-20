from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone
from blog.models import Post, Author


class BlogHome(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(published__lte=timezone.now())


class PostDetail(DetailView):
    model = Post


class AuthorDetail(DetailView):
    model = Author


class AuthorPosts(DetailView):
    model = Author
    template_name = 'blog/post_list.html'


class AuthorList(ListView):
    model = Author


class CreatePost(CreateView):
    pass
