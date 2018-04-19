from django.views.generic import ListView, DetailView

from blog.models import Post


class BlogHome(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5


class PostDetail(DetailView):
    model = Post
