# books/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import BookRecommendation,Book
from rest_framework import status
import json

class FetchBooksViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('book_list')

    def test_fetch_books_no_query(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'No query provided'})


class SubmitRecommendationsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.url = reverse('submit_recommendation')

    def test_submit_recommendation(self):
        data = {
            'title': 'Recommended Book',
            'author': 'Author Name',
            'description': 'Book Description',
            'genre': 'Fiction',
            'publication_date': '2022-01-01',
            'rating': 4.5
        }
        response = self.client.post(self.url, json.dumps(data), content_type='application/json')
        print(response.content)  # Debugging line
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertIn('id', response_data)
        self.assertEqual(response_data['title'], 'Recommended Book')


class LikeCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            cover_image='http://example.com/image.jpg',
            rating=4.5
        )
        self.client.login(username='testuser', password='password')
        self.url = reverse('create_like')

    def test_create_like(self):
        data = {'book': self.book.id}
        response = self.client.post(self.url, json.dumps(data), content_type='application/json')
        print(response.content)  # Debugging line
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertIn('message', response_data)
        self.assertEqual(response_data['message'], f"You liked the book '{self.book.title}'")
