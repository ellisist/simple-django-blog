from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Author, Post
from django.urls import reverse
from django.utils import timezone
import datetime


class TestBlogHome(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username="testuser1",
                                              password="pass@1234")
        test_author1 = Author.objects.create(user=test_user1,
                                             bio="a short bio")
        # create 20 posts
        num_posts = 20
        for num in range(num_posts):
            Post.objects.create(title="Example post {}".format(num),
                                text="This text doesn't matter",
                                author=test_author1, published=timezone.now()
                                - datetime.timedelta(days=num % 5))

    def test_paginates_by_5(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['post_list']) == 5)

    def test_posts_ordered_by_published(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('post_list' in resp.context)

        prev_date = 0
        for post in resp.context['post_list']:
            if(prev_date == 0):
                prev_date = post.published
            else:
                self.assertTrue(prev_date <= post.published)

    def test_template_used(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/index.html')


class TestPostDetailView(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username="testuser",
                                             password="pass@1234")
        test_author = Author.objects.create(user=test_user,
                                            bio="A short bio")
        Post.objects.create(title="Example post",
                            text="Some text for the post",
                            author=test_author)

    def test_template_used(self):
        resp = self.client.get(reverse('post-detail', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/post_detail.html')
