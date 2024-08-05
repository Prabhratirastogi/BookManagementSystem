from django.urls import path
from .views import fetch_books_view, SubmitRecommendationsView, BookRecommendationsView,LikeCreateView,CommentCreateView,SubmitBookView,CreateReviewView, ListReviewsView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fetch-books/', fetch_books_view, name='book_list'),
    path('recommendations/', BookRecommendationsView.as_view(), name='book_recommendations'),
    path('recommendations/submit/', SubmitRecommendationsView.as_view(), name='submit_recommendation'),
    path('comments/', CommentCreateView.as_view(), name='create_comment'),
    path('likes/', LikeCreateView.as_view(), name='create_like'),
    path('books/submit/', SubmitBookView.as_view(), name='submit_book'),
    path('reviews/', CreateReviewView.as_view(), name='create_review'),
    path('reviews/<int:book_id>/', ListReviewsView.as_view(), name='list_reviews'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
