from books.models import Books
from books.usecases import *
from books.usecases import get_saved_books
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .usecases import *


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books_ids = []
        if wish_list := Session(self.request).get(WISH_LIST, []):
            books_ids = wish_list.get("book_ids", [])

        context.update({
            "books_ids": books_ids
        })
        # Do something
        return context


def wishlist_view(request):
    context = {
        "books": get_saved_books(request)
    }
    return render(request, 'wishlist.html', context)


def delete_from_wl(request, book_id: int):
    book = Books.objects.filter(id=book_id).first()
    delete_book_from_wl(request, book_id)

    messages.success(
        request, f"Successfully deleted {book.title} from wishlist")
    return redirect('wishlist_view')
