from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='test')
    
    def test_can_list_posts(self):
        tiago = User.objects.get(username='user')
        Post.objects.create(owner=tiago, title='title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='user', password='test')
        response = self.client.post('/post/', {'title': 'title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_creat_post(self):
        response = selfclient.post('/posts/', {'title': 'title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)