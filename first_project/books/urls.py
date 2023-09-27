from django.urls import path

from .views import *

urlpatterns = [
    path("", BooksListView.as_view(), name="books_view"),
    path("add_book", AddBookView.as_view(), name="add_book"),
    path("update_book/<int:pk>", BookUpdateView.as_view(), name="update_book"),
    path("book_details/<int:pk>", BookDetailsView.as_view(), name="book_details"),
    path("delete_book/<int:book_id>", delete_book, name="delete_book"),
    path('add_to_wishlist/<int:book_id>',
         add_to_wishlist, name="add_to_wishlist"),
]
