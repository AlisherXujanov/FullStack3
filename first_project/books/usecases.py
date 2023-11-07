from first_project.usecases import *

from .models import Books
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60

SHORT_WAIT = SECOND * 3
LONG_WAIT = MINUTE * 10

SHORT_CACHING_TIME = MINUTE * 30
LONG_CACHING_TIME = HOUR * 2

class NoAuthApiView(APIView):
    """Doesn't require authentication"""
    permission_classes = [AllowAny]

class AuthApiView(NoAuthApiView):
    """Requires authentication"""
    permission_classes = [IsAuthenticated]



def get_saved_books(request) -> list[Books]:
    books_ids = getItemsFromWishlist(request, "book")
    books = []
    for book_id in books_ids:
        if book := Books.objects.filter(id=book_id).first():
            books.append(book)
    return books


def delete_book_from_wl(request, book_id: int):
    delete_item_from_wishlist(request, book_id, "book")
