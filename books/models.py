from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(1), MaxValueValidator(5)])  # Limit rating to 1-5
    pdf_file = models.FileField(upload_to='books/pdfs/', null=True, blank=True)  # Add PDF file field

    def __str__(self):
        return self.title


class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cover_image = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(1), MaxValueValidator(5)])  # Limit rating to 1-5

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} on {self.book.title}'

class Like(models.Model):
    book = models.ForeignKey(Book, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} likes {self.book.title}'

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')  # Book being reviewed
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # User who wrote the review
    text = models.TextField() 
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Limit rating to 1-5

    def __str__(self):
        return f'Review by {self.user} for {self.book.title}'
