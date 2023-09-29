from first_project.usecases import *

from .models import Books


def get_saved_books(request) -> list[Books]:
    books_ids = getItemsFromWishlist(request, "book")
    books = []
    for book_id in books_ids:
        if book := Books.objects.filter(id=book_id).first():
            books.append(book)
    return books
