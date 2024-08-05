from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import (
    fetch_books_view, 
    SubmitRecommendationsView, 
    BookRecommendationsView,
    LikeCreateView,
    CommentCreateView,
    SubmitBookView,
    CreateReviewView,
    ListReviewsView
)

class UrlsTest(SimpleTestCase):

    def test_fetch_books_url_resolves(self):
        url = reverse('book_list')
        self.assertEqual(resolve(url).func, fetch_books_view)

    def test_book_recommendations_url_resolves(self):
        url = reverse('book_recommendations')
        self.assertEqual(resolve(url).func.view_class, BookRecommendationsView)

    def test_submit_recommendation_url_resolves(self):
        url = reverse('submit_recommendation')
        self.assertEqual(resolve(url).func.view_class, SubmitRecommendationsView)

    def test_create_comment_url_resolves(self):
        url = reverse('create_comment')
        self.assertEqual(resolve(url).func.view_class, CommentCreateView)

    def test_create_like_url_resolves(self):
        url = reverse('create_like')
        self.assertEqual(resolve(url).func.view_class, LikeCreateView)

    def test_submit_book_url_resolves(self):
        url = reverse('submit_book')
        self.assertEqual(resolve(url).func.view_class, SubmitBookView)

    def test_create_review_url_resolves(self):
        url = reverse('create_review')
        self.assertEqual(resolve(url).func.view_class, CreateReviewView)

    def test_list_reviews_url_resolves(self):
        url = reverse('list_reviews', kwargs={'book_id': 1})
        self.assertEqual(resolve(url).func.view_class, ListReviewsView)
