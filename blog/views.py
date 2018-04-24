from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from blog.models import Post, Author, Comment


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


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'published']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(user=self.request.user)
        post.save()
        return super().form_valid(form)


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['title', 'text']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return super().form_valid(form)


class UpdateAuthor(UserPassesTestMixin, UpdateView):
    model = Author
    fields = ['bio', 'headshot']

    def test_func(self):
        try:
            return self.request.user.author.pk == self.kwargs['pk']
        except AttributeError:
            return False


class UpdatePost(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'published']

    def test_func(self):
        try:
            return self.request.user.author.id == Post.objects.get(
                pk=self.kwargs['pk']).author.id
        except AttributeError:
            return False
