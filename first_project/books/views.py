from typing import Any

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import BookForm
from .models import Books

# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             book = form.save(commit=False)
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
