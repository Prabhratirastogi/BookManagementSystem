from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, BookRecommendation, Comment, Like, Review
from .utils import fetch_books_data
from django.core.paginator import Paginator
from .serializers import BookRecommendationSerializer,CommentSerializer, LikeSerializer,BookSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404

def fetch_books_view(request):
    query = request.GET.get('query', '')
    search_type = request.GET.get('search_type', 'all')
    max_results = int(request.GET.get('max_results', 40))
    page_number = int(request.GET.get('page', 1))

    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)

    search_type_mapping = {
        'title': f'intitle:{query}',
        'author': f'inauthor:{query}',
        'rating': f'averageRating:{query}'
    }
    if search_type not in search_type_mapping:
        return JsonResponse({'error': 'Invalid search type'}, status=400)

    query_param = search_type_mapping.get(search_type, query)

    data = fetch_books_data(query_param, max_results=max_results * page_number)
    if not data:
        return JsonResponse({'error': 'Failed to fetch books data'}, status=500)

    books_data = data.get('items', [])
    filtered_books = []

    for item in books_data:
        volume_info = item.get('volumeInfo', {})
        title = volume_info.get('title', 'No Title')
        authors = volume_info.get('authors', ['Unknown Author'])
        description = volume_info.get('description', 'No description available')
        cover_image = volume_info.get('imageLinks', {}).get('thumbnail', '')
        ratings = volume_info.get('averageRating', 0.0)

        # Save or retrieve the book from the database
        book, created = Book.objects.get_or_create(
            title=title,
            author=', '.join(authors),
            description=description,
            cover_image=cover_image,
            ratings=ratings
        )

        filtered_books.append({
            'id': book.id,
            'title': title,
            'author': ', '.join(authors),
            'description': description,
            'cover_image': cover_image,
            'ratings': ratings,
        })

    # Remove duplicates based on title, author, and description
    unique_books = {}
    for book in filtered_books:
        book_id = (book['title'], book['author'], book['description'])
        if book_id not in unique_books:
            unique_books[book_id] = book

    # Convert the dictionary to a list and apply pagination
    unique_books_list = list(unique_books.values())
    paginator = Paginator(unique_books_list, max_results)
    page_obj = paginator.get_page(page_number)

    return JsonResponse({
        'saved_books': page_obj.object_list,
        'page': page_obj.number,
        'total_pages': paginator.num_pages,
    })


class SubmitRecommendationsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookRecommendationSerializer(data=request.data)

        if serializer.is_valid():
            # Save the book recommendation with the current user as the recommender
            serializer.save(recommended_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return validation errors if the serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRecommendationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recommendations = BookRecommendation.objects.all()

        # Filtering by genre
        genre = request.GET.get('genre')
        if genre is not None:
            if genre.strip():  # Ensures the genre is not empty
                recommendations = recommendations.filter(genre__iexact=genre)
            else:
                return Response({"error": "Genre value cannot be empty."}, status=400)

        # Filtering by minimum rating
        min_rating = request.GET.get('min_rating')
        if min_rating:
            try:
                min_rating_value = float(min_rating)
                recommendations = recommendations.filter(rating__gte=min_rating_value)
            except ValueError:
                return Response({"error": "Invalid min_rating value."}, status=400)

        # Sorting
        sort_by = request.GET.get('sort_by')
        valid_sort_fields = ['rating', '-rating', 'publication_date', '-publication_date']
        if sort_by is not None:
            if sort_by.strip():  # Ensures the sort_by is not empty
                if sort_by in valid_sort_fields:
                    recommendations = recommendations.order_by(sort_by)
                else:
                    return Response({"error": "Invalid sort_by value."}, status=400)
            else:
                return Response({"error": "sort_by value cannot be empty."}, status=400)

        # Serialize and return the filtered and sorted recommendations
        serializer = BookRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)


class SubmitBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            # Include 'id' in the response
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Save the comment with the logged-in user
            comment = serializer.save(user=request.user)
            response_data = serializer.data
            response_data['message'] = f"You commented on '{comment.book.title}'"
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_id = request.data.get('book')
        if not Book.objects.filter(id=book_id).exists():
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        if Like.objects.filter(book_id=book_id, user=request.user).exists():
            return Response({"error": "You have already liked this book"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the like with the logged-in user
        like = Like.objects.create(book_id=book_id, user=request.user)
        serializer = LikeSerializer(like)
        response_data = serializer.data
        response_data['message'] = f"You liked the book '{like.book.title}'"
        return Response(response_data, status=status.HTTP_201_CREATED)


class CreateReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # Set the user to the logged-in user
            review = serializer.save(user=request.user)
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
class ListReviewsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        reviews = book.reviews.all() 
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
