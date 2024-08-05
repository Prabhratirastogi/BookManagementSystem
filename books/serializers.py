from rest_framework import serializers
from .models import BookRecommendation,Comment,Like, Book, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'cover_image', 'rating', 'pdf_file']


class BookRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecommendation
        fields = ['id','title', 'author', 'description', 'genre', 'publication_date', 'cover_image', 'rating']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['book', 'text', 'created_at']
        read_only_fields = ['user']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['book', 'created_at']
        read_only_fields = ['user']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Display the username of the user

    class Meta:
        model = Review
        fields = ['id', 'book', 'text', 'rating', 'user']
        read_only_fields = ['user']
