from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Books


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            # book.author = request.user
            book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('books_view')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'add_book.html', context)


def books(request):
    context = {'books': Books.objects.all()}
    return render(request, 'books.html', context)
