from django.urls import path

from .views import *

urlpatterns = [
    path("", books, name="books_view"),
    path("add_book", add_book, name="add_book"),
    # path("details/<int:book_id>", book_details, name="book_details"),
    # path("delete/<int:del_id>", delete_book, name="delete_book")
]
