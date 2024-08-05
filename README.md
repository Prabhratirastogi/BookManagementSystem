# Book Management System

This project is a Book Management System built using Django, a powerful web framework for building web applications. The system includes various functionalities such as fetching book data, user authentication, submitting book recommendations, and interacting with books through comments, likes, and reviews.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [API Documentation](#api-documentation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### Book Data Management
- Fetch book information from external sources.
- Upload book details, including title, author, description, cover image, and ratings.

### User Authentication
- Secure user registration and login with JWT (JSON Web Tokens).
- Password hashing and user session management.

### Book Recommendations
- Submit book recommendations with metadata like genre, rating, and publication date.
- Filter recommendations by genre and sort them by various criteria.

### Interactive Features
- Users can comment on books, like books, and leave reviews.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- pip (Python package installer)
- A virtual environment tool (optional but recommended)

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/book-management-system.git
    cd book-management-system
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup the Database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
    - The application can be accessed at `http://localhost:8000/`.

## API Documentation

Detailed API documentation is available in the [API Documentation](docs/API_Documentation.md) file. It includes descriptions of each endpoint, request/response examples, and authentication details.

## Usage

### User Registration and Authentication
- Register a new user or log in with an existing account.
- Use the provided JWT tokens for accessing protected endpoints.

### Fetch Book Data
- Use the `/fetch-books/` endpoint to search for books based on various criteria.

### Submit Book Recommendations
- Post recommendations using the `/recommendations/submit/` endpoint.

### Interact with Books
- Comment on books, like books, and submit reviews.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**.
2. **Create a New Feature Branch**:
    ```bash
    git checkout -b feature/YourFeature
    ```
3. **Commit Your Changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the Branch**:
    ```bash
    git push origin feature/YourFeature
    ```
5. **Open a Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
