from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import BookForm
from .models import Books

# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#             book = form.save(commit=False)
#         if form.is_valid():
#             # book.author = request.user
#             book.save()
#             messages.success(request, 'Book added successfully!')
#             return redirect('books_view')
#     else:
#         form = BookForm()

#     context = {'form': form}
#     return render(request, 'add_book.html', context)


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


# def books(request):
#     context = {'books': Books.objects.all()}
#     return render(request, 'books.html', context)

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


class BookUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
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


# class DeleteBook(DeleteView):
#     modal = Books
#     template_name = 'delete_book.html'
#     success_url = '/books/'

#     def get_queryset(self):
#         return Books.objects.filter(id=self.kwargs['pk'])

def delete_book(request, book_id: int):
    book = Books.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('books_view')
