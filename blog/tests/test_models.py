from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Author


class TestAuthorModel(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username="testuser",
                                              password="pass@1234")
        test_user2 = User.objects.create_user(username="testuser2",
                                              password="pass@1234")
        test_user3 = User.objects.create_user(username="testuser3",
                                              password="pass@1234")
        Author.objects.create(user=test_user1,
                              bio="A short bio")
        Author.objects.create(user=test_user2,
                              bio="A short bio",
                              name="Testy")
        Author.objects.create(user=test_user3,
                              bio="A short bio",
                              name="")

    def test_author_str(self):
        self.assertEqual(str(Author.objects.get(pk=1)), "testuser")
        self.assertEqual(str(Author.objects.get(pk=2)), "Testy")
        self.assertEqual(str(Author.objects.get(pk=3)), "testuser3")


class TestPostModel(TestCase):
    pass
