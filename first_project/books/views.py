from django.contrib import messages
from django.shortcuts import render

from .forms import BookForm
from .models import Books


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Book added successfully!')
            form.save(commit=True)
    else:
        form = BookForm()

    context = {'form': form, }
    return render(request, 'add_book.html', context)


def books(request):
    context = {'books': Books.objects.all()}
    return render(request, 'books.html', context)
