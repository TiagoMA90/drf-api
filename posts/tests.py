from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='test')
    
    def test_can_list_posts(self):
        user = User.objects.get(username='user')
        Post.objects.create(owner=user, title='title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='user', password='test')
        response = self.client.post('/posts/', {'title': 'title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='user', password='test')
        admin = User.objects.create_user(username='admin', password='test')
        Post.objects.create(
            owner=user, title='second title', content='admin\'s post'
        )
    
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'second title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_update_own_post(self):
        self.client.login(username='user', password='test')
        response = self.client.put('/posts/1/', {'title': 'third title'})
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, 'third title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_another_users_post(self):
        self.client.login(username='user', password='test')
        response = self.client.put('/posts/2/', {'title': 'third title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
