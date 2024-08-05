from django.contrib import admin
from .models import Book, BookRecommendation,Comment,Like, Review
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Fields to include in the search functionality
    list_filter = ('author',)  # Fields to filter by


admin.site.register(Book, BookAdmin)
admin.site.register(BookRecommendation)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Review)
