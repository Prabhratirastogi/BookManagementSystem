### 1. Saved Books

**Response:**

```json
{
    "saved_books": [
        {
            "id": 98,
            "title": "Automated Reasoning",
            "author": "Christoph Benzmüller",
            "description": "No description available",
            "cover_image": "http://books.google.com/books/content?id=kmUREQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
            "ratings": 0.0
        },
        {
            "id": 99,
            "title": "Bearing Steels",
            "author": "J. J. C. Hoo",
            "description": "No description available",
            "cover_image": "http://books.google.com/books/content?id=wFC0IDYm-EcC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
            "ratings": 0.0
        }
    ],
    "page": 1,
    "total_pages": 2
}

### 2. Submit Book Recommendation

**Endpoint:**

`POST /recommendations/submit/`

**Request Body:**

```json
{
    "title": "Example Book Title",
    "author": "Author Name",
    "description": "A brief description of the book.",
    "genre": "Thriller",
    "rating": 3.5,
    "publication_date": "2022-01-01",
    "cover_image": "https://example.com/cover_image.jpg"
}


3. User Registration
Endpoint:

POST /register/

Request Body:

json
Copy code
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword",
    "password2": "testpassword"
}
Response:

json
Copy code
{
    "username": "testuser",
    "email": "testuser@example.com"
}
4. User Login
Endpoint:

POST /login/

Request Body:

json
Copy code
{
    "username": "testuser",
    "password": "testpassword"
}
Response:

json
Copy code
{
    "refresh": "refresh_token_here",
    "access": "access_token_here"
}
5. Filter Recommendations by Genre
Endpoint:

GET /recommendations/

Query Parameters:

genre: The genre to filter by (e.g., Thriller).
Response:

json
Copy code
{
    "title": "Example Book Title",
    "author": "Author Name",
    "description": "A brief description of the book.",
    "genre": "Thriller",
    "publication_date": "2022-01-01",
    "cover_image": "https://example.com/cover_image.jpg",
    "rating": 4.5
}
6. Sort Recommendations by Publication Date (Descending)
Endpoint:

GET /recommendations/

Query Parameters:

genre: The genre to filter by (e.g., Fiction).
sort_by: The field to sort by (e.g., publication_date).
Response:

Returns the sorted list of book recommendations.

7. Upload Books
Endpoint:

POST /books/upload/

Request Body:

json
Copy code
{
    "title": "Sample Book",
    "author": "John Doe",
    "description": "A great book about something interesting.",
    "cover_image": "http://example.com/image.jpg",
    "ratings": 4.5,
    "pdf_file": "http://127.0.0.1:8000/media/books/pdfs/sample.pdf"
}
Response:

Returns the details of the uploaded book.

8. Comment on Books
Endpoint:

POST /comments/

Request Body:

json
Copy code
{
    "book": 96,
    "text": "This is a sample comment."
}
Response:

json
Copy code
{
    "book": 96,
    "text": "This is a sample comment.",
    "created_at": "2024-08-05T02:29:52.148774Z"
}
9. Like a Book
Endpoint:

POST /likes/

Request Body:

json
Copy code
{
    "book": 95
}
Response:

json
Copy code
{
    "book": 95,
    "created_at": "2024-08-05T02:30:23.089843Z"
}
10. Review a Book
Endpoint:

POST /reviews/

Request Body:

json
Copy code
{
    "book": 95,
    "text": "Great book, highly recommend!",
    "rating": 5
}
Response:

json
Copy code
{
    "id": 4,
    "book": 95,
    "text": "Great book, highly recommend!",
    "rating": 5,
    "user": "testuser"
}
11. List Reviews of a Book
Endpoint:

GET /reviews/{book_id}/

Response:

json
Copy code
{
    "id": 1,
    "book": 95,
    "text": "Great book, highly recommend!",
    "rating": 5
}
Notes
All endpoints require proper authentication unless specified otherwise.
For protected endpoints, use the Authorization: Bearer {token} header.
Response formats and status codes follow RESTful standards.
Always check the status code and response body for error messages and additional details.
This documentation provides a comprehensive overview of the available APIs, making it easier for developers to understand and integrate the Book Management System into their applications. For further customization and enhancement, developers can refer to the underlying Django views, serializers, and models as required.

