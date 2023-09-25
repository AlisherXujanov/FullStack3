from django.urls import path

from .views import *

urlpatterns = [
    path("", BooksListView.as_view(), name="books_view"),
    path("add_book", AddBookView.as_view(), name="add_book"),
    path("book_details/<int:pk>", BookDetailsView.as_view(), name="book_details"),
    # path("details/<int:book_id>", book_details, name="book_details"),
    # path("delete/<int:del_id>", delete_book, name="delete_book")
]
