import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_books_data(query, max_results=40):
    api_key = os.getenv('GOOGLE_BOOKS_API_KEY')  # Fetch API key from environment variable
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}&maxResults={max_results+1}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Google Books API: {e}")
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None
