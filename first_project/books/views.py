
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from first_project.usecases import testpermission

from .forms import BookForm
from .models import Books
from .usecases import *


class AddBookView(CreateView):
    modal = Books
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = '/books/'

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            book = form.save(commit=False)
            book.author = self.request.user
            book.save()
        return redirect('books_view')


class BooksListView(ListView):
    modal = Books
    template_name = 'books.html'

    def get_queryset(self):
        return Books.objects.all()


class BookDetailsView(DetailView):
    modal = Books
    template_name = 'book_details.html'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    modal = Books
    form_class = BookForm
    template_name = 'update_book.html'
    success_url = '/books/'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False


@login_required
@user_passes_test(testpermission, login_url='books_view')
def delete_book(request, book_id: int):
    book = Books.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('books_view')


@login_required
def add_to_wishlist(request, book_id: int):
    book = Books.objects.get(id=book_id)
    added = send_to_wishlist(request, book_id, 'book')

    if not added:
        messages.success(
            request, f"Successfully added a book {book.title.upper()} into wishlist!")
    else:
        messages.warning(
            request, f"The book {book.title.upper()} already exists in your wishlist!")
    return redirect('books_view')
