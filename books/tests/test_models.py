from django.test import TestCase
from django.contrib.auth.models import User
from books.models import Book, BookRecommendation, Comment, Like, Review

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            cover_image='http://example.com/image.jpg',
            rating=4.5
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.description, 'Test Description')
        self.assertEqual(self.book.rating, 4.5)
        self.assertEqual(str(self.book), 'Test Book')

class CommentModelTest(TestCase):
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

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Test comment')
        self.assertEqual(str(self.comment), f'{self.user.username} on {self.book.title}')
