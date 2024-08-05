from django.test import TestCase
from books.models import Book, BookRecommendation, Comment, Like, Review
from books.serializers import BookSerializer, CommentSerializer
from django.contrib.auth.models import User

class BookSerializerTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            cover_image='http://example.com/image.jpg',
            rating=4.5
        )

    def test_book_serializer(self):
        serializer = BookSerializer(self.book)
        data = serializer.data
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['author'], 'Test Author')
        self.assertEqual(data['description'], 'Test Description')
        self.assertEqual(data['rating'], 4.5)

class CommentSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            cover_image='http://example.com/image.jpg',
            rating=4.5
        )
        self.comment = Comment.objects.create(
            book=self.book,
            user=self.user,
            text='Test comment'
        )

    def test_comment_serializer(self):
        serializer = CommentSerializer(self.comment)
        data = serializer.data
        self.assertEqual(data['text'], 'Test comment')
