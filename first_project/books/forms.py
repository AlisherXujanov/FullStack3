from django import forms
from django.contrib.auth.models import User

from .models import Books

genre_choices = (
    ("Fantasy", "Fantasy"),
    ("Science Fiction", "Science Fiction"),
    ("Drama", "Drama"),
    ("Action and Adventure", "Action and Adventure"),
    ("Romance", "Romance"),
    ("Mystery", "Mystery"),
    ("Horror", "Horror"),
)


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Book title",
                            help_text="How your book will be called")
    genre = forms.CharField(max_length=255, label="Genre", help_text="Enter main genre of your book",
                            widget=forms.Select(choices=genre_choices))
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="Price",
                               help_text="Please enter price")
    image = forms.ImageField(required=False, label="Book image",
                             help_text="Please upload book image")
    description = forms.CharField(max_length=255, label="Description", help_text="Please enter description",
                                  widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}))

    class Meta:
        model = Books
        fields = ['title', 'genre', 'price', 'image', 'description']
